from flask import Flask
from flask_wtf.csrf import CSRFProtect

from . import config
from .models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
app.secret_key = 'iyzTwzU8LMmHCVyb_L515CXZAaRtx8il'
app.permanent_session_lifetime = 300
csrf = CSRFProtect(app)
db.init_app(app)
# db.drop_all()
db.create_all()

from app import views