import pytest
import pandas as pd
from src.data_loading import DataLoader
from src.ideal_tbl import Ideal
from src.base_tbl import Base
from src.mse_results_tbl import Result
from database.engine import engine
from src.math_logic import Mathematics


def test_csv_loading_and_db_insertion(db_session):
    '''
    In dieser Testmethode soll die Zusammenarbeit zwischen 
    Datenbank, DataLoader, Ideal, Base und engine getestet werden.
    Um Wiederverwendbarkeit und Reggression zu gewährleisten wird
    zum Setup und Teardown pytest fixure verwendet.
    '''

    # Laden der Daten mit dem DataLoader aus der CSV in ein Dataframe
    data_loader = DataLoader('data/example_data/ideal.csv')
    df_ideal = data_loader.load_data()

    # Check, dass Daten als Dataframe geladen wurden
    assert df_ideal is not None

    # Laden der Daten in die Datenbank in die entsprechende tabelle für Ideale Daten.
    Ideal.add_df_to_tbl(df_ideal)
    
    # Abfrage wie viele Einträge in der Tabelle vorhanden sind.  
    inserted_data_count = db_session.query(Ideal).count()

    # Check ob die Länge der Daten, der Länge der übergeben Daten entspricht.
    assert inserted_data_count == len(df_ideal)

    # Liste der zu verleichenden Spalten definieren, hier x, y1 bis y50
    columns_to_compare = ['x'] + [f'y{i}' for i in range(1, 51)]

    # Daten aus der Datenbank in ein Dataframe Landen
    sql_query = db_session.query(Ideal).statement
    inserted_data_df = pd.read_sql_query(sql_query, con=engine)

    # Filtern, sodass nur die relevanten Spalten im DF enthalten sind
    df_ideal_filtered = df_ideal[columns_to_compare]
    inserted_data_df_filtered = inserted_data_df[columns_to_compare]

    # Check ob der Inhalt der Spalte x, y1, bis y50 übereinstimmt.
    assert df_ideal_filtered.equals(inserted_data_df_filtered)

    # Stichprobe bei y1 = -0,9129453 ob die Daten tatsächlich richtig angefügt wurden
    assert df_ideal_filtered.at[0, 'y1'] == -0.9129453

def test_load_data_mse_store_result(db_session):
    '''
    Diese Methode ist ein Integrationstest für das Laden von Daten,
    das berechnen des MSE, das Speichen der Ergebnisse in der Result Tabelle

    '''

    train_loader = DataLoader("data/example_data/train.csv")  # Loader für die train.csv
    ideal_loader = DataLoader("data/example_data/ideal.csv")  # Loader für die ideal.csv

    train = train_loader.load_data()  # Speichern der Trainingsdaten als Dataframe
    ideal = ideal_loader.load_data()  # Speichern der Idealfunktionen als Dataframe
    # Berechung des MSE aus den Daten
    min_mse = Mathematics()
    result_df = min_mse.calculate_min_mse(train, ideal)

    # Check ob das df Daten enthält.
    assert result_df is not None
    # Speichern des results in der Result Tabelle
    Result.add_df_to_tbl(result_df)

    # Dataframe der in Results enthaltenen Daten für den späteren Vergleich
    sql_query = db_session.query(Result).statement
    inserted_data_df = pd.read_sql_query(sql_query, con=engine)

    # Liste der zu verleichenden Spalten definieren, hier x, y1 bis y50
    columns_to_compare = ['y_train_col', 'best_ideal_col', 'min_mse']

    # Filtern, sodass nur die relevanten Spalten im DF enthalten sind
    df_results_filtered = result_df[columns_to_compare]
    inserted_data_df_filtered = inserted_data_df[columns_to_compare]
    
    # Check ob der Inhalt übereinstimmt
    # Check ob der Inhalt der Spalte x, y1, bis y50 übereinstimmt.
    assert df_results_filtered.equals(inserted_data_df_filtered)