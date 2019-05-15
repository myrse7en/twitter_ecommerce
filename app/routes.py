# import necessary fucntions and classes
from app import app, db
from app.models import Post, User, Product
from flask import render_template, url_for, redirect, flash
from app.forms import PostForm, TitleForm, LoginForm, RegisterForm
from datetime import datetime
from flask_login import current_user, login_user, logout_user, login_required

# create page routes
@app.route('/')
@app.route('/index')
def index():
    products = Product.query.all()

    # products = {
    #     101: {
    #         "id": 101,
    #         "title": "Soap",
    #         "price": 4.95,
    #         "url": "http://placehold.it/250x250",
    #         "desc": "This bar of soap is a bar of soapy soap."
    #     },
    #     102: {
    #         "id": 102,
    #         "title": "Grapes",
    #         "price": 3.85,
    #         "url": "http://placehold.it/250x250",
    #         "desc": "These grapes are abundle of grapey grapes."
    #     },
    #     103: {
    #         "id": 103,
    #         "title": "Oranges",
    #         "price": 67.85,
    #         "url": "http://placehold.it/250x250",
    #         "desc": "This box is a box of orangey oranges."
    #     },
    #     104: {
    #         "id": 104,
    #         "title": "Oranges",
    #         "price": 67.85,
    #         "url": "http://placehold.it/250x250",
    #         "desc": "This box is a box of orangey oranges."
    #     },
    #     105: {
    #         "id": 105,
    #         "title": "Oranges",
    #         "price": 67.85,
    #         "url": "http://placehold.it/250x250",
    #         "desc": "This box is a box of orangey oranges."
    #     }
    # }


    return render_template('index.html', products=products)

# posts_dict = {
#     0: {
#         'date': 'Sept. 9th, 2018',
#         'name': 'Max',
#         'tweet': 'Today I had cereal for breakfast.'
#     },
#     1: {
#         'date': 'July 1st, 2018',
#         'name': 'Kelly',
#         'tweet': 'Went for a run downtown.'
#     },
#     2: {
#         'date': 'June 21st, 2018',
#         'name': 'Max',
#         'tweet': 'Got a new job!! Working for the man.'
#     },
#     3: {
#         'date': 'March 4th, 2018',
#         'name': 'Kelly',
#         'tweet': 'Hiking is fun, get outside.'
#     },
#     4: {
#         'date': 'February 8th, 2018',
#         'name': 'Kelly',
#         'tweet': 'This is a sample text. This is a sample text.'
#     },
#     5: {
#         'date': 'October 10th, 2017',
#         'name': 'Max',
#         'tweet': 'This is a sample text. This is a sample text.'
#     },
#     6: {
#         'date': 'October 1st, 2017',
#         'name': 'Max',
#         'tweet': 'This is a sample text. This is a sample text.'
#     },
#     7: {
#         'date': 'Sept. 31st, 2017',
#         'name': 'Kelly',
#         'tweet': 'This is a sample text. This is a sample text.'
#     }
# }

@app.route('/posts', methods=['GET', 'POST'])
@app.route('/posts/<username>', methods=['GET', 'POST'])
@login_required
def posts(username=''):

 # dictionary no longer required. Reference db for user info
    # people = {
    #     0: {
    #         'name': 'Max',
    #         'age': 26,
    #         'bio': 'Avid swimmer, cat lover, and I ride a bike everywhere.',
    #         'url': 'http://placehold.it/250x250'
    #     },
    #     1: {
    #         'name': 'Kelly',
    #         'age': 21,
    #         'bio': 'My name is Kelly, I work in Boston and love dogs <3.',
    #         'url': 'http://placehold.it/250x250'
    #     }
    # }

    form = PostForm()

    person = User.query.filter_by(username=username).first()

    # on form submission, add data to the posts dictionary then re-render page with new Data
    if form.validate_on_submit():
        # length = len(posts_dict)
        # posts_dict[length] = {
        #     'date': datetime.now().date(),
        #     'name': name,
        #     'tweet': form.post.data
        # }

        p = Post(user_id=current_user.id, tweet=form.post.data)
        db.session.add(p)
        db.session.commit()


    return render_template('posts.html', person=person, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # check if user doesn't exist, or password is incorrect
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect.')
            return redirect(url_for('login'))

        # if not, log them if __name__ == '__main__':
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        # create a new user instance to be stored into the datbase
        user = User(full_name=form.full_name.data, username=form.username.data, email=form.email.data, age=form.age.data, bio=form.bio.data)
        # set the password using the set_password method
        user.set_password(form.password.data)
        # use the db commands to add user to stage and commit to database
        db.session.add(user)
        db.session.commit()
        flash('Congrats, you are now a registerd user!')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
