"""empty message

Revision ID: 8d1c36f444c3
Revises: None
Create Date: 2016-10-30 12:26:33.738491

"""

# revision identifiers, used by Alembic.
revision = '8d1c36f444c3'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('result_all', postgresql.JSON, nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON, nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    ### end Alembic commands ###
