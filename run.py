# run.py

from flask import Flask
import os

from app.interface.main_bp import main_bp
import app.interface  # route登録用: app\interface\init.py

from app.infrastructure.database import init_db, migrate 
from app.infrastructure.auth import init_auth  

from dotenv import load_dotenv  

# アプリ生成の前に環境変数を読み込む
load_dotenv()

def create_app():
    # Flaskオブジェクトの生成
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

    # DB設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salon.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'develop-mode-tiny-secret')
    
    # DB初期化
    init_db(app)

    # auth初期化
    init_auth(app) 

    # ルート初期化
    app.register_blueprint(main_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)