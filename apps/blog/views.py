# -*- coding:utf-8 -*-
import json
from flask import jsonify, request,session,redirect,url_for,flash,render_template
from apps.models import User
from apps.models import db
from apps.blog.forms import LoginForm
from flask_login import login_user

ALLOWED_file_EXTENSIONS = set(['md', 'MD', 'word', 'txt', 'py', 'java', 'c', 'c++', 'xlsx'])
ALLOWED_photo_EXTENSIONS = set(['png', 'jpg', 'xls', 'JPG', 'PNG', 'gif', 'GIF'])

def init_api(app):
    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/login')
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user =User.query.filter_by(username=form.username.data)
            if user is not None and user.verity_password(form.password.data):
                login_user(user,form.remember_me.data)
                return redirect(request.args.get('next') or url_for('admin.index'))
            flash('无效的用户名或者密码')
        return render_template('/login.html',form=form)

    @app.route('/index')
    def init_test():
        return render_template('/index.html')

    def allowed_photo(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_photo_EXTENSIONS

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_file_EXTENSIONS

    from random import Random
    def random_str(randomlength=5):
        _str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            _str += chars[random.randint(0, length)]
        return _str

    from werkzeug.utils import secure_filename
    from datetime import date
    import os
    @app.route('/file/upload',methods=[ 'POST'])
    def editor_pic():
        image_file = request.files['editormd-image-file']
        bpdir = os.path.abspath(os.path.dirname(__file__))
        if image_file and allowed_photo(image_file.filename):
            try:
                filename = secure_filename(image_file.filename)
                filename = str(date.today()) + '-' + random_str() + '-' + filename
                file_path = os.path.join(bpdir, '../static/editorFile', filename)
                image_file.save(file_path)
                qiniu_link = "/static/editorFile/"+filename
                data = {
                    'success': 1,
                    'message': 'image of editor.md',
                    'url': qiniu_link
                }
                return json.dumps(data)
            except Exception as e:
                print("error is coming")
        else:
            return u"没有获得图片或图片类型不支持"