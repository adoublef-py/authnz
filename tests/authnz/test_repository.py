from pytest import fixture
from sqlmodel import SQLModel, Session, create_engine
from testcontainers.postgres import PostgresContainer

@fixture(scope="session")
def authnz_repo():
    with PostgresContainer() as postgres:
        engine = create_engine(postgres.get_connection_url())

        SQLModel.metadata.create_all(engine)

        with Session(engine) as session:
            yield session # yield PostgresRepository(session)