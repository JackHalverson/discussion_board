"""create discussions

Revision ID: 56abd8c9956c
Revises: 
Create Date: 2024-04-26 10:15:59.738733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56abd8c9956c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create Users table
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('name', sa.String, nullable=False)
    )

    # Create Group table
    op.create_table(
        'group',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('date_posted', sa.DateTime, nullable=False),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    )

    # Create Topics table
    op.create_table(
        'topic',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('date_posted', sa.DateTime, nullable=False),
        sa.Column('group_id', sa.Integer, sa.ForeignKey('group.id'), nullable=False),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    )

    # Create Comments table
    op.create_table(
        'comment',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('content', sa.String, nullable=False),
        sa.Column('date_posted', sa.DateTime, nullable=False),
        sa.Column('topic_id', sa.Integer, sa.ForeignKey('topic.id'), nullable=False),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    )


# Define the downgrade function (optional)
def downgrade():
    op.drop_table('comment')
    op.drop_table('topic')
    op.drop_table('group')
    op.drop_table('user')