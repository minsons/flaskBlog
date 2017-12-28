from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from datetime import  datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password= db.Column(db.String(128))
    avatar_hash = db.Column(db.String(32))
    session_token='123213dsfw3432'

    from apps import login_manager
    @login_manager.user_loader
    def load_user(userid):
        user = User.query.filter_by(id=userid).first()
        return user

    def verity_password(self,password):
        return password==self.password

    def get_id(self):
        return self.session_token

    def __repr__(self):
        return '<User %r>' % self.username


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    author_name = db.Column(db.String(64))
    author_email = db.Column(db.String(64))
    avatar_hash = db.Column(db.String(32))
    disabled = db.Column(db.Boolean, default=False)
    comment_type = db.Column(db.String(64), default='comment')
    reply_to = db.Column(db.String(128), default='notReply')

    def __str__(self):
        return "Comment(id='%s')" % self.id

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    desc = db.Column(db.String(64),  nullable=True)
    create_time   = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(),nullable=True)
    count = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Category %r>' % self.name

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    parent_id=db.Column(db.Integer, db.ForeignKey('menu.id'),nullable=True)
    menus = db.relationship('Menu')
    orders =  db.Column(db.Integer,nullable=True)
    link = db.Column(db.String(128), unique=True, nullable=False)
    create_time  = db.Column(db.DateTime,nullable=True)

    def __repr__(self):
        return '<Menu %r>' % self.name
# def session_commit():
#     try:
#         db.session.commit()
#     except SQLAlchemyError as e:
#         db.session.rollback()
#         reason = str(e)
#         return reason

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    img = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime, nullable=True)
    tag = db.Column(db.String(32), nullable=True)


    def __repr__(self):
        return '<Article %r>' % self.title