import pytest
import unittest
from unittest.mock import MagicMock
from src.data_loading import DataLoader
from src.math_logic import Mathematics
import pandas as pd
import numpy as np

class TestMathematics(unittest.TestCase):
    '''
    Diese Test-Klasse testet die Methoden der Klasse Mathematics.

    Methoden:
    - test_calculate_mse()
    - test_calculate_mse_with_exception()
    '''
    def test_calculate_mse(self):
        '''
        Diese Methode teste die normale Ausführung von calculate_mse()
        '''
        # Erzeugen von zwei Pandas Series für den Test
        actual_series = pd.Series([1, 2, 3, 4, 5])
        predicted_series = pd.Series([1.1, 1.9, 3.1, 3.9, 5.1])

        # Berechnung des erwarteten Ergebnisses
        expected_result = ((actual_series - predicted_series) ** 2).mean()

        # Aufruf der zu testenden Methode
        result = Mathematics.calculate_mse(actual_series, predicted_series)

        # Check, ob das berechnete Ergebnis mit dem erwarteten Ergebnis übereinstimmt
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_calculate_mse_with_exception(self):
        '''
        Diese Methode teste calculate_mse mit einer Exception.
        Diese soll durch ein fehlerhaftes Sets zu stande kommen.
        '''
        # Erzeugen von zwei Pandas Series, wobei eine davon einen String enthält ist, 
        # um eine Exception zu provozieren
        actual_series = pd.Series([1, 2, 3])
        predicted_series = pd.Series([1.1, 1.9, 'Fehler'])  # Fehlerhafe Series

        # um zu überprüfen, ob dieser im Fehlerfall aufgerufen wird
        # Überprüfen, ob eine Exception geworfen wird
        with unittest.mock.patch('src.math_logic.logging.error') as mocked_logging_error:
            # Erwarten einer Exception, da die Series unterschiedliche Längen haben
            with self.assertRaises(Exception):
                Mathematics.calculate_mse(actual_series, predicted_series)
          

    def test_calculate_min_mse_files(self):
        '''
        Diese Methode soll testen, ob die Beispieldatensäte 
        mit dem mse-Verfahren verechnet werden können. 
        '''
        train_loader = DataLoader("data/example_data/train.csv")  # Loader für die train.csv
        ideal_loader = DataLoader("data/example_data/ideal.csv")  # Loader für die ideal.csv

        train = train_loader.load_data()  # Speichern der Trainingsdaten als dataframe
        ideal = ideal_loader.load_data()  # Speichern der Idealfunktionen als dataframe
        
        result = Mathematics.calculate_min_mse(train, ideal)

        assert type(result) == pd.DataFrame
        assert result is not None

    def test_calculate_min_mse_correct_return(self):
        '''
        Diese Methode testet das Format des Rückgabe dfs
        von calculate_min_mse().
        '''
        train_df = pd.DataFrame({'x': [1, 2], 'y1': [1, 4], 'y2': [2, 3]})
        ideal_df = pd.DataFrame({'x': [1, 2], 'y1': [1, 3], 'y2': [2, 4]})
        result = Mathematics.calculate_min_mse(train_df, ideal_df)
        # Check ob die richtige Spalten erstellt wurden.
        self.assertTrue(all(
            column in result.columns for column in [
                'y_train_col', 'best_ideal_col', 'min_mse']))
    
    def test_calculate_min_mse_empty_dataframes(self):
        '''
        Diese Methode testet das Verhalten mit 
        leeren Dataframes von calculate_min_mse().
        '''
        train_df = pd.DataFrame()
        ideal_df = pd.DataFrame()
        result = Mathematics.calculate_min_mse(train_df, ideal_df)
        # Check, dass hier ein leeres DF als Ergbnis vorliegt
        self.assertEqual(len(result), 0)

    def test_calculate_min_mse_accuracy(self):
        '''
        Diese Methode testet die Genauigkeit der
        Mean-Squared Error Berechnung in
        calculate_min_mse().
        '''
        train_df = pd.DataFrame({'x': [1, 2], 'y1': [3, 5]})
        ideal_df = pd.DataFrame({'x': [1, 2], 'y1': [2, 4], 'y2': [3, 5]})
        result = Mathematics.calculate_min_mse(train_df, ideal_df)
        self.assertTrue((result['best_ideal_col'] == 'y2').all())

    def test_point_comparison_calculation(self):
        '''
        Diese Methode test die richtige Berechnung der
        Bedingung des Punktvergleichs.
        Mit:
        y_punkt=12
        y_ideal=1
        und (y_punkt-y_ideal)**2 < sqr(2)*y_punkt**2
        => (12-1)**2 < sqr(2)*12**2
        = 121 < 203.65
        => True
        '''
        y1=12
        y2=0.1
        y_ideal=1
        # Check ob die Berechnung das erwartete Ergebnis bringt.
        self.assertTrue(Mathematics.point_comparison(y1, y_ideal))
        self.assertFalse(Mathematics.point_comparison(y2, y_ideal))
    
    def test_point_comparison_exception_handling(self):
        '''
        Diese Methode testet die Exception-Handhabung in der point_comparison-Methode,
        wenn nicht-numerische Eingaben übergeben werden.
        '''
        # Überprüfen, ob eine Exception geworfen wird, bei nicht-numerischer Eingabe
        with unittest.mock.patch('src.math_logic.logging.error') as mocked_logging_error:
            with self.assertRaises(Exception):
                Mathematics.point_comparison("keineZahl", 5)
            mocked_logging_error.assert_called()

    def test_validate_dfs_output_format(self):
        '''
        Diese Methode testet das Format Ausgabe der 
        validierten Daten. Hier werden die Spalten überprüft.
        '''
        # Laden der Testdaten in DataFrames
        train_loader = DataLoader("data/example_data/train.csv")
        ideal_loader = DataLoader("data/example_data/ideal.csv")
        test_loader = DataLoader("data/example_data/test.csv")
        train_df = train_loader.load_data()
        ideal_df = ideal_loader.load_data()
        test_df = test_loader.load_data()
        
        # Berechnen vom MSE und result
        mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
        result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)
        # Liste der erwarteten Spalten
        expected_columns = ['x',
                             'y',
                               'y_ideal1',
                                 'y_ideal2',
                                   'y_ideal3',
                                     'y_ideal4',
                                       'best_ideal',
                                         'min_Abweichung'
                                         ]
        # Check ob die Spalten in result_df enthalten sind.
        for column in expected_columns:
            self.assertIn(column, result_df.columns)

    def test_validate_dfs_with_empty_dfs(self):
        '''
        Diese Methode testet die Methode validate_dfs
        mit leeren Dataframes.
        '''
        # Erstellen von leeren DFs.
        mse_df = pd.DataFrame()
        ideal_df = pd.DataFrame()
        test_df = pd.DataFrame()
        # Berechnen von result_df
        result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)
        # Check ob result_df leer ist
        self.assertEqual(len(result_df), 0)

if __name__ == '__main__':

    unittest.main()
