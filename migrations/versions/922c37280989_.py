"""empty message

Revision ID: 922c37280989
Revises: 60cdc9962627
Create Date: 2024-11-14 17:11:05.806084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '922c37280989'
down_revision = '60cdc9962627'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DATETIME(), nullable=True))

    op.drop_table('boards')
    # ### end Alembic commands ###
