#flask webapp https://exploreflask.com/en/latest/index.html
from flask import Flask, session, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

import sys
import re
from datetime import datetime
from datetime import timedelta #so that we can log last time user interacted with the server for session timeout

#flask_wtf to help with form managemenmt and security https://exploreflask.com/en/latest/forms.html
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
#Database relationships https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
from sqlalchemy.orm import declarative_base, relationship

#usage
#from models import user, tool, accessory

app = Flask(__name__, template_folder='templates')
app.config.update(TESTING=True, TEMPLATES_AUTO_RELOAD=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['EXPLAIN_TEMPLATE_LOADING'] = False
app.secret_key = '1!df56dn;' #can be anything
#sessions data
app.permanent_session_lifetime = timedelta(hours=2)
#session.permanent=True #call this fater session dictionary is instantiated
db = SQLAlchemy(app)
db.app = app
#######
#this adds the variable db (containing our whole SQLAlchemy database) to the config dictonary with key 'database', for easy access in blueprints
app.config['database'] = db
#######

#the with app.app_context() must be used to register the blueprints, for the blueprints to successfully utilize the database
with app.app_context():
    ######blueprint importation ##This has to occur after db setup or else runtime error (since the db will not be setup at import time)
    from blueprints.admin.admin_bp import admin_p
    from blueprints.admin.admin_test_bp import admin_test
    from blueprints.signin.signin_up import sign_in_bp
    from blueprints.hello_world.helloworld import hw_bp
    ############## Blueprint registration
    app.register_blueprint(admin_p)
    app.register_blueprint(admin_test)

    app.register_blueprint(sign_in_bp)

    #Hello world blueprint should be the easiest for you to copy
    app.register_blueprint(hw_bp)
    ##############
################################


#If you don't have this, in some cases your database will not initialize
#AFAIK it will never reset your database, only create a new one if one doesn't exist
@app.before_first_request
def create_tables():
    db.create_all()

########### send user to sign up or to garage if token is fresh
@app.route("/", methods=['GET', 'POST'])
def home():
    valid_sign_in = True
    if (valid_sign_in):
        return redirect('/sign-in')
    else:
        return redirect('/hello')
###########


########### helper/expansion features
#help using the site
@app.route("/help/", methods=['GET'])
def help():
    return render_template('help.html', title="Help")

#manage user settings
@app.route("/user_settings/", methods=['GET','POST'])
def user_settings():
    pass

###########

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
