# app\interface\routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from app.infrastructure.database import db
from werkzeug.security import check_password_hash
from app.infrastructure.orm_models import SalonORM, StaffORM, MenuORM

# Blueprintの作成
# 'main'はBlueprintの名前
# template_folderは、このファイル(routes.py)から見た相対パスで指定します
main_bp = Blueprint(
    'main', 
    __name__, 
    template_folder='../templates'  # デフォルト？
)

@main_bp.route("/")
def home():

    salon = SalonORM.query.first()

    return render_template(
        "home.html",
        salon=salon
    )


@main_bp.route("/reserve")
def reserve():

    salon = SalonORM.query.first()

    staffs = StaffORM.query.filter_by(
        is_active=True
    ).all()

    menus = MenuORM.query.filter_by(
        is_active=True
    ).all()

    return render_template(
        "reserve.html",
        salon=salon,
        staffs=staffs,
        menus=menus,
    )


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