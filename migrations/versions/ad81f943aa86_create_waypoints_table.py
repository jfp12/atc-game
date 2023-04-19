"""Create waypoints table

Revision ID: ad81f943aa86
Revises: 3d9bdeb9b16d
Create Date: 2023-04-19 19:54:37.221682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad81f943aa86'
down_revision = '3d9bdeb9b16d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "waypoints",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("name", sa.String(15), nullable=False),
        sa.Column("airport_id", sa.Integer, sa.ForeignKey("airports.id"), nullable=False),
        sa.Column("x", sa.Float, nullable=False),
        sa.Column("y", sa.Float, nullable=False),
        sa.Column("type", sa.String(15), nullable=False),
        sa.Column("exit_waypoint", sa.Boolean, nullable=False)
    )


def downgrade():
    op.drop_table("waypoints")
