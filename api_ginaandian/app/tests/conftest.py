import os
import pathlib

import factory.random
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine
from sqlmodel.pool import StaticPool

from alembic import command
from alembic.config import Config


@pytest.fixture(autouse=True)
def factory_seed():
    """Ensure factoryboy/Faker generate the same values each time"""
    factory.random.reseed_random(42)


@pytest.fixture(name="engine")
def engine_fixture():
    return create_engine(
        f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
        f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}"
        f"/{os.environ['POSTGRES_DB']}",
        poolclass=StaticPool,
    )


@pytest.fixture(name="session")
def session_fixture(engine):
    alembic_cfg = Config(
        file_=pathlib.Path(__file__).parents[1].joinpath("alembic.ini")
    )

    # build up real database the way alembic would build it
    with engine.begin() as conn:
        alembic_cfg.attributes["connection"] = conn
        command.upgrade(alembic_cfg, "head")

    with Session(engine) as session:
        yield session

    # tear down db
    with engine.begin() as conn:
        alembic_cfg.attributes["connection"] = conn
        command.downgrade(alembic_cfg, "base")


@pytest.fixture(name="client")
def client_fixture(session: Session):
    from api.db import get_session
    from api.api import app

    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
