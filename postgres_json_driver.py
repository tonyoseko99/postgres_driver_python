import psycopg2
import json

# Function to execute SQL queries and return the results as JSON
def execute_query(query):
    try:
        conn = psycopg2.connect(
            host="your_host",
            database="your_database",
            user="your_username",
            password="your_password",
            port=5432,  # change the port number if necessary
        )
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert the query results to JSON string format
        json_result = json.dumps(
            {"status_code": 200, "data": [dict(row) for row in rows]}
        )

        cursor.close()
        conn.close()
        return json_result
    except psycopg2.Error as e:
        print("Error executing query:", e)
        return json.dumps({"status_code": 500, "error": str(e)})


# Example usage: Execute a SQL query and print the JSON result
query = "SELECT * FROM public.user_table"
json_result = execute_query(query)
print(json_result)
