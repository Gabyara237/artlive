import os
import psycopg2

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            database=os.getenv('POSTGRES_DATABASE'),
            user=os.getenv('POSTGRES_USERNAME'),
            password=os.getenv('POSTGRES_PASSWORD')
        )
        print('Successful connection to the database.')
        return connection
    
    except Exception as err:
        print('err:',err)

        return None


