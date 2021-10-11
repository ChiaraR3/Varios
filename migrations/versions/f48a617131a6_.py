"""empty message

Revision ID: f48a617131a6
Revises: 6167b7d0aaaf
Create Date: 2021-10-11 18:52:15.488698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f48a617131a6'
down_revision = '6167b7d0aaaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('gender', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'client', ['gender'])
    op.create_unique_constraint(None, 'client', ['room'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'client', type_='unique')
    op.drop_constraint(None, 'client', type_='unique')
    op.drop_column('client', 'gender')
    # ### end Alembic commands ###
