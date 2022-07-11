from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # TODO
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    #connect_args={"check_same_thread": False}  # TODO remove with sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
