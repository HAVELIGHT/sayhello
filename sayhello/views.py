from sayhello import app
from flask import render_template,flash,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class HelloForm(FlaskForm):
    name=StringField('昵称',validators=[DataRequired(),Length(1,20)])
    body=TextAreaField('内容',validators=[DataRequired(),Length(1,200)])
    submit=SubmitField()

@app.route('/',methods=['GET','POST'])
def index():
    form=HelloForm()
    if form.validate_on_submit():
        flash('你的消息发给了全世界!')
        return redirect(url_for('index'))
    return render_template('index.html',form=form)