# app\interface\routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from app.infrastructure.database import db
from werkzeug.security import check_password_hash
from app.infrastructure.orm_models import SalonORM, StaffORM, MenuORM, CustomerORM

from flask_login import login_user, logout_user, current_user, login_required

from app.interface.main_bp import main_bp

@main_bp.route("/")
def home():

    salon = SalonORM.query.first()

    return render_template(
        "home.html",
        salon=salon
    )

@main_bp.route("/login", methods=["GET", "POST"])
def login():
    # すでにログインしている場合はホームへリダイレクト
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        # データベースからユーザーを検索
        user = CustomerORM.query.filter_by(email=email).first()

        # ユーザーが存在し、パスワードが一致するか確認
        if not user or not check_password_hash(user.password, password):
            flash("メールアドレスまたはパスワードが正しくありません。", "error")
            return redirect(url_for("main.login"))

        # ログイン成功
        login_user(user, remember=remember)
        
        # 次のページ（nextパラメータ）があればそこへ、なければホームへ
        next_page = request.args.get('next')
        return redirect(next_page or url_for("main.home"))

    # GETリクエスト時はログイン画面を表示
    return render_template("login.html")

@main_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@main_bp.route("/mypage")
@login_required
def mypage():
    return render_template("mypage.html", user=current_user)


# @main_bp.route("/reserve")
# def reserve():

#     salon = SalonORM.query.first()

#     staffs = StaffORM.query.filter_by(
#         is_active=True
#     ).all()

#     menus = MenuORM.query.filter_by(
#         is_active=True
#     ).all()

#     return render_template(
#         "reserve.html",
#         salon=salon,
#         staffs=staffs,
#         menus=menus,
#     )


@main_bp.route("/staffs")
def staffs():

    salon = SalonORM.query.first()

    staffs = StaffORM.query.filter_by(
        is_active=True
    ).all()

    return render_template(
        "staffs.html",
        salon=salon,
        staffs=staffs,
    )


@main_bp.route("/menus")
def menus():

    salon = SalonORM.query.first()

    menus = MenuORM.query.filter_by(
        is_active=True
    ).all()

    return render_template(
        "menus.html",
        salon=salon,
        menus=menus,
    )