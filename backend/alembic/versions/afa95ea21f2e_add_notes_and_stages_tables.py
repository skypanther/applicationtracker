"""Add notes and stages tables

Revision ID: afa95ea21f2e
Revises: 3507d9ce8fcd
Create Date: 2025-11-09 09:37:07.735228

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "afa95ea21f2e"
down_revision = "3507d9ce8fcd"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "notes",
        sa.Column("notes_id", sa.Integer(), nullable=False),
        sa.Column("job_app_id", sa.Integer(), nullable=False),
        sa.Column("notes", sa.String(), nullable=False),
        sa.Column(
            "datestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("current_timestamp"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("notes_id"),
    )

    op.create_table(
        "stages",
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("is_deleted", sa.Boolean, default=False),
        sa.PrimaryKeyConstraint("stage_id"),
    )


def downgrade() -> None:
    op.drop_table("notes")
    op.drop_table("stages")
