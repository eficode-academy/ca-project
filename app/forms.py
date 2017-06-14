from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class PostForm(Form):
    title = StringField('Title')
    user_name = StringField('user_name')
    body  = StringField('Body')

