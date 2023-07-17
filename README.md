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

```bash
python3 postgres_json_driver.py
```

## Database Connection and Data Loading
- This guide is a command line tutorial for connecting to a PostgreSQL database and loading data into the database on a linux machine.
- The guide assumes that you have a PostgreSQL database installed on your machine and that you have a user with the appropriate permissions to create a database and load data into it.

### Create a Database
- Open a terminal and run the following command to connect to the PostgreSQL database server:
```bash
sudo -u postgres psql
```

- Create a database by running the following command:
```sql
CREATE DATABASE driver_db;
```

- Connect to the database by running the following command:
```sql
\c driver_db
```

### Create a Table
- Create a table by running the following command:
```sql
CREATE TABLE IF NOT EXISTS public.user_table
(
user_id numeric(10,0) NOT NULL,
name character varying(50) COLLATE pg_catalog."default" NOT NULL, age numeric(3,0) NOT NULL,
phone character varying(20) COLLATE pg_catalog."default",
CONSTRAINT user_table_pkey PRIMARY KEY (user_id)
);
```

### Grant Permissions
- Grant permissions to the user by running the following command:
```sql
GRANT ALL PRIVILEGES ON TABLE user_table TO postgres;
```

### Load Data
- Load data into the table by running the following command:
```sql
INSERT INTO public.user_table (user_id, name, age, phone) VALUES (3, 'Jenny', 34, NULL);
INSERT INTO public.user_table (user_id, name, age, phone) VALUES (2, 'Tom', 29, '1-800-123-1234');
INSERT INTO public.user_table (user_id, name, age, phone) VALUES (1, 'John', 28, NULL);
```



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

