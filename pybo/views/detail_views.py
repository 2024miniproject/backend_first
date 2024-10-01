from flask import Blueprint, render_template

bp = Blueprint('detail', __name__, url_prefix='/')

@bp.route('/detail')  # 원하는 URL 경로에 따라 수정 가능
def detail():
    return render_template('front/detail.html')  # 템플릿 파일 경로
