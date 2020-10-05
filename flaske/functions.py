import functools
import json

from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaske.db import get_db

bp = Blueprint('query',__name__)

@bp.route('/list', methods=['GET'])
def getAll():
    dbf = get_db()
    query = dbf.execute(
        'select * from Article'
    ).fetchall()
    
    queryJ = json.dumps([dict(ix) for ix in query])

    return queryJ

@bp.route('/createA', methods=['POST'])
def create():