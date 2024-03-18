import pytest
from src.data_loading import DataLoader
from src.visualisation import Visualisierung
from src.math_logic import Mathematics

class TestVisualisierung:
    '''
    Diese Klasse ist für das Testen der Visualisierung implementiert.
    Die Tests sind haupsächlich für die Erstellung von TestPlots.
    Die Plots können mit show_plots=True angezeigt werden. 
    Überprüft werden sie durch Augenmerk.

    Testmetoden:
    - test_plot_train_data
    - test_plot_ideal_funktions
    - test_plot_test_data
    - test_plot_mse_result
    - test_plot_validation_results
    '''

    def test_plot_train_data(self):
        '''
        Diese Methode testet die Visualisierung der Trainingsdaten
        '''
        # Daten laden   
        data_loader = DataLoader('data/example_data/train.csv')
        train_df = data_loader.load_data()
        
        # Visualisierung
        visualisierung = Visualisierung()
        visualisierung.plot_train_data(train_df)
        assert True

    def test_plot_ideal_funktions(self):
        '''
        Diese Methode testet die Visualisierung der idealen Funktionen
        '''
        # Daten laden   
        data_loader = DataLoader('data/example_data/ideal.csv')
        ideal_df = data_loader.load_data()
        
        # Visualisierung
        visualisierung = Visualisierung()
        visualisierung.plot_ideal_funktions(ideal_df)
        assert True

    def test_plot_test_data(self):
        '''
        Diese Methode testet die Visualisierung der Testdaten
        '''
        # Daten laden   
        data_loader = DataLoader('data/example_data/test.csv')
        test_df = data_loader.load_data()
        
        # Visualisierung
        visualisierung = Visualisierung()
        visualisierung.plot_test_data(test_df)
        assert True

    def test_plot_mse_result(self):
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
        
        # Visualisierung
        visualisierung = Visualisierung()
        visualisierung.plot_mse_result(mse_df, train_df, ideal_df)      
        assert True


    def test_plot_validation_results(self):
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
        visualisierung = Visualisierung()
        visualisierung.plot_validation_results(result_df)
        assert True