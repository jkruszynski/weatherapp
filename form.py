from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ZipcodeForm(FlaskForm):
    zipcode = StringField('Zip Code')
    submit = SubmitField('Update Weather')