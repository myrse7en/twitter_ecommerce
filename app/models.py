# need the db instance
from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tweet = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.now().date())
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return 'Post {} by {}: {}'.format(self.id, self.name, self.tweet)
