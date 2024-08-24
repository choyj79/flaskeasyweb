from flask import Flask, Blueprint
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #앱의 config 설정
    app.config.from_mapping(
            SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ",
            SQLALCHEMY_DATABASE_URI =f"sqlite:///{Path(__file__).parent.parent/'local.sqlite'}", 
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLALCHEMY_ECHO = True #sql언어를 로그에 출력
            )

    # SQLAlchemy와 앱을 연계한
    db.init_app(app) 
    # Migrate와 앱을 연계한다
    Migrate(app, db)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud,url_prefix="/crud") 

    return app