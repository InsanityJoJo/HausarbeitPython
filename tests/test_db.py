import pytest
import pandas as pd
from sqlalchemy.orm import sessionmaker
from src.train_tbl import Train
from src.base_tbl import Base
from database.engine import engine

# Setup der DB für den Test
@pytest.fixture(scope="module")
def db_session():
    '''
    Diese Methode setzt die DB auf einen bekannten Zustand vor dem Test. - Setup
    Der Test kann dann mit Testdaten ausgeführt werden. 
    Nach dem Test wird die Kotrolle der Session an diese Methode zurückgegeben, 
    anschließend wird der Ausgangstzustand wiederhergestellt. - Teardown
    '''

    # Datenbank wird vor den Test gesetzt- Setup
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session  # Gibt die Kontrolle an den Test zurück

    # Teardown
    session.close()
    Base.metadata.drop_all(engine)

def test_db_insertion(db_session):
    '''
    Diese Methode testet das Hinzufühen von Daten an die db,
    inder Trainingsdatentabelle.

    Methodenparameter:
    - db_session: Testsession für diesen Test. pytest Fixure

    
    '''
    # Testdaten 
    df_train_data = pd.DataFrame([{"x": 1, "y1": 0.313, "y2": 797, "y3": 0.4, "y4": 2}])
    Train.add_df_to_tbl(df_train_data)

    # Überprüfen ob die Daten korrekt angefügt wurden
    inserted_data = db_session.query(Train).all()
    assert len(inserted_data) == 1
    assert inserted_data[0].x == 1
    assert inserted_data[0].y1 == 0.313
    assert inserted_data[0].y2 == 797
    assert inserted_data[0].y3 == 0.4
    assert inserted_data[0].y4 == 2