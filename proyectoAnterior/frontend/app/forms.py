from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, FileField)
from wtforms.validators import InputRequired, Length, Email,EqualTo

class LoginForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = PasswordField('password', validators=[InputRequired()])
    remember_me = BooleanField('remember_me')

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(),Length(min=4,max=48)])
    email = StringField('email', validators=[InputRequired(),Email()])
    password = PasswordField('password', validators=[InputRequired()])
    confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password')])
    #Meter fechas , genero,etc

