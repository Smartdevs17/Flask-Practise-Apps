"""empty message

Revision ID: 5d2048796efa
Revises: 
Create Date: 2022-08-17 08:35:34.949367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d2048796efa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###

    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    
    op.alter_column("todos", "completed", nullable=False)

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
