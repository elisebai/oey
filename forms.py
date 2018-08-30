from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import Post

class LoginForm(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')


class PostForm(FlaskForm):
  #  # datetime =

    boatname = StringField('船名',
                        validators=[DataRequired(), Length(min=1, max=20)])

    price = StringField('价格',
                           validators=[DataRequired(), Length(min=1, max=20)])

    length = StringField('长度',
                           validators=[DataRequired(), Length(min=1, max=20)])

    numberofguests = StringField('核载人数',
                        validators=[DataRequired(), Length(min=1, max=20)])

    numberofcabins = StringField('仓位数',
                           validators=[DataRequired(), Length(min=1, max=20)])

    bodylength = StringField('船身长度',
                           validators=[DataRequired(), Length(min=1, max=20)])

    beamlength = StringField('梁长',
                        validators=[DataRequired(), Length(min=1, max=20)])

    draft = StringField('吃水深度',
                           validators=[DataRequired(), Length(min=1, max=20)])

    crewnumber = StringField('船员人数',
                           validators=[DataRequired(), Length(min=1, max=20)])      

    builtyear = StringField('建造时间',
                           validators=[DataRequired(), Length(min=1, max=20)])

    producer = StringField('制造商',
                        validators=[DataRequired(), Length(min=1, max=20)])

    engine = StringField('引擎',
                           validators=[DataRequired(), Length(min=1, max=20)])

    cruisespeed = StringField('航行速度',
                           validators=[DataRequired(), Length(min=1, max=20)])       
                                         
    submit = SubmitField('提交')

class InfoForm(FlaskForm):

    interestedboat = StringField('船名',
                        validators=[DataRequired(), Length(min=1, max=20)])

    destination = StringField('目的地',
                           validators=[DataRequired(), Length(min=1, max=20)])

    sex = StringField('性别',
                           validators=[DataRequired(), Length(min=1, max=20)])

    name = StringField('名字''',
                        validators=[DataRequired(), Length(min=1, max=20)])

    email = StringField('邮箱地址',
                           validators=[DataRequired(), Length(min=1, max=20)])

    phone = StringField('电话',
                           validators=[DataRequired(), Length(min=1, max=20)])

    availabletime = StringField('方便电话时间',
                           validators=[DataRequired(), Length(min=1, max=20)])

    notes = StringField('备注',
                           validators=[DataRequired(), Length(min=1, max=20)])

    submit = SubmitField('提交')