"""empty message

Revision ID: 8a8e177c22c8
Revises: eef69a932db1
Create Date: 2019-12-15 18:02:16.218540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a8e177c22c8'
down_revision = 'eef69a932db1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'key'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('key')
    )
    op.create_unique_constraint(None, 'clients', ['id'])
    op.create_unique_constraint(None, 'tickets', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tickets', type_='unique')
    op.drop_constraint(None, 'clients', type_='unique')
    op.drop_table('settings')
    # ### end Alembic commands ###
