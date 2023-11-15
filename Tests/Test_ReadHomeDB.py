# Tested remotely from Cell Service over Tailscale vpn
import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Database connection details
host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT'))
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

# Establish database connection
connection = pymysql.connect(host=host, port=port, user=user, password=password, db=database)

try:
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a SELECT query
    query = 'SELECT * FROM HIST LIMIT 3'
    cursor.execute(query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Display the retrieved data
    for row in rows:
        print(row)

finally:
    # Close the database connection
    connection.close()
