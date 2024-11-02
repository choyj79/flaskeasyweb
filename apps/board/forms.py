from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length

#사용자 신구 장성, 편집 폼 클래스
class BoardForm(FlaskForm):
    title = StringField(
        "제목",
        validators=[
            DataRequired(message='사용자명은 필수입니다.'),
            length(max=30, message='30자 이내로 입력해주세요.')
        ]
    )

    content = StringField(
        '내용',
        validators=[
            DataRequired(message='내용은 필수입니다.'),
            length(max=500, message='500자 이내로 입력해주세요.')
        ]
    )
    

    submit = SubmitField('신규등록')