"""Initial Migration

Revision ID: ef3690d113b3
Revises: 6f6775242f8d
Create Date: 2019-08-13 09:27:59.776101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef3690d113b3'
down_revision = '6f6775242f8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')
    # ### end Alembic commands ###
