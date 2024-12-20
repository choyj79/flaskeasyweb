"""empty message

Revision ID: 5c931be99590
Revises: c29fd8c0793c
Create Date: 2024-11-07 16:55:52.756666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c931be99590'
down_revision = 'c29fd8c0793c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('views', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('content',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.create_index(batch_op.f('ix_board_updated_at'), ['updated_at'], unique=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['author_id'], ['id'])
        batch_op.drop_column('user_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_name', sa.VARCHAR(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_name'], ['id'])
        batch_op.drop_index(batch_op.f('ix_board_updated_at'))
        batch_op.alter_column('content',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('updated_at')
        batch_op.drop_column('views')
        batch_op.drop_column('author_id')

    # ### end Alembic commands ###
