"""empty message

Revision ID: 1899d2c9e60f
Revises: 59c0efd4e8a9
Create Date: 2024-01-19 20:01:40.244247

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1899d2c9e60f'
down_revision = '59c0efd4e8a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('nome', sa.String(length=50), nullable=False))
    op.drop_column('role', 'name')
    op.add_column('usuario', sa.Column('create_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('usuario', sa.Column('update_at', sa.DateTime(timezone=True), nullable=True))
    op.drop_column('usuario', 'data_criacao')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('data_criacao', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.drop_column('usuario', 'update_at')
    op.drop_column('usuario', 'create_at')
    op.add_column('role', sa.Column('name', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('role', 'nome')
    # ### end Alembic commands ###
