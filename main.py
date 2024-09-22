from hface import query_model
from dbcon import execute_sql_commands
from config import INPUT_PROMPT, API_TOKEN
from query_extraction import extract_sql_queries

def main():
    api_token = API_TOKEN
    input_prompt = input(INPUT_PROMPT)  # Prompt user for input

    if input_prompt.lower() == 'exit':
        print("Exiting the program.")
        return

    # Step 1: Query the Hugging Face model with the input
    try:
        sql_command = query_model(input_prompt, api_token)
        if sql_command:
            # Step 2: Extract and filter SQL queries
            extracted_sql, _ = extract_sql_queries(sql_command)
            
            # Check if there are any SQL queries extracted
            if extracted_sql:
                # Step 3: Format and execute SQL queries
                for sql_exct in extracted_sql:
                    formatted_sql = format_sql_query(sql_exct)
                    execute_sql_commands([formatted_sql])
            else:
                print("No valid SQL queries found.")

    except Exception as e:
        print(f"Error processing input: {e}")

def format_sql_query(sql_query):
    # Basic formatting function; you can enhance this as needed
    return sql_query.strip()  # Strip whitespace or modify further

if __name__ == "__main__":
    main()
