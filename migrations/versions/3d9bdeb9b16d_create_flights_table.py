"""Create flights table

Revision ID: 3d9bdeb9b16d
Revises: 95f9f61bf14e
Create Date: 2023-04-19 19:51:28.344719

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '3d9bdeb9b16d'
down_revision = '95f9f61bf14e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "flights",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("airport_id", sa.Integer, sa.ForeignKey("airports.id"), nullable=False),
        sa.Column("flight_no", sa.String(10), nullable=False),
        sa.Column("bound", sa.Enum("a", "d", name="operation_type"), nullable=False),
        sa.Column("aircraft_type", sa.String(10), nullable=False),
        sa.Column("aircraft_name", sa.String(100), nullable=False),
        sa.Column("other_airport", sa.String(4), nullable=False),
        sa.Column("other_airport_name", sa.String(100), nullable=False),
        sa.UniqueConstraint('airport_id', 'flight_no', name='unique_flight')
    )


def downgrade():
    op.drop_table("flights")

    operation_type = postgresql.ENUM("a", "d", name="operation_type")
    operation_type.drop(op.get_bind())
