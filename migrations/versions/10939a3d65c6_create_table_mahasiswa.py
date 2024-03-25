"""create table mahasiswa

Revision ID: 10939a3d65c6
Revises: 7ba6612dc7c6
Create Date: 2024-03-24 22:56:24.241424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10939a3d65c6'
down_revision = '7ba6612dc7c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mahasiswa',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nim', sa.String(length=30), nullable=False),
    sa.Column('nama', sa.String(length=250), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('alamat', sa.String(length=250), nullable=False),
    sa.Column('dosen_satu', sa.BigInteger(), nullable=True),
    sa.Column('dosen_dua', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['dosen_dua'], ['dosen.id'], ),
    sa.ForeignKeyConstraint(['dosen_satu'], ['dosen.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_mahasiswa_nim'), ['nim'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mahasiswa_nim'))

    op.drop_table('mahasiswa')
    # ### end Alembic commands ###