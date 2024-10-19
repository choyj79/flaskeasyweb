from datetime import datetime
from apps.app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#db.Model을 상속한 클래스 작성
class User(db.Model, UserMixin): 
    __tablename__="users"
    #컬럼명 정의
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, index=True)
    password_hash = db.Column(db.String)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError('읽어 들일 수 없음')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    #비밀번호 확인 메서드
    def verity_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_duplicate_email(self):
        User.query.filter_by(email=self.email).first() is not None

#이거 여기에ㅔ!!!!!
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User_auth(db.Model): 
    __tablename__="users_auth"
    #컬럼명 정의
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, index=True)
    password_hash = db.Column(db.String)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    @property 
    def password(self):
        raise AttributeError('읽어 들일 수 없음')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
