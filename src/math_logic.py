import numpy as np
import pandas as pd


class Mathematics:
    '''
    Diese Klasse enhält alle mathematischen Methoden die für das Projekt nötig sind.
    Sie sind als statische Methoden implementiert.

    Methoden:

    '''

    def __init__(self):
        pass
    
    
    @staticmethod  # statische Methode da die Funktion der mse berechung isoliert ausgeführt wird.
    def calculate_mse(actual, predicted):
        """
        Berechnet den Mean Squared Error
        actual: Zahl
        predicted: Zahl
        return: float
        """
        # Subtrahieren actual - predicted
        # Quadrieren des Ergebnisses
        # 
        return ((actual - predicted) ** 2).mean()
    
    @staticmethod
    def calculate_min_mse(train, ideal):
        """
        Vergleicht Trainingsdaten mit idealen Daten
        und findet die beste Übereinstimmung basierend auf dem MSE.
        Übergabeparameter:
        train: Dataframe aus Trainingsdaten
        ideal: Dataframe aus Idealdaten
        
        Rückgabewert:
        result: Dataframe der Ergebnisse
        """
        # Liste für die Ergebnisse, dass wird später in ein Dataframe umgewaldelt
        results = []
        
        # über die y-Spalten im Trainingsdatensatz iterrieren, 
        # die x-Spalte wird durch [1:] übersprungen
        for y_train_col in train.columns[1:]:

            # Der Minimale MSE beginnt bei unendlich, damit dieser sicher nicht unter dem ersten errechneten MSE liegt.
            min_mse = np.inf

            # Es kann noch keine Ideale Funktion zugeornet werden, daher None.
            best_ideal_index = None
            
            # hier wird über die y-Spalten im Ideal-Datensatz iterriert.
            # Auch hier wird die x-Spalte mit [1:] übersprungen.
            for y_ideal_col in ideal.columns[1:]:

                # berechnen des MSE auf der aktuellen y Spalte von Trainigs und Ideal Datensatz
                mse = Mathematics.calculate_mse(train[y_train_col], ideal[y_ideal_col])
                
                if mse < min_mse:
                    min_mse = mse
                    best_ideal_col = y_ideal_col
            
            results.append({'y_train_col': y_train_col, 'best_ideal_col': best_ideal_col, 'min_mse': min_mse})
        
        return pd.DataFrame(results)

