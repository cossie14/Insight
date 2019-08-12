from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import create_app
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),index = True)
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    blogs = db.relationship('Blog', backref = 'user', lazy ="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):

    __tablename__='roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role', lazy="dynamic")

    def save_role(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.name}'
class Blog(db.Model):
    __tablename__='blogs'

    id = db.Column(db.Integer,primary_key = True)
    blog_title = db.Column(db.String(255))
    blog_description = db.Column(db.String(255))
    story = db.Column(db.String())
    category = db.Column(db.String(255))
    posted  = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    # This defines the relationships with other tables
    author = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'blog',lazy="dynamic")

    # This method saves the blog posts
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    # Returns all the blogs from the database
    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.filter_by(id=id)
        return blogs

    def __repr__(self):
        return f'Blog {self.blog_title}'

class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id)
        return comments

    @classmethod
    def delete_comment(cls,comment):
        db.session.delete(comment)
        db.session.commit()

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'