from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os
import pymysql
pymysql.install_as_MySQLdb()


# Load environment variables
load_dotenv()

# Get the DATABASE_URL from the .env file
database_url = os.getenv("Mysql_URL")

# Function to test database connection
def test_database_connection():
    try:
        # Create an engine instance
        engine = create_engine(database_url)

        # Connect to the database
        with engine.connect() as connection:
            # If connection is successful
            print("Database connection successful.")
            return True
    except SQLAlchemyError as e:
        # If connection fails, print the error
        print(f"Database connection failed: {e}")
        return False

# Run the test function
test_database_connection()
