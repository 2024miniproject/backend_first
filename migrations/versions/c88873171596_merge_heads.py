# c88873171596_merge_heads.py 예시
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c88873171596'
down_revision = ('0946b0393c26', '2059c3e2149c')  # 두 개의 헤드 명시
branch_labels = None
depends_on = None

def upgrade():
        op.create_table(
            'posts',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('title', sa.String(length=200), nullable=False),
            sa.Column('content', sa.Text(), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )

def downgrade():
    pass  # 필요한 다운그레이드 코드를 여기에 추가

