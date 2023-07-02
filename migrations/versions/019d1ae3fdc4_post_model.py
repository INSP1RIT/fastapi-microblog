"""Post model

Revision ID: 019d1ae3fdc4
Revises: 58cfccccb9e1
Create Date: 2023-07-02 23:43:03.433255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019d1ae3fdc4'
down_revision = '58cfccccb9e1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('email', sa.VARCHAR(length=50), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.add_column('microblog_posts', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('microblog_posts', sa.Column('user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'microblog_posts', 'user', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'microblog_posts', type_='foreignkey')
    op.drop_column('microblog_posts', 'user')
    op.drop_column('microblog_posts', 'date')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
