from flask import Blueprint, render_template

bp = Blueprint('front', __name__, url_prefix='/')

@bp.route('/home')  # 원하는 URL 경로에 따라 수정 가능
def home():
    return render_template('front/home.html')  # 템플릿 파일 경로
