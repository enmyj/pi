"""BASE

Revision ID: 4fc5b798f5b7
Revises: 
Create Date: 2023-04-20 21:54:19.855966

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "4fc5b798f5b7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "guest",
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("has_plus_one", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "rsvp",
        sa.Column("guest_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("plus_one_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("attending", sa.Boolean(), nullable=False),
        sa.Column(
            "shuttle_or_driving", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "shuttle_lodging_location",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=True,
        ),
        sa.Column("driving_num_seats", sa.Integer(), nullable=True),
        sa.Column(
            "dietary_restrictions", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "mobility_restrictions", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("num_children", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("guest_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["guest_id"],
            ["guest.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("guest_name"),
    )
    op.execute("insert into guest (name, has_plus_one) values ('Ian Myjer', true)")
    op.execute("insert into guest (name, has_plus_one) values ('Gina Rogari', true)")
    op.execute("insert into guest (name, has_plus_one) values ('Serena Myjer', false)")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("rsvp")
    op.drop_table("guest")
    # ### end Alembic commands ###