import re

def extract_sql_queries(input_buffer):
    # Define the SQL query regex pattern
    sql_pattern = re.compile(r"(?i)(SELECT\s+.+?\s+FROM\s+.+?|INSERT\s+INTO\s+.+?\s+VALUES\s*\(.+?\)|UPDATE\s+.+?\s+SET\s+.+?|DELETE\s+FROM\s+.+?|CREATE\s+TABLE\s+.+?\s*\(.+?\);?)")

    # Find all SQL queries in the input buffer
    sql_queries = re.findall(sql_pattern, input_buffer)

    # Clear input buffer (emulating clearing older messages)
    input_buffer = ""

    if not sql_queries:
        return [], input_buffer  # Return an empty list and cleared buffer

    return sql_queries, input_buffer

# Example input buffer containing mixed messages
# input_buffer = """
# Hello, how are you? 
# SELECT * FROM users WHERE age > 18;
# Some random message.
# CREATE TABLE test_2;
# CREATE TABLE test_3 (id INT, name VARCHAR(50));
# INSERT INTO products (id, name, price) VALUES (1, 'Laptop', 1000);
# Random text again.
# UPDATE users SET name = 'John Doe' WHERE id = 2;
# Goodbye.
# """
