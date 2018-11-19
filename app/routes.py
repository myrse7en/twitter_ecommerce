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
