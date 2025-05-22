from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "postgresql+psycopg2://postgres:password@postgres:5432/mm_db"

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()