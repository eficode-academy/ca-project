from app import db
# models.py
# 
# Used to model our datastore
# We are not using the user model
# The post model is used to handle the posts any one can make
# This model allows us to only care about how the object looks, 
# and not care about how it is serialized

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_name = db.Column(db.String(40))
    title = db.Column(db.String(50))

    def __repr__(self):
        return '<Post %r>' % (self.body)
