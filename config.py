import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

# 이미지 업로드 설정
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')  # 'uploads' 폴더 경로
