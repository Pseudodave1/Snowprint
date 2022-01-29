"""empty message

Revision ID: 4e74f94ad765
Revises: 7f734eb26bc4
Create Date: 2022-01-28 08:43:53.718659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e74f94ad765'
down_revision = '7f734eb26bc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alignment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('query_id', sa.String(length=16), nullable=True),
    sa.Column('homologs', sa.Text(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_alignment_query_id'), 'alignment', ['query_id'], unique=True)
    op.create_table('operator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_seqs', sa.Integer(), nullable=True),
    sa.Column('consensus_score', sa.Float(precision=128), nullable=True),
    sa.Column('validated', sa.Boolean(), nullable=True),
    sa.Column('motif', sa.Text(length=4096), nullable=True),
    sa.Column('aligned_seqs', sa.Text(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('operon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('operon_seq', sa.String(length=4096), nullable=True),
    sa.Column('operon', sa.Text(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('regulator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prot_id', sa.String(length=16), nullable=True),
    sa.Column('genome_id', sa.String(length=16), nullable=True),
    sa.Column('organism_id', sa.Integer(), nullable=True),
    sa.Column('operator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['operator_id'], ['operator.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_regulator_prot_id'), 'regulator', ['prot_id'], unique=True)
    op.create_table('association',
    sa.Column('regulator_id', sa.Integer(), nullable=False),
    sa.Column('operon_id', sa.Integer(), nullable=False),
    sa.Column('reg_index', sa.Integer(), nullable=True),
    sa.Column('reg_type', sa.Integer(), nullable=True),
    sa.Column('regulated_seq', sa.String(length=4096), nullable=True),
    sa.ForeignKeyConstraint(['operon_id'], ['operon.id'], ),
    sa.ForeignKeyConstraint(['regulator_id'], ['regulator.id'], ),
    sa.PrimaryKeyConstraint('regulator_id', 'operon_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_index(op.f('ix_regulator_prot_id'), table_name='regulator')
    op.drop_table('regulator')
    op.drop_table('operon')
    op.drop_table('operator')
    op.drop_index(op.f('ix_alignment_query_id'), table_name='alignment')
    op.drop_table('alignment')
    # ### end Alembic commands ###
