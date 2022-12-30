from flask import Blueprint, render_template, abort, url_for, request, flash, current_app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from util.my_utilities import Unique
from datetime import datetime
from models import user, tool, accessory

#current app is an import from flask (in this file, its at the end of line 1)
app = current_app

#To retreive the database, app.app_context() must be used
with app.app_context():
    #bring in the database as a variable in this blueprint
    db = current_app.config['database']
    #register this blueprint.  The name of this variable is what we import webapp.py for instance: from blueprints.signin.signin_up import sign_in_bp
    hw_bp = Blueprint('helloworld', __name__, template_folder='templates/hello_world', static_folder='static')

########### Sign in and sign up routes
@hw_bp.route("/hello/", methods=["GET", "POST"])
def hello_fxn():
    return render_template('hello_world_html.html')
