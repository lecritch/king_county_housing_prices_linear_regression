from io import BytesIO, TextIOWrapper, StringIO
from zipfile import ZipFile
from gzip import GzipFile
from csv import QUOTE_ALL

import pandas as pd
import requests

from src.data import sql_utils

def download_data_and_load_into_sql():
    """
    This function dispatches everything.  It creates a PostgreSQL database with
    the appropriate name, sets up the table schema, downloads all of the files
    containing the data, and loads the data into the database
    """
    sql_utils.create_database_and_tables()
    data_files_dict = collect_all_data_files()
    load_into_sql(data_files_dict)


def collect_all_data_files():
    """
    Create a dictionary with the in-memory file objects associated with all
    database tables
    """
    data_files_dict = {
        "real_property_sales": collect_real_property_sales_data(),
        "residential_building": collect_residential_building_data(),
        "parcel": collect_parcel_data(),
        "lookup": collect_lookup_data(),
    }
    return data_files_dict


def load_into_sql(data_files_dict):
    """
    Given a dictionary of in-memory file objects, use sql_utils to copy them
    into the database.  Then close all of them.

    Each dictionary value is a tuple containing a CSV file object, then either
    None or some other file to be closed, e.g. a zip file
    """
    sql_utils.copy_csv_files(data_files_dict)

    for csv_file, other_file in data_files_dict.values():
        csv_file.close()
        if other_file:
            other_file.close()


def collect_real_property_sales_data():
    """
    Download the King County Housing Prices sales data
    """
    REAL_PROPERTY_URL = "https://aqua.kingcounty.gov/extranet/assessor/Real%20Property%20Sales.zip"
    REAL_PROPERTY_CSV_NAME = "EXTR_RPSale.csv"
    return collect_zipfile_data(REAL_PROPERTY_URL, REAL_PROPERTY_CSV_NAME)


def collect_residential_building_data():
    """
    Download the residential building data
    """ 
    RESIDENTIAL_BUILDING_URL = "https://aqua.kingcounty.gov/extranet/assessor/Residential%20Building.zip"
    RESIDENTIAL_BUILDING_CSV_NAME = "EXTR_ResBldg.csv"
    return collect_zipfile_data(RESIDENTIAL_BUILDING_URL, RESIDENTIAL_BUILDING_CSV_NAME)


def collect_parcel_data():
    """
    Download the parcels data
    """
    PARCELS_URL = "https://aqua.kingcounty.gov/extranet/assessor/Parcel.zip"
    PARCELS_CSV_NAME = "EXTR_Parcel.csv"
    return collect_zipfile_data(PARCELS_URL, PARCELS_CSV_NAME)


def collect_lookup_data():
    """
    Download the lookup data
    """
    LOOKUP_URL = "https://aqua.kingcounty.gov/extranet/assessor/Lookup.zip"
    LOOKUP_CSV_NAME = "EXTR_LookUp.csv"
    return collect_zipfile_data(LOOKUP_URL, LOOKUP_CSV_NAME)



def collect_zipfile_data(URL, csv_name):
    """
    Helper function used to collect CSV files contained in .zip archives
    """
    zip_file = download_zipfile(URL)
    csv_file = open_csv_from_zip(zip_file, csv_name)
    # return both so we can safely close them at the end
    return csv_file, zip_file


def collect_csv_data(URL):
    """
    Given a URL for an un-compressed CSV, download and open it
    """
    response = requests.get(URL)
    print(f"""Successfully downloaded CSV file
    {URL}
    """)

    content_as_file = BytesIO(response.content)
    csv_file_text = TextIOWrapper(content_as_file, encoding="ISO-8859-1")
    # only 1 file needs to be closed, but later code is expecting a tuple
    return csv_file_text, None


def download_zipfile(URL):
    """
    Given a URL for a .zip, download and unzip the .zip file
    """
    response = requests.get(URL)
    print(f"""Successfully downloaded ZIP file
    {URL}
    """)

    content_as_file = BytesIO(response.content)
    zip_file = ZipFile(content_as_file)
    return zip_file


def open_csv_from_zip(zip_file, csv_name):
    """
    Given an unzipped .zip file and the name of a CSV inside of it, 
    extract the CSV and return the relevant file
    """
    csv_file_bytes = zip_file.open(csv_name)
    # it seems we have to open the .zip as bytes, but CSV reader requires text
    csv_file_text = TextIOWrapper(csv_file_bytes, encoding="ISO-8859-1")
    return csv_file_text



