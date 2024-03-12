"""add entityes

Revision ID: a633d5eb37d5
Revises: c45777d436f1
Create Date: 2024-03-05 00:39:52.933902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a633d5eb37d5'
down_revision: Union[str, None] = 'c45777d436f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logistic_company_many_to_many',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.Column('logistic_company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['logistic_company_id'], ['logistic_company_new.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_logistic_company_many_to_many_hospital_id'), 'logistic_company_many_to_many', ['hospital_id'], unique=False)
    op.create_index(op.f('ix_logistic_company_many_to_many_logistic_company_id'), 'logistic_company_many_to_many', ['logistic_company_id'], unique=False)
    op.drop_index('ix_logistic_company_hospital_id', table_name='logistic_company')
    op.drop_index('ix_logistic_company_logistic_company_id', table_name='logistic_company')
    op.drop_table('logistic_company')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logistic_company',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('hospital_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('logistic_company_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.id'], name='logistic_company_hospital_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['logistic_company_id'], ['logistic_company_new.id'], name='logistic_company_logistic_company_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='logistic_company_pkey')
    )
    op.create_index('ix_logistic_company_logistic_company_id', 'logistic_company', ['logistic_company_id'], unique=False)
    op.create_index('ix_logistic_company_hospital_id', 'logistic_company', ['hospital_id'], unique=False)
    op.drop_index(op.f('ix_logistic_company_many_to_many_logistic_company_id'), table_name='logistic_company_many_to_many')
    op.drop_index(op.f('ix_logistic_company_many_to_many_hospital_id'), table_name='logistic_company_many_to_many')
    op.drop_table('logistic_company_many_to_many')
    # ### end Alembic commands ###