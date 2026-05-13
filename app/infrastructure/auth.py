# app/infrastructure/auth.py
from flask_login import LoginManager
from .orm_models import CustomerORM

login_manager = LoginManager()

def init_auth(app):
    # ログインが必要なページに未ログインでアクセスした時のリダイレクト先
    login_manager.login_view = "main.login"
    login_manager.login_message = "ログインが必要です。"
    login_manager.login_message_category = "info"
    
    login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # flask-loginがセッションからユーザーIDを取り出し、DBからユーザー情報を取得する
    return CustomerORM.query.get(int(user_id))