import pytest
from sqlmodel import Session

from api.orm.factories import RSVPFactory


@pytest.fixture()
def rsvp_fixture(session: Session):

    RSVPFactory._meta.sqlalchemy_session = session
    RSVPFactory.create_batch(200)
    session.commit()
