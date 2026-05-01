# run.py

from flask import Flask
import os

from app.interface.routes import main_bp
from app.infrastructure.database import init_db, migrate  # migrateをインポート


def create_app():
    # Flaskオブジェクトの生成
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

    # DB設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salon.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # .envにある

    # DB初期化
    init_db(app)
    app.register_blueprint(main_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)