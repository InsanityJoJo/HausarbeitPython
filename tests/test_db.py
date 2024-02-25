import pytest
import pandas as pd
from src.train_tbl import Train

def test_db_insertion(db_session):
    '''
    Diese Methode testet das Hinzufühen von Daten an die db,
    inder Trainingsdatentabelle.

    Um Wiederverwendbarkeit und Reggression zu gewährleisten wird
    zum Setup und Teardown pytest fixure verwendet.
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