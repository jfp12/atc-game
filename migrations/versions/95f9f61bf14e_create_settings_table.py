"""Create settings table

Revision ID: 95f9f61bf14e
Revises: c53d4756cadf
Create Date: 2023-04-19 19:48:33.173626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95f9f61bf14e'
down_revision = 'c53d4756cadf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "parameters",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("name", sa.String(64), nullable=False, unique=True),
        sa.Column("value", sa.String(64), nullable=False)
    )


def downgrade():
    op.drop_table("parameters")
