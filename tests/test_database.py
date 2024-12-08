import os
from pathlib import Path
import psycopg2
import pytest
from dotenv import load_dotenv
import json

def load_data_from_json(filename, key=None):
    """Load test data from a json"""
    tests_folder = Path(__file__).resolve().parent.parent / "tests"
    file_path = tests_folder / filename

    if file_path.suffix == ".json":
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data if key is None else data[key]

@pytest.fixture(scope="session")
def database_connection_setup():
    """Setup and tear down the database connection"""
    env_path = Path(__file__).parent / "database.env"
    load_dotenv(dotenv_path=env_path)

    database_info = {
        "host": os.getenv('POSTGRES_HOST'),
        "port": os.getenv('POSTGRES_PORT'),
        "dbname": os.getenv('POSTGRES_DB'),
        "user": os.getenv('POSTGRES_USER'),
        "password": os.getenv('POSTGRES_PASSWORD')
    }

    with psycopg2.connect(**database_info) as connection:
        yield connection


@pytest.fixture()
def cursor(database_connection_setup):
    with database_connection_setup.cursor() as cursor:
        yield cursor


@pytest.mark.parametrize("test_database_queries", load_data_from_json("test_database_queries.json", "queries"))
def test_provided_queries(cursor, test_database_queries):
    cursor.execute(test_database_queries["query"])
    actual_results = cursor.fetchall()
    expected_results = [tuple(row) for row in test_database_queries["expected_results"]]
    
    assert actual_results == expected_results