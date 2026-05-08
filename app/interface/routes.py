# app\interface\routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from app.infrastructure.database import db
from werkzeug.security import check_password_hash
from app.infrastructure.orm_models import SalonORM

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