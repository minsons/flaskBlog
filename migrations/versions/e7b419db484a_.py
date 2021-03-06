"""empty message

Revision ID: e7b419db484a
Revises: 
Create Date: 2017-12-27 15:05:45.330735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7b419db484a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('img', sa.String(length=256), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('desc', sa.String(length=64), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_name', sa.String(length=64), nullable=True),
    sa.Column('author_email', sa.String(length=64), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('comment_type', sa.String(length=64), nullable=True),
    sa.Column('reply_to', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('orders', sa.Integer(), nullable=True),
    sa.Column('link', sa.String(length=128), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['menu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('menu')
    op.drop_table('comments')
    op.drop_table('category')
    op.drop_table('article')
    # ### end Alembic commands ###
