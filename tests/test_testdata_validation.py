import pytest
import pandas as pd
from src.data_loading import DataLoader
from src.math_logic import Mathematics
from src.visualisation import Visualisierung

def test_testdata_valid():

    train_loader = DataLoader("data/example_data/train.csv")  # Loader für die train.csv
    ideal_loader = DataLoader("data/example_data/ideal.csv")  # Loader für die ideal.csv
    test_loader = DataLoader("data/example_data/test.csv")  # Loader für die test.csv

    train_df = train_loader.load_data()  # Speichern der Trainingsdaten als Dataframe
    ideal_df = ideal_loader.load_data()  # Speichern der Idealfunktionen als Dataframe
    test_df = test_loader.load_data()  # Speichern der Testdaten als Dataframe
    
    # Check ob die Dfs existiert
    assert train_df is not None
    assert ideal_df is not None
    assert test_df is not None

    # Berechung des mse_df
    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
    # Check ob mse_df existiert
    assert mse_df is not None
    
    result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)
    
    # Überprüfen, ob result_df ein DataFrame ist
    assert isinstance(result_df, pd.DataFrame), "result_df ist kein DataFrame"
    
    # Überprüfen, ob result_df nicht leer ist
    assert not result_df.empty, "result_df ist leer"
    assert result_df is not None
    
    assert type(result_df) is pd.DataFrame
    
    # Überprüfen, ob bestimmte Spalten in result_df vorhanden sind
    erwartete_spalten = ['x', 'y', 'best_ideal', 'min_Abweichung']
    for spalte in erwartete_spalten:
        assert spalte in result_df.columns, f"Spalte '{spalte}' fehlt in result_df"

    # Überprüfen, ob alle Werte in der Spalte 'min_Abweichung' >= 0 sind
    assert (result_df['min_Abweichung'] >= 0).all(), "Negative Werte in 'min_Abweichung' gefunden"


    # Visualisierung der Daten.
    # vis = Visualisierung()
    # vis.plot_train_data(train_df)
    # vis.plot_ideal_funktions(ideal_df)
    # vis.plot_test_data(test_df)
    # vis.plot_mse_result(mse_df, train_df, ideal_df)
    # vis.plot_validation_results(result_df)



