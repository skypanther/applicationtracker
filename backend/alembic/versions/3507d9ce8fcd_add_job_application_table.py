"""Add job_application table

Revision ID: 3507d9ce8fcd
Revises: 29a6cbe02a23
Create Date: 2025-11-08 18:08:56.321406

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3507d9ce8fcd"
down_revision = "29a6cbe02a23"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "job_applications",
        sa.Column("job_app_id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("job_title", sa.String(), nullable=False),
        sa.Column("source", sa.String(), nullable=True),
        sa.Column("source_url", sa.String(), nullable=True),
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column(
            "application_datetime",
            sa.DateTime(timezone=True),
            server_default=sa.text("current_timestamp"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("job_app_id"),
    )


def downgrade() -> None:
    op.drop_table("job_applications")
