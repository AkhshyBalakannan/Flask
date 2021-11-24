"""remove email column

Revision ID: 9f8da5f192eb
Revises: 3ff76f95743c
Create Date: 2021-11-24 18:35:20.519537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f8da5f192eb'
down_revision = '3ff76f95743c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###