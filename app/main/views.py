from flask import Flask
from . import main
import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Post, Comment
from .forms import UpdateProfile, PostForm , CommentForm
from .. import db, photos
app = Flask(__name__)


# views
@main.route("/")
def index():
   '''
   title = "Post Perfect"
   '''
   title = 'Post Perfect'
   posts = Post.query.all()

   return render_template('index.html', title= title, posts = posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        post = Post(title=title, content=content,category=category)
        # post.save_post(post)
        db.session.add(post)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index', id=post.id))

    return render_template('new_post.html', title='New Post', post_form=form, post ='New Post')


@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        
        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content, post_id=id)

        # post.save_post(post)
        db.session.add(comment)
        db.session.commit()
        
    comment = Comment.query.filter_by(post_id=id).all()
    return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')

@main.route('/music/new', methods=['GET','POST'])
@login_required
def music(category = "Music"):

    musics = Post.query.filter_by(category = "Music")
    
    title = "Music Blogs"
    return render_template('music.html', musics= musics, title=title, post ='New Post')


@main.route('/animations/new', methods=['GET','POST'])
@login_required
def animations(category = "Animations"):

    animations = Post.query.filter_by(category = "Animations")
    
    title = "Animations Blogs"
    return render_template('animations.html', animations= animations, title=title, post ='New Post')


@main.route('/adventure/new', methods=['GET','POST'])
@login_required
def adventure(category = "Adventures"):

    adventures = Post.query.filter_by(category = "Adventures")
    
    title = "Adventures Blogs"
    return render_template('adventure.html', adventures= adventures, title=title, post ='New Post')


@main.route('/celebrity/new', methods=['GET','POST'])
@login_required
def celebrity(category = "Celebrity"):

    celebritys = Post.query.filter_by(category = "Celebrity")
    
    title = "Celebrity Blogs"
    return render_template('celebrity.html', celebritys= celebritys, title=title, post ='New Post')


@main.route('/nature/new', methods=['GET','POST'])
@login_required
def nature(category = "Nature"):

    natures = Post.query.filter_by(category = "Nature")
    
    title = "Nature Blogs"
    return render_template('nature.html', natures= natures, title=title, post ='New Post')

@main.route('/fashion/new', methods=['GET','POST'])
@login_required
def fashion(category = "Fashion"):

    fashions = Post.query.filter_by(category = "Fashion")
    
    title = "Fashion Blogs"
    
    return render_template('fashion.html', fashions= fashions, title=title, post ='New Post')