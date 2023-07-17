import psycopg2
import json
from decimal import Decimal

# Custom JSON encoder to handle Decimal objects


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

# Function to execute SQL queries and return the results as JSON


def execute_query(query):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="driver_db",
            user="test_user",
            password="root",
            port=5432,  # change the port number if necessary
        )
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert the query results to a list of dictionaries
        data = [
            {"user_id": row[0], "name": row[1], "age": row[2], "phone": row[3]}
            for row in rows
        ]

        # Create the JSON object with the custom DecimalEncoder
        json_data = {"status_code": 200, "data": data}

        # Write the JSON object to a file using the custom encoder
        with open("output.json", "w") as file:
            json.dump(json_data, file, indent=4, cls=DecimalEncoder)

        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error executing query:", e)


# Example usage: Execute a SQL query and generate the JSON file
query = "SELECT * FROM public.user_table"
execute_query(query)
