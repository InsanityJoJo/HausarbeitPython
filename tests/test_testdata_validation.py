import pytest
import pandas as pd
from src.data_loading import DataLoader
from src.math_logic import Mathematics

def test_testdata_valid():

    train_loader = DataLoader("data/example_data/train.csv")  # Loader für die train.csv
    ideal_loader = DataLoader("data/example_data/ideal.csv")  # Loader für die ideal.csv
    test_loader = DataLoader("data/example_data/test.csv")  # Loader für die test.csv

    train_df = train_loader.load_data()  # Speichern der Trainingsdaten als Dataframe
    ideal_df = ideal_loader.load_data()  # Speichern der Idealfunktionen als Dataframe
    test_df = test_loader.load_data()  # Speichern der Testdaten als Dataframe
    
    # Check ob das df Daten enthält.
    assert train_df is not None
    # Check ob das df Daten enthält.
    assert ideal_df is not None
    # Check ob das df Daten enthält.
    assert test_df is not None

    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)

    result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)

    assert result_df is not None