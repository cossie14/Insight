from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class BlogsForm(FlaskForm):
    blog_title = StringField('title',validators=[Required()])
    blog_description = StringField('blog description',validators=[Required()])
    story = TextAreaField('Give the blog content',validators=[Required()])
    category = SelectField('Category', choices=[('Religion','Religion'),('Politics','Politics'),('Love','Love'),('Cancer','Cancer'),('Science','Science')], validators=[Required()])
    author=StringField('Give author',validators=[Required()])
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write your bio.',validators = [Required()])
    submit = SubmitField('Submit')



class SubscribersForm(FlaskForm):

    email = StringField('Your Email Address')
    name = StringField('Enter your name',validators = [Required()])
    submit = SubmitField('Subscribe')