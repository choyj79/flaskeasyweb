from flask import Flask, Blueprint, render_template, redirect, url_for
from app import db
from apps.crud.models import User
from apps.crud.forms import UserForm
from flask_login import login_required

#blueprint로 crud 앱을 생성
main = Blueprint(
    "main", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@main.route("/")
def index():
    return render_template("main/index.html")
