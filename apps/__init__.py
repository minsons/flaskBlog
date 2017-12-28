# -*- coding:utf-8 -*-
from flask import Flask, request,make_response,session

from flask_login import LoginManager
from flask_babelex import Babel



app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
login_manager = LoginManager()

def create_app(config=None):
    #app.config.from_object(config)
    if config is not None:
        app.config.from_pyfile(config)
    # send CORS headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
                ##response.headers['Authorization'] = 'xiaominggessdfs3432ds34ds32432cedsad332e23'
        return response

    from apps.models import db,User,Menu,Category,Article
    db.init_app(app)


    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    from apps.blog.views import init_api
    init_api(app)

    from flask_admin.contrib.sqla import ModelView
    from flask_admin import Admin
    from .models_view import  UserView2,CustomModelView,AnalyticsView,ArticleModelView
    admin = Admin(app, name='microblog', template_mode='bootstrap3',base_template='admin/mybase.html')
    admin.add_view(UserView2(User, db.session))
    # models = [Menu,Category]
    # for model in models:
    #     admin.add_view(
    #         CustomModelView(model, db.session, category='Models'))
    admin.add_view(CustomModelView(Menu, db.session,category='Models'))
    admin.add_view(CustomModelView(Category, db.session , category='Models'))

    admin.add_view(AnalyticsView(name='分析报告', endpoint='analytics'))
    admin.add_view(ArticleModelView(Article, db.session))
    babel = Babel(app)

    # from werkzeug.wsgi import SharedDataMiddleware
    # app.add_url_rule('/uploads/<filename>', 'uploaded_file',
    #                  build_only=True)
    # app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    #     '/uploads': app.config['UPLOAD_FOLDER']
    # })



    @babel.localeselector
    def get_locale():
        if request.args.get('lang'):
            session['lang'] = request.args.get('lang')
        return session.get('lang', 'zh')

    return app
