# -*- coding:utf-8 -*-
from wtforms import fields, validators
from flask_wtf import Form

class LoginForm(Form):
    username = fields.StringField(label=u'管理员账号', validators=[validators.required()])
    password = fields.PasswordField(label=u'密码', validators=[validators.required()])

    remember_me = fields.BooleanField('记住我')
    submit = fields.SubmitField('登陆')


