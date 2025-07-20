import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
from typing import Generator

# ✅ 1. Load environment variables from .env if present
load_dotenv()

# ✅ 2. Get DATABASE_URL from environment
# Fallback is optional and can be changed or removed in production
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://paulregnier:abc123@localhost:5432/ethosdb"
)

# ✅ 3. Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True,     # Log SQL queries for development; turn off in prod
    future=True    # Use SQLAlchemy 2.0 style
)

# ✅ 4. Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ 5. Declarative Base for models
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

