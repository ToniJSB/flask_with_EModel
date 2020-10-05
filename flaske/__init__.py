import os

from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_cors import CORS, cross_origin

from . import db
from . import functions


app = Flask(__name__,instance_relative_config=True)
CORS(app)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path,'flaske.sqllite'),
    CORS_HEADERS= 'application/json'
)

try: 
    os.makedirs(app.instance_path)
except OSError:
    pass
db.init_app(app)

@app.route('/home',methods=['GET'])
def listArticles():
    return render_template('templates/base.html')

app.register_blueprint(functions.bp)



