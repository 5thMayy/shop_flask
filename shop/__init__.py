from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from werkzeug.datastructures import  FileStorage
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
# from werkzeug.utils import secure_filename



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY']='jfjfjjs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
app.config["MAX_CONTENT_LENGTH"] = 24 * 1024 * 1024




db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from shop.admin import routes
from shop.products import routes