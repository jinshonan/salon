"""
app/infrastructure/orm_models.py
Clean Architecture - Infrastructure Layer
SQLAlchemyのORMテーブル定義。DBの都合（カラム型、外部キーなど）はここだけが知っている。
domain/models.py とは完全に独立している。
"""

from datetime import datetime
from app.infrastructure.database import db


# ---------------------------------------------------------------------------
# SalonORM
# ---------------------------------------------------------------------------

class SalonORM(db.Model):
    __tablename__ = "salons"

    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(100), nullable=False)
    address      = db.Column(db.String(255), nullable=False)
    phone        = db.Column(db.String(20),  nullable=False)
    email        = db.Column(db.String(255), nullable=False, unique=True)
    opening_time = db.Column(db.String(5),   nullable=False)  # "10:00"
    closing_time = db.Column(db.String(5),   nullable=False)  # "20:00"
    created_at   = db.Column(db.DateTime,    nullable=False, default=datetime.now)

    # リレーション
    staffs       = db.relationship("StaffORM",       back_populates="salon", lazy="select")
    menus        = db.relationship("MenuORM",         back_populates="salon", lazy="select")
    reservations = db.relationship("ReservationORM",  back_populates="salon", lazy="select")

    def __repr__(self) -> str:
        return f"<SalonORM id={self.id} name={self.name}>"


# ---------------------------------------------------------------------------
# StaffORM
# ---------------------------------------------------------------------------

class StaffORM(db.Model):
    __tablename__ = "staffs"

    id              = db.Column(db.Integer,     primary_key=True)
    salon_id        = db.Column(db.Integer,     db.ForeignKey("salons.id"), nullable=False)
    name            = db.Column(db.String(100), nullable=False)
    role            = db.Column(db.String(20),  nullable=False)   # StaffRole.value を保存
    email           = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    is_active       = db.Column(db.Boolean,     nullable=False, default=True)
    created_at      = db.Column(db.DateTime,    nullable=False, default=datetime.now)

    # リレーション
    salon        = db.relationship("SalonORM",       back_populates="staffs")
    reservations = db.relationship("ReservationORM", back_populates="staff", lazy="select")

    def __repr__(self) -> str:
        return f"<StaffORM id={self.id} name={self.name}>"


# ---------------------------------------------------------------------------
# CustomerORM
# ---------------------------------------------------------------------------

class CustomerORM(db.Model):
    __tablename__ = "customers"

    id         = db.Column(db.Integer,     primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(255), nullable=False, unique=True)
    phone      = db.Column(db.String(20),  nullable=False)
    notes      = db.Column(db.Text,        nullable=False, default="")
    created_at = db.Column(db.DateTime,    nullable=False, default=datetime.now)

    # リレーション
    reservations = db.relationship("ReservationORM", back_populates="customer", lazy="select")

    def __repr__(self) -> str:
        return f"<CustomerORM id={self.id} name={self.name}>"


# ---------------------------------------------------------------------------
# MenuORM
# ---------------------------------------------------------------------------

class MenuORM(db.Model):
    __tablename__ = "menus"

    id               = db.Column(db.Integer,     primary_key=True)
    salon_id         = db.Column(db.Integer,     db.ForeignKey("salons.id"), nullable=False)
    name             = db.Column(db.String(100), nullable=False)
    description      = db.Column(db.Text,        nullable=False, default="")
    price            = db.Column(db.Integer,     nullable=False)  # 円単位で保存
    duration_minutes = db.Column(db.Integer,     nullable=False)
    is_active        = db.Column(db.Boolean,     nullable=False, default=True)
    created_at       = db.Column(db.DateTime,    nullable=False, default=datetime.now)

    # リレーション
    salon = db.relationship("SalonORM", back_populates="menus")

    def __repr__(self) -> str:
        return f"<MenuORM id={self.id} name={self.name} price={self.price}>"


# ---------------------------------------------------------------------------
# ReservationORM
# ---------------------------------------------------------------------------

class ReservationORM(db.Model):
    __tablename__ = "reservations"

    id             = db.Column(db.Integer,     primary_key=True)
    salon_id       = db.Column(db.Integer,     db.ForeignKey("salons.id"),    nullable=False)
    customer_id    = db.Column(db.Integer,     db.ForeignKey("customers.id"), nullable=False)
    staff_id       = db.Column(db.Integer,     db.ForeignKey("staffs.id"),    nullable=False)
    start_at       = db.Column(db.DateTime,    nullable=False)
    status         = db.Column(db.String(20),  nullable=False, default="pending")  # ReservationStatus.value
    customer_notes = db.Column(db.Text,        nullable=False, default="")
    created_at     = db.Column(db.DateTime,    nullable=False, default=datetime.now)
    updated_at     = db.Column(db.DateTime,    nullable=False, default=datetime.now, onupdate=datetime.now)

    # リレーション
    salon    = db.relationship("SalonORM",    back_populates="reservations")
    customer = db.relationship("CustomerORM", back_populates="reservations")
    staff    = db.relationship("StaffORM",    back_populates="reservations")
    menus    = db.relationship("ReservationMenuORM", back_populates="reservation",
                               cascade="all, delete-orphan", lazy="select")

    def __repr__(self) -> str:
        return f"<ReservationORM id={self.id} status={self.status}>"


# ---------------------------------------------------------------------------
# ReservationMenuORM（中間テーブル）
# ---------------------------------------------------------------------------

class ReservationMenuORM(db.Model):
    """
    予約とメニューの中間テーブル。
    price_snapshot / menu_name は予約時点の値をスナップショット保存する。
    （後でメニューが変更・削除されても予約履歴が壊れない）
    """
    __tablename__ = "reservation_menus"

    id               = db.Column(db.Integer,     primary_key=True)
    reservation_id   = db.Column(db.Integer,     db.ForeignKey("reservations.id"), nullable=False)
    menu_id          = db.Column(db.Integer,     db.ForeignKey("menus.id"),         nullable=False)
    menu_name        = db.Column(db.String(100), nullable=False)   # スナップショット
    price_snapshot   = db.Column(db.Integer,     nullable=False)   # スナップショット（円）
    duration_minutes = db.Column(db.Integer,     nullable=False)   # スナップショット

    # リレーション
    reservation = db.relationship("ReservationORM", back_populates="menus")
    menu        = db.relationship("MenuORM")

    def __repr__(self) -> str:
        return f"<ReservationMenuORM reservation_id={self.reservation_id} menu={self.menu_name}>"