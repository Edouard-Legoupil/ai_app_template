
#  Standard Library
import logging
import urllib.parse
import os

#  Third-Party Libraries
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pg8000.dbapi
import psycopg2

#  Internal Modules
from backend.core.config import db_host, db_name, db_username, db_password

# Configure logging
logger = logging.getLogger(__name__)

# --- Additional Config ---
cloud_provider = os.getenv("CLOUD_PROVIDER", "local").lower()  # gcp | azure | local

# <--- Start with None, lazy-load later
engine = None


def get_engine():
    """
    Lazily initializes and returns a SQLAlchemy engine.
    """
    global engine
    if engine is not None:
        return engine

    logger.info(f"Initializing SQLAlchemy engine... cloud_provider={cloud_provider}")

    if os.getenv("TESTING"):
        from unittest.mock import MagicMock
        logger.info("TESTING mode: using MagicMock engine")
        engine = MagicMock()
        return engine

    try:
        if cloud_provider == "gcp":
            # --- Cloud SQL Connector Initialization ---
            connector = None

            def get_connector() -> "Connector":
                """Initializes and returns a Cloud SQL Connector instance."""
                global connector
                if connector is None:
                    from google.cloud.sql.connector import Connector
                    connector = Connector()
                return connector

            logger.info(f"Creating GCP SQLAlchemy engine for {db_host}, db: {db_name}, user: {db_username}")
            engine = create_engine(
                "postgresql+pg8000://",
                creator=lambda: get_connector().connect(
                    db_host,
                    "pg8000",
                    user=db_username,
                    password=db_password,
                    db=db_name,
                ),
                pool_pre_ping=True,
                pool_recycle=300,
            )
            logger.info("GCP engine created successfully")

            # Test the connection immediately
            with engine.connect() as test_conn:
                result = test_conn.execute(text("SELECT CURRENT_TIMESTAMP"))
                logger.info(f"✅ GCP Database connection test passed: {result.scalar()}")

        elif cloud_provider == "azure":
            encoded_password = urllib.parse.quote_plus(db_password) if db_password else ""
            connection_string = (
                f"postgresql+psycopg2://{db_username}:{encoded_password}@{db_host}:5432/{db_name}?sslmode=require"
            )
            logger.info(f"Creating Azure engine for {db_host}")
            engine = create_engine(
                connection_string,
                pool_pre_ping=True,
                pool_recycle=300,
            )
            logger.info("Azure engine created successfully")

            # Test the connection immediately
            with engine.connect() as test_conn:
                result = test_conn.execute(text("SELECT CURRENT_TIMESTAMP"))
                logger.info(f"✅ Azure Database connection test passed: {result.scalar()}")

        else:  # local or default
            logger.info(f"Creating local engine for {db_host}")
            encoded_password = urllib.parse.quote_plus(db_password) if db_password else ""
            connection_string = (
                f"postgresql+psycopg2://{db_username}:{encoded_password}@{db_host}:5432/{db_name}"
            )
            engine = create_engine(
                connection_string,
                pool_pre_ping=True,
                pool_recycle=300,
            )

            # Test the connection immediately
            with engine.connect() as test_conn:
                result = test_conn.execute(text("SELECT CURRENT_TIMESTAMP"))
                logger.info(f"✅ Local Database connection test passed: {result.scalar()}")

    except Exception as e:
        logger.error(f"Failed to create engine for {cloud_provider}: {e}", exc_info=True)
        raise

    return engine





def test_connection():
    """
    Explicitly test database connectivity.
    """
    try:
        eng = get_engine()
        with eng.connect() as conn:
            from sqlalchemy import text
            result = conn.execute(text("SELECT CURRENT_TIMESTAMP as current_time, version() as db_version"))
            logger.info(f"✅ Database connection successful. Current time: {result.scalar()}")
            return True
    except Exception as e:
        logger.error(f"❌ Failed to connect to database: {e}")
        return False
