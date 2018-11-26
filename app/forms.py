from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User


class PostForm(FlaskForm):
    post = StringField('Tweet...', validators=[DataRequired()])
    submit = SubmitField('Post')

class TitleForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    submit = SubmitField('Change Title')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    age = IntegerField('Age')
    bio = StringField('Bio')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already taken.')
