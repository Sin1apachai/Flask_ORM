"""empty message

Revision ID: 88f29fcd891d
Revises: bf76e2058b9f
Create Date: 2020-07-01 23:45:18.368083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88f29fcd891d'
down_revision = 'bf76e2058b9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column(
        'phone', sa.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###
