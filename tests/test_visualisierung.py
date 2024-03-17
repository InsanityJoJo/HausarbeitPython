import pytest
from src.data_loading import DataLoader
from src.visualisation import Visualisierung
from src.math_logic import Mathematics


def test_plot_train_data():
    '''
    Diese Methode testet die Visualisierung der Trainingsdaten
    '''
    # Daten laden   
    data_loader = DataLoader('data/example_data/train.csv')
    train_df = data_loader.load_data()
    
    # Aufruf der Visualiserung und der Methode zum Plotten
    visualisierung = Visualisierung()
    visualisierung.plot_train_data(train_df)

    assert True

def test_plot_ideal_funktions():
    '''
    Diese Methode testet die Visualisierung der idealen Funktionen
    '''
    # Daten laden   
    data_loader = DataLoader('data/example_data/ideal.csv')
    ideal_df = data_loader.load_data()
    
    # Aufruf der Visualiserung und der Methode zum Plotten
    visualisierung = Visualisierung()
    visualisierung.plot_ideal_funktions(ideal_df)

    assert True

def test_plot_test_data():
    '''
    Diese Methode testet die Visualisierung der Testdaten
    '''
    # Daten laden   
    data_loader = DataLoader('data/example_data/test.csv')
    test_df = data_loader.load_data()
    
    # Aufruf der Visualiserung und der Methode zum Plotten
    visualisierung = Visualisierung(show_plots=True)
    visualisierung.plot_test_data(test_df)

    assert True

def test_plot_mse_result():
    '''
    Diese Methode testet die Visualiserung der MSE Berechnung
    '''
    # Daten laden   
    data_loader = DataLoader('data/example_data/train.csv')
    train_df = data_loader.load_data()
    data_loader = DataLoader('data/example_data/ideal.csv')
    ideal_df = data_loader.load_data()

    # Berechnungen durchführen
    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
    visualisierung = Visualisierung()
    visualisierung.plot_mse_result(mse_df, train_df, ideal_df)      

def test_plot_validation_results():
    '''
    Diese Methode testet die Visualisierung des Egebnisses der Validierung
    ''' 

    # Daten laden   
    data_loader = DataLoader('data/example_data/train.csv')
    train_df = data_loader.load_data()
    data_loader = DataLoader('data/example_data/ideal.csv')
    ideal_df = data_loader.load_data()
    data_loader = DataLoader('data/example_data/test.csv')
    test_df = data_loader.load_data()

    # Berechnungen durchführen
    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
    result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)

    # Visualisierung 
    visualisierung = Visualisierung(show_plots=True)
    visualisierung.plot_validation_results(result_df)
