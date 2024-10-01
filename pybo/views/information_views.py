from flask import Blueprint, render_template

bp = Blueprint('information', __name__, url_prefix='/information')

@bp.route('/')
def information():
    return render_template('information/information.html')
