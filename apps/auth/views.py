from flask import Flask, Blueprint, render_template, redirect, url_for
from app import db
from apps.crud.models import User_auth
from apps.crud.forms import UserForm
import subprocess

#blueprint로 crud 앱을 생성
auth = Blueprint(
    "auth", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@auth.route("/")
def index():
    return render_template("auth/index.html")

@auth.route("/users/new", methods=["GET", "POST"])
def create_user():
    # UserForm을 인스턴스화한다
    form = UserForm()

    # 폼의 값을 벨리데이트한다
    if form.validate_on_submit():
        # 사용자를 작성한다
        user = User_auth(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        # 사용자를 추가하고 커밋한다
        db.session.add(user)
        db.session.commit()

        # 사용자의 일람 화면으로 리다이렉트한다
        return redirect(url_for("auth.users"))
    return render_template("auth/create.html", form=form)
@auth.route('/user/<user_id>',methods=["GET","POST"])
def edit_user(user_id):
    form = UserForm()
    user = User_auth.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud.users'))
    return render_template('crud/edit.html',user=user, form=form)

@auth.route('/users')
def users():
    users = User_auth.query.all()
    return render_template('auth/index.html', users = users)

@auth.route('/game')
def run_game():
    # 여기에 .exe 파일 실행
    exe_path = r'C:\\Users\\User\\Documents\\shooting_game.exe'  # 실행할 exe 파일의 경로
    subprocess.Popen(exe_path)  # exe 파일을 실행
    return "게임 실행 중!"