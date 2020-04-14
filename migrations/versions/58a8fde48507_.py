"""empty message

Revision ID: 58a8fde48507
Revises: 
Create Date: 2020-04-11 22:38:15.863743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58a8fde48507'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=20), nullable=False),
    sa.Column('lastname', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('location', sa.String(length=30), nullable=True),
    sa.Column('biography', sa.String(length=200), nullable=True),
    sa.Column('profile_picture', sa.String(length=20), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
