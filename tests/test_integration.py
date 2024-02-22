import pytest
import pandas as pd
from src.data_loading import DataLoader
from src.ideal_tbl import Ideal
from src.base_tbl import Base
from database.engine import engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope='module')
def db_session():
    # Setup
    Base.metadata.create_all(engine)  # Erstelle der Tabellen
    Session = sessionmaker(bind=engine)
    session = Session()
    # Test
    yield session # Hier laufen die Tests
    # Teardown
    session.close()
    Base.metadata.drop_all(engine) # Bereinige die Daten

def test_csv_loading_and_db_insertion(db_session):
    # Laden der Daten aus der Methode DataLoader
    data_loader = DataLoader('data/example_data/ideal.csv')
    df_ideal = data_loader.load_data()

    # Wurden Daten geladen
    assert df_ideal is not None

    # Laden der Daten in die db
    Ideal.add_df_to_tbl(df_ideal)

    inserted_data_count = db_session.query(Ideal).count()
    assert inserted_data_count == len(df_ideal)