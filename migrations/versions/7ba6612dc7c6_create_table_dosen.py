"""create table dosen

Revision ID: 7ba6612dc7c6
Revises: bb69b1f508ab
Create Date: 2024-03-24 22:51:41.148671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ba6612dc7c6'
down_revision = 'bb69b1f508ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nidn', sa.String(length=30), nullable=False),
    sa.Column('nama', sa.String(length=250), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('alamat', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('dosen', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_dosen_nidn'), ['nidn'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dosen', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_dosen_nidn'))

    op.drop_table('dosen')
    # ### end Alembic commands ###
