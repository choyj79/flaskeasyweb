from flask import Flask, Blueprint, render_template
from apps.app import db
from apps.crud.models import User

#blueprint로 crud 앱을 생성
crud = Blueprint(
    "crud", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@crud.route("/")
def index():
    print("!!!!!!!!!!!")
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(User).all()
    return '콘솔 로그 확인!' 
