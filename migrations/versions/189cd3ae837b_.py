"""empty message

Revision ID: 189cd3ae837b
Revises: 6e5e99e76436
Create Date: 2024-09-21 10:40:26.713656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '189cd3ae837b'
down_revision = '6e5e99e76436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_auth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users_auth', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_auth_email'), ['email'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_auth_username'), ['username'], unique=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_userid')
        batch_op.drop_column('userid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userid', sa.VARCHAR(), nullable=True))
        batch_op.create_index('ix_users_userid', ['userid'], unique=False)

    with op.batch_alter_table('users_auth', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_auth_username'))
        batch_op.drop_index(batch_op.f('ix_users_auth_email'))

    op.drop_table('users_auth')
    # ### end Alembic commands ###
