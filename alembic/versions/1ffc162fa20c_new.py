"""new

Revision ID: 1ffc162fa20c
Revises: 44748706699c
Create Date: 2024-03-05 18:53:57.097501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ffc162fa20c'
down_revision: Union[str, None] = '44748706699c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # op.create_table(
    #     "patients_new",
    #     sa.Column("id", sa.Integer, primary_key=True),
    #     sa.Column("first_name", sa.String, nullable=False, primary_key=True),
    #     sa.Column("last_name", sa.String, nullable=False, primary_key=True),
    #     sa.Column("age", sa.Integer, nullable=False, primary_key=True),
    #     sa.Column("hospital_id", sa.Integer, nullable=False),
    # )
    # op.create_foreign_key(
    #     constraint_name="fk_patients",
    #     source_table="patients_new",
    #     referent_table="hospital",
    #     local_cols=["hospital_id"],
    #     remote_cols=["id"],
    # )


def downgrade() -> None:
    pass
    # op.drop_table("patients_new")
