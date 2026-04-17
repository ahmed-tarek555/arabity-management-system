from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://arabblbo_arabity_db:JFd7ZxtB_oNQ@localhost:5432/arabblbo_arabity_db"
# DATABASE_URL=  "postgresql://postgres:admin@db:5432/arabity_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
