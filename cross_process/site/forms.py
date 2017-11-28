from flask_wtf import Form, FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),
                                                   Length(min=4,max=15)])
    password = PasswordField('Password', validators=[InputRequired(),
                                                   Length(min=8, max=80)])
    remember = BooleanField('Remember Me')

class SignupForm(FlaskForm):
    username = StringField(u'Your name', validators=[InputRequired()])
    password = PasswordField(u'Your favorite password', validators=[InputRequired()])
    email = StringField(u'Your email address', validators=[Email(message="Invalid Email")])
    #birthday = DateField(u'Your birthday')

    """a_float = FloatField(u'A floating point number')
    a_decimal = DecimalField(u'Another floating point number')
    a_integer = IntegerField(u'An integer')

    now = DateTimeField(u'Current time',
                        description='...for no particular reason')
    sample_file = FileField(u'Your favorite file')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[Required('You must agree to not agree!')])

    submit = SubmitField(u'Signup') """
