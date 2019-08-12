from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BlogsForm
from ..models import Blogs,User
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db,photos
from ..email import mail_message

import markdown2

@main.route("/")
@main.route("/home")
def index():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Welcome to Blog Insight'

   page = request.args.get('page', 1, type=int)
  

   return render_template('index.html')

@main.route('/blog/can')
def can():
   blog=blog.query.filter_by(name='cancer')
   return render_template('can.html', blog=blog)


@main.route('/blog/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_blogpost(id):
    """
    Edit a blogpost in the database
    """

    if not current_user.is_admin:
        abort(403)

    blogpost = Blogs.query.get(id)
    form = BlogForm()

    if form.validate_on_submit():

        blogpost.topic = form.topic.data
        blogpost.content = form.content.data
        blogpost.title =form.title.data

        # Updated bloginstance
        db.session.add(blogpost)
        db.session.commit()

        title='New Blog'

        return redirect(url_for('main.single_blog',id=blogpost.id))


    form.title.data = blogpost.title
    form.content.data = blogpost.content
    form.topic.data= blogpost.topic

    return render_template('blog.html',action="Edit", blogpost_form= form, legend='Update Post')

@main.route('/comment/delete/<int:blogs_id>' ,methods=['GET', 'POST'])
@login_required
def delete_comment(blogs_id):

    blogpost = Blogs.query.filter_by(id=blogs_id).first()
    comment = Comments.query.filter_by(blogs_id=blogs_id).first()

    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('main.blogpost', comment=comment, blogpost=blogpost, blogs_id=blogs_id))

@main.route('/subscribe', methods=['GET','POST'])
def subscriber():

    subscriber_form=SubscriberForm()
    blogs = Blogs.query.order_by(Blogs.date.desc()).all()

    if subscriber_form.validate_on_submit():

        subscriber= Subscriber(email=subscriber_form.email.data,name = subscriber_form.name.data)

        db.session.add(subscriber)
        db.session.commit()

        mail_message("Hello, Welcome Blog Insight.","email/welcome_subscriber",subscriber.email,subscriber=subscriber)

        title= "Blog Insight"
        return render_template('index.html',title=title, blogs=blogs)

    subscriber = Blogs.query.all()

    blog = Blogs.query.all()


    return render_template('subscribe.html',subscriber=subscriber,subscriber_form=subscriber_form,blog=blog)