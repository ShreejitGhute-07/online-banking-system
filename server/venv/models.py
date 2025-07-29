from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    full_name=db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))

class Account(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    user_id=db.Column(db.Integer,db.foreign_key('user_id'))
    account_type = db.Column(db.String(50))  # for the savings and the checking thing.....
    balance = db.Column(db.Float,default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    account_id=db.Column(db.Integer,db.foreign_key('account_id'))
    type = db.Column(db.String(50)) # for the deposit, withdraw and the transfer
    amount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

