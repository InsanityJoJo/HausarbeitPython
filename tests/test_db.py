import pytest
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from src.db_tables.base_tbl import Base
from src.db_tables.train_tbl import Train
from src.db_tables.ideal_tbl import Ideal
from src.db_tables.exp_tbl import Test
from src.db_tables.mse_results_tbl import Result
from src.db_tables.validation_result_tbl import Summery
from src.math_logic import Mathematics
from unittest.mock import patch

class TestDB:
    '''
    Diese Klasse Testet die Datenbank und das Anfügen
    von Daten an die Tabellen. 
    Die Logging Nachrichten werden durch Mock-Logging überprüft
    Aktuelle

    Testmethoden:
    - test_add_df_to_tbl_base_success(): Test der Oberklasse Base
    - test_add_df_to_tbl_train_success(): Test der Unterklasse Train
    - test_add_df_to_tbl_ideal_success(): Test der Unterklasse Ideal
    - test_add_df_to_tbl_test_success(): Test der Unterklasse Test
    - test_add_df_to_tbl_mse_success(): Test der Unterklasse Result
    - test_add_df_to_tbl_summery_success(): Test der Unterklasse Summery
    - test_add_df_to_tbl_fail(): Test des Anfügens mit falschen DFs
    '''
    def test_add_df_to_tbl_base_success(self, engine_fixture, sample_dataframes):
        '''
        Die Testmethode prüft das Anfügen an die Tabelle Bas
        Die Tabelle Base ist die Oberklasse und wird nicht
        zur Speicherung verwendent. Sie stellt ihre Funktionen
        für die Unterklassen Train, Ideal, Test, Result, Summery
        zur Verfügung. In diesem Test wird nur die Funktion 
        add_df_to_tbl überprüft.

        '''
        train_df, _, _ = sample_dataframes  # Extraktion des Trainingsdaten-DataFrames
        Base.__tablename__ = 'test_table'

        # Mock-Objekt für das Logging         
        with patch('src.db_tables.base_tbl.logging') as mock_logging:
            # Methode ausführen, die getestet werden soll
            Base.add_df_to_tbl(train_df, engine_fixture)
            
            # Überprüfen, ob die Erfolgsnachricht korrekt protokolliert wurde
            mock_logging.info.assert_called_once()
        
    def test_add_df_to_tbl_train_success(self, db_session, engine_fixture, sample_dataframes):
        '''
        Diese Testmethode prüft das Anfügen an die Tabelle Train.
        
        Im ersten Teil wird überprüft, ob das positive Anfügen von
        Daten zu einer Erfolgsnachricht führt.
        
        Im zweiten Teil wird überprüft ob die Anzahl der Zeilen
        übereinstimmt.
        
        Im dritten Teil wird überprüft ob die ein aus der Tablle
        generiertes Dataframe die gewünschten Spalten hat.

        Methodenparameter:
        - db_session: pytest fixture für die DB Arbeit in Conftest.py
        - engine:fixture: pytest fixture für die verbindung zur DB in Conftest.py
        - sample_dataframes: pytest fixture der Beispieldaten in Conftest.py
        '''
        train_df, _, _ = sample_dataframes  # Extraktion des Trainingsdaten-DataFrames
        
        # Mock-Objekt für das Logging
        with patch('src.db_tables.train_tbl.logging') as mock_logging:
            Train.add_df_to_tbl(train_df, engine_fixture)  # Methode ausführen
            mock_logging.info.assert_called_once()  # Überprüfen der Erfolgsnachricht

        # Überprüfen, ob die Daten korrekt angefügt wurden
        inserted_data = db_session.query(Train).all()
        # Überprüfen der Anzahl der eingefügten Zeilen
        assert len(inserted_data) == len(train_df)

        # Laden der Daten aus der Datenbanktabelle in einen DataFrame
        df = pd.read_sql_query(db_session.query(Train).statement, con=db_session.bind)

        # Erwartete Spaltennamen aus dem SQLAlchemy Modell extrahieren
        expected_columns = [column.name for column in Train.__table__.columns]

        # Vergleichen der Spaltennamen des DataFrame mit den erwarteten Spaltennamen.
        assert set(df.columns) == set(expected_columns), "Die Spaltennamen stimmen nicht überein."

        # Stichprobe ob bei y1 = 100.216064 die Daten richtig angefügt worden sind.
        assert df.at[0, 'Y1 (Training Funktion)'] == 100.216064

    def test_add_df_to_tbl_ideal_success(self, db_session, engine_fixture, sample_dataframes):
        '''
        Diese Testmethode prüft das Anfügen an die Tabelle Ideal.
        
        Im ersten Teil wird überprüft, ob das positive Anfügen von
        Daten zu einer Erfolgsnachricht führt.
        
        Im zweiten Teil wird überprüft ob die Anzahl der Zeilen
        übereinstimmt.
        
        Im dritten Teil wird überprüft ob die ein aus der Tablle
        generiertes Dataframe die gewünschten Spalten hat.

        Methodenparameter:
        - db_session: pytest fixture für die DB Arbeit in Conftest.py
        - engine:fixture: pytest fixture für die verbindung zur DB in Conftest.py
        - sample_dataframes: pytest fixture der Beispieldaten in Conftest.py
        '''
        _, ideal_df, _ = sample_dataframes  # Extraktion des Ideal-DataFrames
        
        # Mock-Objekt für das Logging
        with patch('src.db_tables.ideal_tbl.logging') as mock_logging:
            Ideal.add_df_to_tbl(ideal_df, engine_fixture)  # Methode ausführen
            mock_logging.info.assert_called_once()  # Überprüfen der Erfolgsnachricht        
        
        # Überprüfen, ob die Daten korrekt angefügt wurden
        inserted_data = db_session.query(Ideal).all()
        # Überprüfen der Anzahl der eingefügten Zeilen
        assert len(inserted_data) == len(ideal_df) 

        # Laden der Daten aus der Datenbanktabelle in einen DataFrame
        df = pd.read_sql_query(db_session.query(Ideal).statement, con=db_session.bind)

        # Erwartete Spaltennamen aus dem SQLAlchemy Modell extrahieren
        expected_columns = [column.name for column in Ideal.__table__.columns]

        # Vergleichen der Spaltennamen des DataFrame mit den erwarteten Spaltennamen
        assert set(df.columns) == set(expected_columns), "Die Spaltennamen stimmen nicht überein"
        
        # Stichprobe bei y1 = -0,9129453 ob die Daten tatsächlich richtig angefügt wurden
        assert df.at[0, 'Y1 (Ideale Funktion)'] == -0.9129453
    
    def test_add_df_to_tbl_test_success(self, db_session, engine_fixture, sample_dataframes):
        '''
        Diese Testmethode prüft das Anfügen an die Tabelle Test.
        
        Im ersten Teil wird überprüft, ob das positive Anfügen von
        Daten zu einer Erfolgsnachricht führt.
        
        Im zweiten Teil wird überprüft ob die Anzahl der Zeilen
        übereinstimmt.
        
        Im dritten Teil wird überprüft ob die ein aus der Tablle
        generiertes Dataframe die gewünschten Spalten hat.

        Methodenparameter:
        - db_session: pytest fixture für die DB Arbeit in Conftest.py
        - engine:fixture: pytest fixture für die verbindung zur DB in Conftest.py
        - sample_dataframes: pytest fixture der Beispieldaten in Conftest.py
        '''
        _, _, test_df = sample_dataframes  # Extraktion des Test-DataFrames
        
        # Mock-Objekt für das Logging
        with patch('src.db_tables.exp_tbl.logging') as mock_logging:
            Test.add_df_to_tbl(test_df, engine_fixture)  # Methode ausführen
            mock_logging.info.assert_called_once()  # Überprüfen der Erfolgsnachricht

        # Überprüfen, ob die Daten korrekt angefügt wurden
        inserted_data = db_session.query(Test).all()
        # Überprüfen der Anzahl der eingefügten Zeilen
        assert len(inserted_data) == len(test_df) 

        # Laden der Daten aus der Datenbanktabelle in einen DataFrame
        df = pd.read_sql_query(db_session.query(Test).statement, con=db_session.bind)

        # Erwartete Spaltennamen aus dem SQLAlchemy Modell extrahieren
        expected_columns = [column.name for column in Test.__table__.columns]

        # Vergleichen der Spaltennamen des DataFrame mit den erwarteten Spaltennamen
        assert set(df.columns) == set(expected_columns), "Die Spaltennamen stimmen nicht überein."

        # Stichprobe bei y = 4.9 ob die Daten tatsächlich richtig angefügt wurden
        assert df.at[0, 'x_punkt'] == 4.9

    def test_add_df_to_tbl_mse_success(self, db_session, engine_fixture, sample_dataframes):
        '''
        Diese Testmethode prüft das Anfügen an die Tabelle Result.
        
        Im ersten Teil wird überprüft, ob das positive Anfügen von
        Daten zu einer Erfolgsnachricht führt.
        
        Im zweiten Teil wird überprüft ob die Anzahl der Zeilen
        übereinstimmt.
        
        Im dritten Teil wird überprüft ob die ein aus der Tablle
        generiertes Dataframe die gewünschten Spalten hat.

        Methodenparameter:
        - db_session: pytest fixture für die DB Arbeit in Conftest.py
        - engine:fixture: pytest fixture für die verbindung zur DB in Conftest.py
        - sample_dataframes: pytest fixture der Beispieldaten in Conftest.py
        '''
        # Extraktion der DataFrames
        train_df, ideal_df, _ = sample_dataframes
        # Berechnung MSE
        mse_df = Mathematics.calculate_min_mse(train_df, ideal_df) 
        
        # Mock-Objekt für das Logging
        with patch('src.db_tables.base_tbl.logging') as mock_logging:
            Result.add_df_to_tbl(mse_df, engine_fixture)  # Methode ausführen
            mock_logging.info.assert_called_once()  # Überprüfen der Erfolgsnachricht
        
        # Überprüfen, ob die Daten korrekt angefügt wurden
        inserted_data = db_session.query(Result).all()
        # Überprüfen der Anzahl der eingefügten Zeilen
        assert len(inserted_data) == len(mse_df)             

        # Laden der Daten aus der Datenbanktabelle in einen DataFrame
        df = pd.read_sql_query(db_session.query(Result).statement, con=db_session.bind)

        # Erwartete Spaltennamen aus dem SQLAlchemy Modell extrahieren
        expected_columns = [column.name for column in Result.__table__.columns]

        # Vergleichen der Spaltennamen des DataFrame mit den erwarteten Spaltennamen
        assert set(df.columns) == set(expected_columns), "Die Spaltennamen stimmen nicht überein."

        # Stichprobe ob 0, best_ideal_col = y36 ist.
        assert df.at[0, 'best_ideal_col'] == 'y36'

    def test_add_df_to_tbl_summery_success(self, db_session, engine_fixture, sample_dataframes):
        '''
        Diese Testmethode prüft das Anfügen an die Tabelle Summery.
        
        Im ersten Teil wird überprüft, ob das positive Anfügen von
        Daten zu einer Erfolgsnachricht führt.
        
        Im zweiten Teil wird überprüft ob die Anzahl der Zeilen
        übereinstimmt.
        
        Im dritten Teil wird überprüft ob die ein aus der Tablle
        generiertes Dataframe die gewünschten Spalten hat.

        Methodenparameter:
        - db_session: pytest fixture für die DB Arbeit in Conftest.py
        - engine:fixture: pytest fixture für die verbindung zur DB in Conftest.py
        - sample_dataframes: pytest fixture der Beispieldaten in Conftest.py
        '''
        train_df, ideal_df, test_df = sample_dataframes  # Extraktion des Train-DataFrames

        # Berechnung MSE
        mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
        # Berechnung Validierung
        summery_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df) 
   
        # Mock-Objekt für das Logging
        with patch('src.db_tables.validation_result_tbl.logging') as mock_logging:
            Summery.add_df_to_tbl(summery_df, engine_fixture)  # Methode ausführen
            mock_logging.info.assert_called_once()  # Überprüfen der Erfolgsnachricht
                
        # Überprüfen, ob die Daten korrekt angefügt wurden
        inserted_data = db_session.query(Summery).all()
        # Überprüfen der Anzahl der eingefügten Zeilen
        assert len(inserted_data) == len(summery_df)

        # Laden der Daten aus der Datenbanktabelle in einen DataFrame
        df = pd.read_sql_query(db_session.query(Summery).statement, con=db_session.bind)

        # Erwartete Spaltennamen aus dem SQLAlchemy Modell extrahieren
        expected_columns = [column.name for column in Summery.__table__.columns]

        # Vergleichen der Spaltennamen des DataFrame mit den erwarteten Spaltennamen
        assert set(df.columns) == set(expected_columns), "Die Spaltennamen stimmen nicht überein."
        
        # Stichprobe ob 0, best_ideal_col = y36 ist.
        assert df.at[0, 'Nummer der Idealen Funktion'] == 'y11'

    def test_add_df_to_tbl__fail(self, engine_fixture, sample_dataframes):
        '''
        Die Testmethode, überprüft den Fehler beim
        Anfügen eines falschen Dataframes

        Methodenparameter:
        - db_session: pytest fixture für die DB Arbeit in Conftest.py
        - engine:fixture: pytest fixture für die verbindung zur DB in Conftest.py
        - sample_dataframes: pytest fixture der Beispieldaten in Conftest.py
        '''
        
        # Laden Dataframes
        train_df, ideal_df, test_df = sample_dataframes  
    
        with patch('src.db_tables.ideal_tbl.logging') as mock_logging, pytest.raises(Exception):
            Ideal.add_df_to_tbl(train_df, engine_fixture)
            # Überprüfen, ob die Fehlermeldung protokolliert wurde
            mock_logging.error.assert_called_once()  

        with patch('src.db_tables.train_tbl.logging') as mock_logging, pytest.raises(Exception):
            Train.add_df_to_tbl(ideal_df, engine_fixture)
            # Überprüfen, ob die Fehlermeldung protokolliert wurde
            mock_logging.error.assert_called_once()  

        with patch('src.db_tables.exp_tbl.logging') as mock_logging, pytest.raises(Exception):
            Test.add_df_to_tbl(train_df, engine_fixture)
            # Überprüfen, ob die Fehlermeldung protokolliert wurde
            mock_logging.error.assert_called_once()  
