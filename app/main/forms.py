from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class PostForm(FlaskForm):

    title = StringField('Blog title')
    category= SelectField('Blog Category', choices=[('Select a category', 'Select a category'),('Music', 'Music'),('Adventures', 'Adventures'),('Animations', 'Animations'),('Fashion', 'Fashion'),('Nature', 'Nature'),('Celebrity', 'Celebrity')])
    content = TextAreaField('The Blog...')
    submit = SubmitField('Post')


class CommentForm(FlaskForm):

    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you...')
    submit = SubmitField('Submit')