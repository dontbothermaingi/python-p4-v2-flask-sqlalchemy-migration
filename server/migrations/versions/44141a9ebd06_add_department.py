"""add Department

Revision ID: 44141a9ebd06
Revises: e9969a5dba93
Create Date: 2024-04-03 05:47:22.312964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44141a9ebd06'
down_revision = 'e9969a5dba93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
