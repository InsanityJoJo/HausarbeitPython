import numpy as np
import pandas as pd
import math
import logging
from src.status_messages import Messages

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
        try: 
            result = ((actual - predicted) ** 2).mean()
            return result
        except Exception as e:
            logging.error(Messages.ERROR_MSE_CALCULATED.value.format(actual=actual, predicted=predicted, error=e))
            raise

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
            best_ideal_col = None
            # hier wird über die y-Spalten im Ideal-Datensatz iterriert.
            # Auch hier wird die x-Spalte mit [1:] übersprungen.
            for y_ideal_col in ideal.columns[1:]:

                # berechnen des MSE auf der aktuellen y Spalte von Trainigs und Ideal Datensatz
                mse = Mathematics.calculate_mse(train[y_train_col], ideal[y_ideal_col])
                
                if mse < min_mse:
                    min_mse = mse
                    best_ideal_col = y_ideal_col
            
            results.append({'y_train_col': y_train_col, 'best_ideal_col': best_ideal_col, 'min_mse': min_mse})
        try:
            results_df = pd.DataFrame(results)
            logging.info(Messages.MSE_CALCULATED.value.format(result=results_df))
            return results_df
        except Exception as e:
            logging.error(Messages.ERROR_MSE_CALCULATED.value.format(actual=train, predicted=ideal, error=e))
            raise

    @staticmethod
    def validate_selection(y_punkt, y_ideal):
        '''
        Diese Methode sorgt für die Berechung der Validierung der Selektion 
        von Ausgewählten Idealen Funktionen mit einem Punkvergleich der Testdaten.
        Punktvergleich (y_punkt-y_ideal)**2 < sqr(2)*y_punkt**2 
        '''    
        try:
            result = (y_punkt-y_ideal)**2 < math.sqrt(2)*y_punkt**2
            logging.info(Messages.VALIDATED_SELECTION.value)
            return result
        except Exception as e:
            logging.error(Messages.ERROR_VALIDATED_SELECTION.value.format(error=e))
            raise