import logging
from app.db.database import engine, create_db_and_tables
from sqlalchemy import text
from app.db.models import member, payment, user
logger = logging.getLogger('uvicorn.error')

# Function to run during server start up.
# To initialize and check various components required by the application.
# Raises error if any function fails.
def startup():
    logger.info("\n")
    logger.info("Start up check for Fastapi Gym Management\n")
    check_db_connection()
    init_database_models()

def check_db_connection():
    logger.info("Starting Database")
    logger.info("Connecting to database.....")
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            logger.info("Database connected successfully!\n")
    except:
        logger.error("Database connection failed!\n")

def init_database_models():
    logger.info("Initializing Database Models.....")
    try:
        create_db_and_tables()
        logger.info("Database Models initialization successfully!\n")
    except Exception as e:
        print(e)
        logger.error("Database Models initialization failed!\n")