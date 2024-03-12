"""add entityes

Revision ID: ac394290322b
Revises: 038232a6baf8
Create Date: 2024-03-05 18:44:32.361529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac394290322b'
down_revision: Union[str, None] = '038232a6baf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
