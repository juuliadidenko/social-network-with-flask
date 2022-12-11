from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
    BooleanField, SubmitField, TextAreaField)
from wtforms.validators import (DataRequired,
    ValidationError, Email, EqualTo, Length)
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[
        DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat password'), validators=[DataRequired(),
        EqualTo('password')]
    )
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                _l('Please use a different username'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                _l('Please use a different email address'))


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[Length(0, 140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(
                username=self.username.data).first()
            if user is not None:
                raise ValidationError(
                    _l('Please use a different username'))


class EmptyForm(FlaskForm):
    submit = SubmitField(_l('Submit'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[
        DataRequired(), Length(1, 140)])
    submit = SubmitField(_l('Submit'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[
        DataRequired(), Email()])
    submit = SubmitField(_l('Request password reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[
        DataRequired()])
    password2= PasswordField(_l('Repeat password'), validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Reset password'))
