from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# To Do :
# replace the secret key
app.config['SECRET_KEY'] = '9c47844038dd8fe3543a9c0b080e8572'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from your_blogs import routes