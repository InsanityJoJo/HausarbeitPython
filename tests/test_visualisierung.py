import pytest
from src.data_loading import DataLoader
from src.visualisation import Visualisierung


def test_plot_train_data():
    '''
    Diese Methode testet die Visualisierung der Trainingsdaten
    '''
    data_loader = DataLoader('data/example_data/train.csv')
    train_df = data_loader.load_data()
    
    # Aufruf der Visualiserung und der Methode zum Plotten
    visualisierung = Visualisierung()
    visualisierung.plot_train_data(train_df, 'x')

    assert True

def test_plot_ideal_funktions():
    '''
    Diese Methode testet die Visualisierung der idealen Funktionen
    '''
    data_loader = DataLoader('data/example_data/ideal.csv')
    ideal_df = data_loader.load_data()
    
    # Aufruf der Visualiserung und der Methode zum Plotten
    visualisierung = Visualisierung()
    visualisierung.plot_ideal_funktions(ideal_df, 'x')

    assert True

def test_plot_test_data():
    '''
    Diese Methode testet die Visualisierung der Testdaten
    '''
    data_loader = DataLoader('data/example_data/test.csv')
    ideal_df = data_loader.load_data()
    
    # Aufruf der Visualiserung und der Methode zum Plotten
    visualisierung = Visualisierung()
    visualisierung.plot_test_data(ideal_df, 'x')

    assert True  