from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class HelloForm(FlaskForm):
    name=StringField('昵称',validators=[DataRequired(),Length(1,20)])
    body=TextAreaField('内容',validators=[DataRequired(),Length(1,200)])
    submit=SubmitField()