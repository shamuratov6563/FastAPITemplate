# db/session_manager.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextvars import ContextVar

# Har bir tenant uchun alohida engine (real loyihada dinamika qilish kerak bo'ladi)
DATABASES = {
    "default": "postgresql://user:pass@localhost/default_db",
    "tenant1": "postgresql://user:pass@localhost/tenant1_db",
    "tenant2": "postgresql://user:pass@localhost/tenant2_db",
}

_session_context = ContextVar("session")

def get_engine(tenant: str):
    db_url = DATABASES.get(tenant)
    if not db_url:
        raise Exception(f"No DB config found for tenant {tenant}")
    return create_engine(db_url)

def get_session(tenant: str):
    engine = get_engine(tenant)
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return SessionLocal()
