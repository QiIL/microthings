from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from app import app

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default=False)