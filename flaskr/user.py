from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

import json

from flaskr.auth import login_required
# from flaskr.db import get_db

bp = Blueprint('user', __name__, url_prefix='/users')

@bp.route('/')
def index():
    users = [
        {
            "id": 1,
            "name": "name1",
            "password": "password1",
        },
        {
            "id": 2,
            "name": "name2",
            "password": "password2",
        },
    ]
    users = json.dumps(users)
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('user/index.html', users=users)