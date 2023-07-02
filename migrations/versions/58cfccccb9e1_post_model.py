"""Post model

Revision ID: 58cfccccb9e1
Revises: 
Create Date: 2023-07-02 23:33:14.629262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58cfccccb9e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('microblog_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.VARCHAR(length=350), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microblog_posts_id'), 'microblog_posts', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_microblog_posts_id'), table_name='microblog_posts')
    op.drop_table('microblog_posts')
    # ### end Alembic commands ###
