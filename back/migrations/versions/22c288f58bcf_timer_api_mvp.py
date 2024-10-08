"""Timer API MVP

Revision ID: 22c288f58bcf
Revises: 
Create Date: 2024-10-04 15:37:24.392820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '22c288f58bcf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maps',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('start_zone', sa.String(), nullable=False),
        sa.Column('end_zone', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('unique_id', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('times',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('time', sa.Float(), nullable=False),
        sa.Column('max_speed', sa.Float(), nullable=False),
        sa.Column('average_speed', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('map_id', sa.Integer(), nullable=False),
        sa.Column('player_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['map_id'], ['maps.id'], ),
        sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('times')
    op.drop_table('players')
    op.drop_table('maps')
    # ### end Alembic commands ###
