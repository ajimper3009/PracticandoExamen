import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Forzar uso de SQLite si estamos corriendo pytest
if "pytest" in os.getenv("_", "") or os.getenv("TESTING") == "True":
    DATABASE_URL = "sqlite:///test.db"
    connect_args = {"check_same_thread": False}
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@db:3306/fastapi_db")
    connect_args = {}

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
