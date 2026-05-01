"""
app/domain/models.py
Clean Architecture - Domain Layer
ビジネスロジックの中心。外部ライブラリ（SQLAlchemyなど）に依存しない純粋なドメインモデル。
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class ReservationStatus(Enum):
    PENDING   = "pending"    # 予約受付中
    CONFIRMED = "confirmed"  # 確定
    CANCELLED = "cancelled"  # キャンセル
    COMPLETED = "completed"  # 施術完了


class StaffRole(Enum):
    OWNER      = "owner"      # オーナー
    NAIL_ARTIST = "nail_artist"  # ネイリスト
    TRAINEE    = "trainee"    # 研修中


# ---------------------------------------------------------------------------
# Value Objects（値オブジェクト）
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PhoneNumber:
    """電話番号（フォーマット検証つき）"""
    value: str

    def __post_init__(self):
        digits = self.value.replace("-", "").replace(" ", "")
        if not digits.isdigit() or not (10 <= len(digits) <= 11):
            raise ValueError(f"無効な電話番号: {self.value}")


@dataclass(frozen=True)
class Email:
    """メールアドレス"""
    value: str

    def __post_init__(self):
        if "@" not in self.value or "." not in self.value.split("@")[-1]:
            raise ValueError(f"無効なメールアドレス: {self.value}")


@dataclass(frozen=True)
class Money:
    """金額（円）"""
    amount: int  # 円単位

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("金額は0以上である必要があります")

    def __add__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)

    def __str__(self) -> str:
        return f"¥{self.amount:,}"


# ---------------------------------------------------------------------------
# Entities
# ---------------------------------------------------------------------------

@dataclass
class Salon:
    """店舗"""
    id: Optional[int]
    name: str
    address: str
    phone: PhoneNumber
    email: Email
    opening_time: str   # 例: "10:00"
    closing_time: str   # 例: "20:00"
    created_at: datetime = field(default_factory=datetime.now)

    def __repr__(self) -> str:
        return f"<Salon id={self.id} name={self.name}>"


@dataclass
class Staff:
    """スタッフ（ネイリスト）"""
    id: Optional[int]
    salon_id: int
    name: str
    role: StaffRole
    email: Email
    hashed_password: str
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)

    def is_owner(self) -> bool:
        return self.role == StaffRole.OWNER

    def __repr__(self) -> str:
        return f"<Staff id={self.id} name={self.name} role={self.role.value}>"


@dataclass
class Customer:
    """顧客"""
    id: Optional[int]
    name: str
    email: Email
    phone: PhoneNumber
    notes: str = ""          # アレルギーや要望などの備考
    created_at: datetime = field(default_factory=datetime.now)

    def __repr__(self) -> str:
        return f"<Customer id={self.id} name={self.name}>"


@dataclass
class Menu:
    """メニュー（施術内容）"""
    id: Optional[int]
    salon_id: int
    name: str                # 例: "ジェルネイル（手）"
    description: str
    price: Money
    duration_minutes: int    # 施術時間（分）
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)

    def __repr__(self) -> str:
        return f"<Menu id={self.id} name={self.name} price={self.price}>"


@dataclass
class ReservationMenu:
    """予約とメニューの中間エンティティ（1予約に複数メニュー対応）"""
    menu_id: int
    menu_name: str           # 予約時点の名称をスナップショット保存
    price_snapshot: Money    # 予約時点の価格をスナップショット保存
    duration_minutes: int


@dataclass
class Reservation:
    """予約"""
    id: Optional[int]
    salon_id: int
    customer_id: int
    staff_id: int
    menus: list[ReservationMenu]   # 複数メニュー
    start_at: datetime
    status: ReservationStatus = ReservationStatus.PENDING
    customer_notes: str = ""       # 顧客からの要望
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    # --- ドメインロジック ---

    @property
    def total_price(self) -> Money:
        """合計金額"""
        return sum(
            (m.price_snapshot for m in self.menus),
            start=Money(0)
        )

    @property
    def total_duration_minutes(self) -> int:
        """合計施術時間（分）"""
        return sum(m.duration_minutes for m in self.menus)

    @property
    def end_at(self) -> datetime:
        """終了予定時刻"""
        from datetime import timedelta
        return self.start_at + timedelta(minutes=self.total_duration_minutes)

    def confirm(self) -> None:
        if self.status != ReservationStatus.PENDING:
            raise ValueError("確定できるのはPENDING状態の予約のみです")
        self.status = ReservationStatus.CONFIRMED
        self.updated_at = datetime.now()

    def cancel(self) -> None:
        if self.status == ReservationStatus.COMPLETED:
            raise ValueError("完了済みの予約はキャンセルできません")
        self.status = ReservationStatus.CANCELLED
        self.updated_at = datetime.now()

    def complete(self) -> None:
        if self.status != ReservationStatus.CONFIRMED:
            raise ValueError("完了にできるのはCONFIRMED状態の予約のみです")
        self.status = ReservationStatus.COMPLETED
        self.updated_at = datetime.now()

    def is_cancellable(self) -> bool:
        return self.status in (
            ReservationStatus.PENDING,
            ReservationStatus.CONFIRMED
        )

    def __repr__(self) -> str:
        return (
            f"<Reservation id={self.id} "
            f"customer_id={self.customer_id} "
            f"start_at={self.start_at} "
            f"status={self.status.value}>"
        )