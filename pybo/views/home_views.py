from flask import Blueprint, render_template
from pybo.models import Post  # Post 모델을 import합니다.

bp = Blueprint('home_views', __name__, url_prefix='/')

@bp.route('/home')  # 원하는 URL 경로에 따라 수정 가능
def home():
    posts = Post.query.all()  # 데이터베이스에서 모든 게시글 조회
    return render_template('front/home.html', posts=posts)  # 템플릿 파일 경로
