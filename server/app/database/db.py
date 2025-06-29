from sqlmodel import create_engine, Session, SQLModel
from app.config.conf import DATABASE_URL

engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
