from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    # Equal to checks the variable name for the confirmation area. Can be done with email also.
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match.')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('This email is already in use. Try a different email.')

    def check_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username is taken.')

class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')
