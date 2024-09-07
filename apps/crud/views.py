from flask import Flask, Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm

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
    # user = User(
    #     username = '조유정',
    #     email = 'cho@naver.com',
    #     userid = 'cho',
    #     password_hash = '1111'
    # )
    # db.session.add(user) #사용자추가
    # db.session.commit() #커밋하기
    # db.session.query(User).all()
    # db.session.query(User).filter_by(id=1).all()
    db.session.query(User).delete() #데이터 전체 지우기
    db.session.commit()
    return '콘솔 로그 확인!' 

@crud.route("/users/new", methods=["GET", "POST"])
def create_user():
    # UserForm을 인스턴스화한다
    form = UserForm()

    # 폼의 값을 벨리데이트한다
    if form.validate_on_submit():
        # 사용자를 작성한다
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        # 사용자를 추가하고 커밋한다
        db.session.add(user)
        db.session.commit()

        # 사용자의 일람 화면으로 리다이렉트한다
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

@crud.route('/users')
def users():
    users = User.query.all()
    return render_template('crud/index.html', users = users)

@crud.route('/user/<user_id>',methods=["GET","POST"])
def edit_user(user_id):
    form = UserForm()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud.users'))
    return render_template('crud/edit.html',user=user, form=form)
