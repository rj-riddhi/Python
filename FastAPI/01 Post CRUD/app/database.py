from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Loads the env file
load_dotenv()

# Get the database url env from .env file
database_url = os.getenv("DATABASE_URL")

# create postgresql engine 
engine = create_engine(database_url)

# Set the session with db
SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

# To make model as object of db
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
