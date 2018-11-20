# import necessary fucntions and classes
from app import app
from flask import render_template, url_for, redirect



# create page routes
@app.route('/')
@app.route('/index')
def index():
    products = {
        101: {
            "id": 101,
            "title": "Soap",
            "price": 4.95,
            "url": "http://placehold.it/250x250",
            "desc": "This bar of soap is a bar of soapy soap."
        },
        102: {
            "id": 102,
            "title": "Grapes",
            "price": 3.85,
            "url": "http://placehold.it/250x250",
            "desc": "These grapes are abundle of grapey grapes."
        },
        103: {
            "id": 103,
            "title": "Oranges",
            "price": 67.85,
            "url": "http://placehold.it/250x250",
            "desc": "This box is a box of orangey oranges."
        },
        104: {
            "id": 104,
            "title": "Oranges",
            "price": 67.85,
            "url": "http://placehold.it/250x250",
            "desc": "This box is a box of orangey oranges."
        },
        105: {
            "id": 105,
            "title": "Oranges",
            "price": 67.85,
            "url": "http://placehold.it/250x250",
            "desc": "This box is a box of orangey oranges."
        }
    }


    return render_template('index.html', products=products)

@app.route('/posts')
@app.route('/posts/<name>')
def posts(name='Max'):
    posts_dict = {
        0: {
            'date': 'Sept. 9th, 2018',
            'name': 'Max',
            'tweet': 'Today I had cereal for breakfast.'
        },
        1: {
            'date': 'July 1st, 2018',
            'name': 'Kelly',
            'tweet': 'Went for a run downtown.'
        },
        2: {
            'date': 'June 21st, 2018',
            'name': 'Max',
            'tweet': 'Got a new job!! Working for the man.'
        },
        3: {
            'date': 'March 4th, 2018',
            'name': 'Kelly',
            'tweet': 'Hiking is fun, get outside.'
        },
        4: {
            'date': 'February 8th, 2018',
            'name': 'Kelly',
            'tweet': 'This is a sample text. This is a sample text.'
        },
        5: {
            'date': 'October 10th, 2017',
            'name': 'Max',
            'tweet': 'This is a sample text. This is a sample text.'
        },
        6: {
            'date': 'October 1st, 2017',
            'name': 'Max',
            'tweet': 'This is a sample text. This is a sample text.'
        },
        7: {
            'date': 'Sept. 31st, 2017',
            'name': 'Kelly',
            'tweet': 'This is a sample text. This is a sample text.'
        }
    }
    people = {
        0: {
            'name': 'Max',
            'age': 26,
            'bio': 'Avid swimmer, cat lover, and I ride a bike everywhere.',
            'url': 'http://placehold.it/250x250'
        },
        1: {
            'name': 'Kelly',
            'age': 21,
            'bio': 'My name is Kelly, I work in Boston and love dogs <3.',
            'url': 'http://placehold.it/250x250'
        }
    }
    return render_template('posts.html', posts=posts_dict, people=people, name=name)
