"""empty message

Revision ID: 5f32d50b3320
Revises: 16b38413ba51
Create Date: 2024-01-13 18:13:13.076792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f32d50b3320'
down_revision = '16b38413ba51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('data_update', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'data_update')
    # ### end Alembic commands ###