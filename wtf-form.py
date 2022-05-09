import email
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length,Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email() )
