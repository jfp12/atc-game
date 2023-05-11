"""Create runways table

Revision ID: 3c926f3fe639
Revises: ad81f943aa86
Create Date: 2023-04-19 19:57:35.102022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c926f3fe639'
down_revision = 'ad81f943aa86'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "runways",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("airport_id", sa.Integer, sa.ForeignKey("airports.id"), nullable=False),
        sa.Column("active", sa.Boolean, nullable=False)
    )


def downgrade():
    op.drop_table("runways")
