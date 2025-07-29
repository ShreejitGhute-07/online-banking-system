from flask import Flask
from flask_cors import CORS
from models import db

app=Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "Online Banking System Flask API"

if __name__=='__main__':
    app.run(debug=True)