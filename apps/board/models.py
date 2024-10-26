from datetime import datetime
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#db.Model을 상속한 클래스 작성
class Board(db.Model, UserMixin): 
    __tablename__="board"
    #컬럼명 정의
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, db.ForeignKey('users.id'))
    title = db.Column(db.String)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

    @property
    def password(self):
        raise AttributeError('읽어 들일 수 없음')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
  