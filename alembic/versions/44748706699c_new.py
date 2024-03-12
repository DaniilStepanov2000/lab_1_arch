"""new

Revision ID: 44748706699c
Revises: ac394290322b
Create Date: 2024-03-05 18:45:00.721877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44748706699c'
down_revision: Union[str, None] = 'ac394290322b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "patients_new",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String, nullable=False, primary_key=True),
        sa.Column("last_name", sa.String, nullable=False, primary_key=True),
        sa.Column("age", sa.Integer, nullable=False, primary_key=True),
        sa.Column("hospital_id", sa.Integer, nullable=False),
    )
    op.create_foreign_key(
        constraint_name="fk_patients",
        source_table="patients_new",
        referent_table="hospital",
        local_cols=["hospital_id"],
        remote_cols=["id"],
        ondelete="cascade",
    )


def downgrade() -> None:
    op.drop_table("patients_new")
