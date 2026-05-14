# app\interface\reserve.py

from datetime import datetime

from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.interface.main_bp import main_bp

from app.infrastructure.orm_models import (
    MenuORM,
    ReservationMenuORM,
    ReservationORM,
    SalonORM,
    StaffORM,
    db,
)

# need to see understand how to separate this from routes.py

@main_bp.route("/reserve", methods=["GET", "POST"])
@login_required
def reserve():

    salon  = SalonORM.query.first()
    staffs = StaffORM.query.filter_by(is_active=True).all()
    menus  = MenuORM.query.filter_by(is_active=True).all()

    if request.method == "POST":

        # ── フォーム値の取得 ──────────────────────────────────
        menu_id        = request.form.get("menu_id",        type=int)
        staff_id       = request.form.get("staff_id",       type=int)
        date_str       = request.form.get("date",           type=str)
        time_str       = request.form.get("time",           type=str)
        customer_notes = request.form.get("customer_notes", default="", type=str)

        # ── 簡易バリデーション ────────────────────────────────
        if not all([menu_id, staff_id, date_str, time_str]):
            # 本番では flash() + フォームの再表示が望ましい
            return render_template(
                "reserve.html",
                salon=salon,
                staffs=staffs,
                menus=menus,
                error="必須項目をすべて入力してください",
            )

        # ── start_at の組み立て ───────────────────────────────
        try:
            start_at = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        except ValueError:
            return render_template(
                "reserve.html",
                salon=salon,
                staffs=staffs,
                menus=menus,
                error="日時の形式が正しくありません",
            )

        # ── DB書き込み ────────────────────────────────────────
        # 1. 予約のメインレコードを作成
        reservation = ReservationORM(
            salon_id       = salon.id,
            customer_id    = current_user.id,   # flask-login
            staff_id       = staff_id,
            start_at       = start_at,
            status         = "pending",
            customer_notes = customer_notes.strip(),
        )
        db.session.add(reservation)
        db.session.flush()  # reservation.id を確定させてから中間テーブルへ

        # 2. 選択されたメニューのマスター情報を取得する（← ここが重要！）
        selected_menu = MenuORM.query.get(menu_id)

        if not selected_menu:
            # メニューが見つからない場合のハンドリング
            return "Menu not found", 400

        # 3. 中間テーブルに「その時点の情報」をコピーして保存
        reservation_menu = ReservationMenuORM(
            reservation_id   = reservation.id,
            menu_id          = selected_menu.id,
            menu_name        = selected_menu.name,           # 名前をコピー
            price_snapshot   = selected_menu.price,          # 価格をコピー
            duration_minutes = selected_menu.duration_minutes # 時間をコピー
        )
        db.session.add(reservation_menu)
        db.session.commit()

        # ── 確認ページへリダイレクト ─────────────────────────
        return redirect(url_for("main.reserve_confirm", reservation_id=reservation.id))

    # ── GET ──────────────────────────────────────────────────
    return render_template(
        "reserve.html",
        salon=salon,
        staffs=staffs,
        menus=menus,
    )


"""
pending -> confirmed
"""

@main_bp.route("/reserve/confirm/<int:reservation_id>")
@login_required
def reserve_confirm(reservation_id: int):

    reservation = ReservationORM.query.filter_by(
        id          = reservation_id,
        customer_id = current_user.id,
        status      = "pending",          # pending 以外は表示しない
    ).first_or_404()

    return render_template(
        "reserve_confirm.html",
        reservation = reservation,
    )


@main_bp.route("/reserve/confirm/<int:reservation_id>/commit", methods=["POST"])
@login_required
def reserve_confirm_post(reservation_id: int):

    reservation = ReservationORM.query.filter_by(
        id          = reservation_id,
        customer_id = current_user.id,
        status      = "pending",          # 二重送信対策：pending のみ更新
    ).first_or_404()

    reservation.status = "confirmed"
    db.session.commit()

    return redirect(url_for("main.mypage"))