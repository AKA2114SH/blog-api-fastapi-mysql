# Import necessary SQLAlchemy modules
from sqlalchemy import create_engine  # Used to establish a connection to the database
from sqlalchemy.orm import sessionmaker  # Provides a factory for creating new database sessions
from sqlalchemy.ext.declarative import declarative_base  # Base class for all model classes

# Define the database URL (connection string) - replace with actual database URL
URL_DATABASE = 'mysql+pymysql://root:MYSQL2114@localhost/BlogApplication'



# Create an SQLAlchemy engine to manage the connection to the database
# The engine is responsible for SQL dialects, connections, and managing resources
engine = create_engine(URL_DATABASE)

# Configure a session factory to handle database sessions
# autocommit=False ensures that transactions are committed manually
# autoflush=False prevents automatic flushing of changes to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base class for model classes using the declarative base
# All ORM models will inherit from this base class
Base = declarative_base()
