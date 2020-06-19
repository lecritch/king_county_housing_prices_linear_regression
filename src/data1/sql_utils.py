import psycopg2
import pandas as pd
import os

DBNAME = "king_county_housing_prices"

def create_database_and_tables():
    create_database()
    create_tables()
    print("Successfully created database and all tables")
    print()


def create_database():
    """
    This function assumes that you have an existing database called `postgres`
    without any username/password required to access it.  Then it creates a new
    database called `king_county_housing_prices`
    """
    # Depending on your local settings, you may need to specify a user and password, e.g.
    # conn = psycopg2.connect(dbname="postgres", user="postgres", password="password")

    conn = psycopg2.connect(dbname="postgres")
    conn.autocommit = True  # it seems this mode is needed to make a db
    conn.set_isolation_level(0)  # also this for dropping db

    # un-comment this line if you already have a database called
    # `king_county_housing_prices` and you want to drop it
    #execute_sql_script(conn, "01_drop_old_database.sql")
    #execute_sql_script(conn, "02_create_new_database.sql")

    conn.close()


def create_tables():
    """
    Composite function that creates all relevant tables in the database
    This creates empty tables with the appropriate schema, then the data
    transfer is performed in the `copy_csv_files` function
    """
    # Depending on your local settings, you may need to specify a user and password, e.g.
    # conn = psycopg2.connect(dbname=DBNAME, user="postgres", password="password")
    conn = psycopg2.connect(dbname=DBNAME)

    create_real_property_sales(conn)
    create_residential_building(conn)
    create_parcel(conn)
    create_lookup(conn)

    conn.close()


def create_real_property_sales(conn):
    """
    Create a table for the real property sales data
    """
    execute_sql_script(conn, "03_create_real_property_sales.sql")


def create_residential_building(conn):
    """
    Create a table for the residential building data
    """
    execute_sql_script(conn, "04_create_residential_building.sql")


def create_parcel(conn):
    """
    Create a table for the parcel data
    """
    execute_sql_script(conn, "05_create_parcel.sql")


def create_lookup(conn):
    """
    Create a table for the lookup data
    """
    execute_sql_script(conn, "06_create_lookup.sql")


def copy_csv_files(data_files_dict):
    """
    Composite function that copies all CSV files into the database
    """
    # Depending on your local settings, you may need to specify a user and password, e.g.
    # conn = psycopg2.connect(dbname=DBNAME, user="postgres", password="password")
    conn = psycopg2.connect(dbname=DBNAME)

    for name, files in data_files_dict.items():
        csv_file = files[0]
        # skip the header; this info is already in the table schema
        next(csv_file)
        if name == "real_property_sales":
            copy_csv_to_real_property_sales_table(conn, csv_file)
        elif name == "residential_building":
            copy_csv_to_residential_building_table(conn, csv_file)
        elif name == "parcel":
            copy_csv_to_parcel_table(conn, csv_file)
        elif name == "lookup":
            copy_csv_to_lookup_table(conn, csv_file)

        print(f"""Successfully loaded CSV file into `{name}` table
        """)

    conn.close()


def copy_csv_to_real_property_sales_table(conn, csv_file):
    """
    Copy the CSV contents of real property sales into the table
    """
    COPY_REAL_PROPERTY_SALES = "07_copy_real_property_sales_to_table.psql"
    copy_expert_psql_script(conn, COPY_REAL_PROPERTY_SALES, csv_file)


def copy_csv_to_residential_building_table(conn, csv_file):
    """
    Copy the txt contents of the residential building data into the table
    """
    COPY_RESIDENTIAL_BUILDING = "08_copy_residential_building_to_table.psql"
    copy_expert_psql_script(conn, COPY_RESIDENTIAL_BUILDING, csv_file)


def copy_csv_to_parcel_table(conn, csv_file):
    """
    Copy the csv contents of the parcel data into the table
    """
    COPY_PARCELS = "09_copy_parcel_to_table.psql"
    copy_expert_psql_script(conn, COPY_PARCELS, csv_file)


def copy_csv_to_lookup_table(conn, csv_file):
    """
    Copy the csv contents of the lookup data into the table
    """
    COPY_LOOKUP = "10_copy_lookup_to_table.psql"
    copy_expert_psql_script(conn, COPY_LOOKUP, csv_file)


def execute_sql_script(conn, script_filename):
    """
    Given a DB connection and a file path to a SQL script, open up the SQL
    script and execute it
    """
    file_contents = open_sql_script(script_filename)
    cursor = conn.cursor()
    cursor.execute(file_contents)
    conn.commit()


def open_sql_script(script_filename):
    """
    Given a file path, open the file and return its contents
    We assume that the file path is always inside the sql directory
    """
    dir = os.path.dirname(__file__)
    relative_filename = os.path.join(dir, 'sql', script_filename)

    file_obj = open(relative_filename, 'r')
    file_contents = file_obj.read()
    file_obj.close()

    return file_contents


def copy_expert_psql_script(conn, script_filename, csv_file):
    """
    Given a DB connection and a file path to a PSQL script, open up the PSQL
    script and use it to run copy_expert
    """
    file_contents = open_sql_script(script_filename)
    cursor = conn.cursor()
    cursor.copy_expert(file_contents, csv_file)
    conn.commit()

