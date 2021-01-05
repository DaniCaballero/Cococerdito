from flask import (
    Blueprint,flash,g,redirect,render_template,request,url_for
)

from werkzeug.exceptions import abort
from coco.auth import login_required
from coco.db import get_db

bp = Blueprint('routes',__name__)

@bp.route('/')
def home():
    return render_template('routes/home.html')