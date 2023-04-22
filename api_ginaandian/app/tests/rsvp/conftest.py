import pytest
from sqlmodel import Session

from api.orm.factories import RSVPFactory, GuestFactory


@pytest.fixture()
def rsvp_fixture(session: Session):

    RSVPFactory._meta.sqlalchemy_session = session
    GuestFactory._meta.sqlalchemy_session = session
    for id in range(1, 3):
        GuestFactory(id=id)
        RSVPFactory(id=id, guest_id=id)
    session.commit()


@pytest.fixture()
def guest_fixture(session: Session):
    GuestFactory._meta.sqlalchemy_session = session
    GuestFactory(id=1, name="Gina Rogari", has_plus_one=True)
    GuestFactory(id=2, name="Ian Myjer", has_plus_one=True)
    session.commit()
