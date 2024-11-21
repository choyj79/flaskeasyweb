from flask import Flask, Blueprint, render_template, redirect, url_for,flash, request
from app import db
from apps.board.models import Boards
from apps.board.forms import BoardForm
from flask_login import login_user, logout_user, current_user, login_required

#blueprint로 crud 앱을 생성
board = Blueprint(
    "board", 
    __name__, 
    template_folder="templates",
    static_folder="static"
)

@board.route("/")
def index():
    board = Boards.query.all()
    return render_template("board/index.html", board = board)

#게시글목록리스트
@board.route('/boards')
def boards():
    posts = Boards.query.order_by(Boards.created_at.desc()).all()
    return render_template('board/view.html', posts = posts)

#게시판 글쓰기
@board.route('/boards/write', methods=['GET','POST'])
@login_required
def write():
    form = BoardForm()

    if form.validate_on_submit():
        new_post = Boards(
            title = form.title.data,
            content = form.content.data,
            author_id = current_user.id
        )

        db.session.add(new_post)
        db.session.commit()

        flash('글이 성공적으로 작성되었습니다.','success')
        return redirect(url_for('board/boards'))
    return render_template('board/write.html', form=form)