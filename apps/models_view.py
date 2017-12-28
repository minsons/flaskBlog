from flask_admin import BaseView, expose,model
from flask_admin.contrib.sqla import ModelView
from apps.models import db,User,Category
from flask_admin.contrib import sqla
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask_admin import Admin, form
from flask import Flask, url_for
from sqlalchemy.event import listens_for
import os.path as op
import  os
from jinja2 import Markup

file_path = op.join(op.dirname(__file__), 'static')

class UserView2(ModelView):
    # def scaffold_list_columns(self):
    #     columns = ['username','email','password','avatar_hash']
    #     return columns
    # def scaffold_sortable_columns(self):
    #     columns = ['username','email','password','avatar_hash']
    #     return columns
    #
    # def scaffold_form(self):
    #     pass
    # def create_model(self,form):
    #     #print(obj.name)
    #     print(str(form.__dict__))
    #     category=Category(name="xiaobing2",count=12)
    #     user =User(username=form['username'],email=form['email'],password=form['password'])
    #     db.session.add(category)
    #     db.session.add(user)
    #     db.session.commit()

    def on_model_change(self,form, model, is_created):
        print(str(model.__dict__))
        category = Category(name="xiaob3",desc=str(model.id) ,count=12)
       #user = User(username=form['username'], email=form['email'], password=form['password'])
        db.session.add(category)
        #db.session.add(user)
        db.session.commit()

    def get_save_return_url(self,model,is_created=True):
        print(str(model.__dict__))
        category = Category(name="xiaob3", desc=str(model.id), count=12)
        # user = User(username=form['username'], email=form['email'], password=form['password'])
        db.session.add(category)
        # db.session.add(user)
        db.session.commit()
        return self.get_url('.details_view', id=model.id)


class CustomModelView(ModelView):
    list_template = 'admin/list.html'
    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('test1.html')


class EditorMdWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(EditorMdWidget, self).__call__(field, **kwargs)

class EditorMdAreaField(TextAreaField):
    widget = EditorMdWidget()

from apps.models import Article

@listens_for(Article, 'after_delete')
def del_image(mapper, connection, target):
    if target.img:
        # Delete image
        try:
            os.remove(op.join(file_path, target.img))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(file_path,
                              form.thumbgen_filename(target.img)))
        except OSError:
            pass


class ArticleModelView(sqla.ModelView):
    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    # extra_css = ["/static/editorMd/css/editormd.css"]
    # extra_js = ["/static/editorMd/js/editormd.js","/static/editorMd/js/myeditor.js"]

    def _list_thumbnail(view, context, model, name):
        if not model.img:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.img)))

    column_formatters = {
        'img': _list_thumbnail
    }

    column_exclude_list = ['content', ]
    # form_overrides = {
    #     'body': EditorMdAreaField
    # }

    form_extra_fields = {
        'img': form.ImageUploadField('Image',
                                      base_path=file_path,
                                      relative_path='uploadFile/',
                                      thumbnail_size=(100, 100, True)),
        'tag':form.Select2Field('请选择',choices=[('xiaoming','xiaoming'),('xiao2','xodk2')])
    }

