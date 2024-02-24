import pytest
from src.data_loading import DataLoader
from src.math_logic import Mathematics
import pandas as pd


'''
Dieser Test soll die Minimierung der Summe der quadratische y-Abweichung testen. 
Auch bekannt als mean_squared_error(mse) 
'''

def test_calculate_min_mse():
    '''
    Diese Methode soll testen, ob die Beispieldatensäte mit dem mse-Verfahren verechnet werden können. 

    '''

    train_loader = DataLoader("data/example_data/train.csv")  # Loader für die train.csv
    ideal_loader = DataLoader("data/example_data/ideal.csv")  # Loader für die ideal.csv

    train = train_loader.load_data()  # Speichern der Trainingsdaten als dataframe
    ideal = ideal_loader.load_data()  # Speichern der Idealfunktionen als dataframe
    min_mse = Mathematics()
    result = min_mse.calculate_min_mse(train, ideal)

    assert type(result) == pd.DataFrame
    assert result is not None