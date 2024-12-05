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
        return redirect(url_for('board.boards'))
    return render_template('board/write.html', form=form)

@board.route('/boards/<int:post_id>',methods=["GET","POST"])
def view(post_id):
    post = Boards.query.get_or_404(post_id) #게시글의 작성 번호로 조회
    return render_template('board/view_id.html',post=post)

@board.route('/board/<int:post_id>/edit',methods=["GET","POST"])
def edit_post(post_id):
    post = Boards.query.get_or_404(post_id)
    form = BoardForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('게시글이 수정되었습니다.','success')
        return redirect(url_for('board.view',post_id=post.id))
    return render_template('board/edit.html',form=form, post=post)