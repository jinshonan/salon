from werkzeug.security import generate_password_hash

from run import app
from app.infrastructure.database import db

from app.infrastructure.orm_models import (
    SalonORM,
    StaffORM,
    CustomerORM,
    MenuORM,
)

# Enum
from app.domain.models import StaffRole


def seed():

    with app.app_context():

        # ---------------------------------------------------
        # 既存データ確認
        # ---------------------------------------------------

        existing_salon = SalonORM.query.first()

        if existing_salon:
            print("すでに初期データがあります")
            return

        # ---------------------------------------------------
        # Salon
        # ---------------------------------------------------

        salon = SalonORM(
            name="Cyberpunk Salon",
            address="東京都渋谷区神南1-2-3",
            phone="03-1234-5678",
            email="info@spunk-salon.jp",
            opening_time="10:00",
            closing_time="20:00",
        )

        db.session.add(salon)
        db.session.flush()  # salon.id を取得するため

        # ---------------------------------------------------
        # Staffs
        # ---------------------------------------------------

        staffs = [
            StaffORM(
                salon_id=salon.id,
                name="桐生 一馬",
                role=StaffRole.OWNER.value,
                email="owner@spunk-salon.jp",
                hashed_password=generate_password_hash("password123"),
            ),

            StaffORM(
                salon_id=salon.id,
                name="佐藤 美咲",
                role=StaffRole.NAIL_ARTIST.value,
                email="misaki@spunk-salon.jp",
                hashed_password=generate_password_hash("password123"),
            ),

            StaffORM(
                salon_id=salon.id,
                name="鈴木 彩",
                role=StaffRole.TRAINEE.value,
                email="aya@spunk-salon.jp",
                hashed_password=generate_password_hash("password123"),
            ),
        ]

        db.session.add_all(staffs)

        # ---------------------------------------------------
        # Customers
        # ---------------------------------------------------

        customers = [
            CustomerORM(
                name="田中 優子",
                email="yuko@example.com",
                phone="090-1111-2222",
                notes="ジェルネイル希望",
            ),

            CustomerORM(
                name="高橋 里奈",
                email="rina@example.com",
                phone="090-3333-4444",
                notes="爪が弱め",
            ),
        ]

        db.session.add_all(customers)

        # ---------------------------------------------------
        # Menus
        # ---------------------------------------------------

        menus = [
            MenuORM(
                salon_id=salon.id,
                name="ジェルネイル",
                description="シンプルなジェルネイル施術",
                price=6000,
                duration_minutes=90,
            ),

            MenuORM(
                salon_id=salon.id,
                name="フレンチネイル",
                description="人気のフレンチデザイン",
                price=7500,
                duration_minutes=120,
            ),

            MenuORM(
                salon_id=salon.id,
                name="ネイルケア",
                description="甘皮ケアと爪のメンテナンス",
                price=4000,
                duration_minutes=60,
            ),
        ]

        db.session.add_all(menus)

        # ---------------------------------------------------
        # commit
        # ---------------------------------------------------

        db.session.commit()

        print("初期データ投入完了")


if __name__ == "__main__":
    seed()