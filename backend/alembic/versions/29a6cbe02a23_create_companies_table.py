"""create companies table

Revision ID: 29a6cbe02a23
Revises:
Create Date: 2025-11-07 17:34:18.019568

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "29a6cbe02a23"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "companies",
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("website", sa.String(), nullable=True),
        sa.Column("recruiter_name", sa.String(), nullable=True),
        sa.Column("recruiter_email", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("current_timestamp"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("current_timestamp"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("company_id"),
    )


def downgrade() -> None:
    pass
