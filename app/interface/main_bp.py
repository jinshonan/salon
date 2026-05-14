# app\interface\main_bp.py

from flask import Blueprint

main_bp = Blueprint(
    'main', 
    __name__, 
    template_folder='../templates' 
)

# Blueprintの作成
# 'main'はBlueprintの名前
# template_folderは、このファイル(routes.py)から見た相対パスで指定します