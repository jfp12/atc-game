"""Create airports table

Revision ID: c53d4756cadf
Revises:
Create Date: 2023-04-19 19:58:04.879531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c53d4756cadf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "airports",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("code", sa.String(3), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("airports")
