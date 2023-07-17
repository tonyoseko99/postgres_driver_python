# PostgreSQL JSON Driver

The PostgreSQL JSON Driver is a Python script that connects to a PostgreSQL database using the `psycopg2` library and executes SQL queries. It returns the query results in JSON string format.

## Requirements

- Python 3.x
- `psycopg2` library

## Installation

1. Clone the repository or download the `postgres_json_driver.py` file.

2. Install the required dependency by running the following command:


## Usage

1. Open the `postgres_json_driver.py` file in a text editor.

2. Replace the connection details (`host`, `database`, `user`, `password`, and `port`) with your PostgreSQL database information.

3. Save the file.

4. Open a terminal in the project directory.

5. Run the script by executing the following command:


The script will execute the SQL query specified in the `execute_query` function and print the JSON result.

## Example

The provided example executes the following SQL query:
```sql
`SELECT * FROM public.user_table`

```

## Notes
- Make sure you have a PostgreSQL database with the appropriate table (public.user_table) and data inserted before running the script.
- Adjust the SQL query in the execute_query function to match your database structure.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- [psycopg2](https://pypi.org/project/psycopg2/)
- [PostgreSQL](https://www.postgresql.org/)

