import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def execute_sql_commands(sql_commands):
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        # Execute each SQL command in the list
        for sql_command in sql_commands:
            print(f"Executing SQL: {sql_command}")
            cursor.execute(sql_command)

        # Commit after all commands
        connection.commit()
        # Clear the list after execution
        sql_commands.clear()
        print("All SQL commands executed and array cleared!")
    
    except Exception as e:
        print(f"Error executing SQL commands: {e}")
        connection.rollback()  # Roll back in case of error
    
    finally:
        if connection:
            cursor.close()
            connection.close()
