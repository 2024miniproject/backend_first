# write_views.py
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from pybo.models import Post, db
import os

bp = Blueprint('write_views', __name__)

@bp.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        content = request.form['content']

        # 파일 업로드 처리
        files = request.files.getlist('files')
        filenames = []
        for file in files:
            if file:
                filename = file.filename
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                filenames.append(filename)

        # DB 작업을 위한 애플리케이션 컨텍스트 활성화
        try:
            with current_app.app_context():
                new_post = Post(title=title, price=price, content=content, filename=', '.join(filenames))
                db.session.add(new_post)
                db.session.commit()
        except Exception as e:
            # 오류 처리
            db.session.rollback()  # 롤백
            return f"오류가 발생했습니다: {str(e)}", 500

        # JavaScript로 알림을 보여주고 다시 write 페이지로 리다이렉트
        return '''
        <script>
            alert("등록이 완료되었습니다.");
            window.location.href = "{url}";
        </script>
        '''.format(url=url_for('write_views.write'))  # url_for 사용

    return render_template('front/write.html')
