import pytest
import logging
import pandas as pd
from src.test_tbl import DataTableTest
from database.engine import engine

def test_testdata_valid(db_session):
    # Daten aus der Datenbank in ein Dataframe Landen
    sql_query = db_session.query(DataTableTest).statement
    test_df = pd.read_sql_query(sql_query, con=engine)
    
    test_df.sort_values(by='x_punkt', ascending=False)
    logging.info()
    assert test_df is not None
