import numpy as np
import pandas as pd
import math
import logging
from src.status_messages import Messages

class Mathematics:
    '''
    Diese Klasse enhält alle mathematischen und logischen Operationen für das Projekt.
    Diese sind in statischen Methoden implementiert.

    Methoden:
    - calculate_mse: 
        Berechnet den Mean Squared Error zwischen zwei Zahlen,
        gibt einen float Wert als Ergebnis zurück.

    - calculate_min_mse: 
        Wendet calculate_mse auf zwei Dataframe an und 
        gibt ein Ergebnis-Dataframe zurück.
    
    - point_comparison: 
        Stellt fest ob zwei Punkte um mehr als Facktor von sqrt(2) auseinander liegen,
        gibt ein boolschen Wert als Ergebnis zurück.

    - validate_dfs: 
        Validiert die Selektion der idealen Funktionen mit Testdaten.
        Vergleich die Testdaten mit den durch das Training erhaltentenen vier Idealen Funktionen,
        nutzt dazu den absoluten Abstand und die Methode point_comparison. 
        Gibt ein Ergebnis Dataframe zurück.

    - create_summary_df: 
        Erzeugt aus dem Ergebnis Dataframe von validate_dfs 
        eine Zusammenfassung für die Speicherung.
        Gibt eine Ergebnis Dataframe zurück.
    '''

    def __init__(self):
        '''Konstruktor'''
        pass
        
    
    @staticmethod  # statische Methode da die Funktion der mse berechung isoliert ausgeführt wird.
    def calculate_mse(actual, predicted):
        """
        Berechnet den Mean Squared Error
        
        Methodenparameter:
        - actual: int oder float, tatsachlicher Wert
        
        - predicted: int oder float, voraussichtlicher Wert
        
        Rückgabewert:
        - result: float, Mean Squared Error
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
    def point_comparison(y_punkt, y_ideal):
        '''
        Diese Methode führt einen Punktvergleich durch mit zwei Punkten durch. Wenn gilt:
        (y_punkt-y_ideal)**2 < sqr(2)*y_punkt**2 , dann wird True zurückgegeben. 

        Methodenparameter:
        - y_punkt: int oder float, 1. y-Wert
        - y_ideal: int oder float, 2. y-Wert

        Rückgabewert:
        - result: boolean
        '''    
        try:
            result = (y_punkt-y_ideal)**2 < math.sqrt(2)*y_punkt**2
            # logging.info(Messages.VALIDATED_SELECTION.value)
            return result
        except Exception as e:
            logging.error(Messages.ERROR_VALIDATED_SELECTION.value.format(error=e))
            raise

    @staticmethod
    def validate_dfs(mse_df, ideal_df, test_df):
        """
        Diese Methode validiert die Selektion der Idealen Funktionen mit den Testdaten.
        Sie erzeugt ein DataFrame aus den validierten Daten.

        Methodenparameter:
        - mse_df: DataFrame, Ergebniss von calculate_min_mse() generiert wird
        - ideal_df: DataFrame der idealen Funktionen
        - test_df: DataFrame der Testdaten

        Rückgabewert:
        - result_df: Neues DataFrame mit den Spalten 
            x, y, y_ideal1, y_ideal2, y_ideal3, y_ideal4, best_ideal, min_Abweichung
        """
        logging.info(
            f'mse_df: {mse_df}\
            ideal_df: {ideal_df}\
            test_df: {test_df}'
        )
        # Die Namen der viel Idealen Funktionen aus dem mse Ergebniss extrahieren
        ideal_funktion_names = mse_df['best_ideal_col'].unique()
        logging.info(
            f'ideal_funktion_names: {ideal_funktion_names}'
        )

        # ideal_df filtern, so dass nur noch die vier idealen Funktionen behalten werden
        filtered_ideal_df = ideal_df[['x'] + list(ideal_funktion_names)]
        logging.info(
            f'filtered_ideal_df: {filtered_ideal_df}'
        )        
        # verbinden von Test_df und den entsprechenden x Werten aus fitered_ideal_df 
        result_df = pd.merge(test_df, filtered_ideal_df[filtered_ideal_df['x'].isin(test_df['x'])], how='left', on='x')
        logging.info(
            f'result_df: {result_df}'
        )        
        # Initialisiere neue Spalten für das Ergebnis-DataFrame
        result_df['best_ideal'] = None
        result_df['min_Abweichung'] = float('inf')
        logging.info(
            f'result_df: {result_df}'
        ) 
        # Durch die Zeilen des resultierenden DataFrames iterieren
        for index, row in result_df.iterrows():
            x_test = row['x']
            y_test = row['y']

            min_deviation = float('inf')  # Unendlich da der Vergleich sehr hoch beginnt
            best_ideal = None  # Wenn keine Ideale Funktion gefunden werden sollte, None
            
            # Durch die vier idealen Funktionen iterieren
            for ideal_name in ideal_funktion_names:
                y_ideal = row[ideal_name]
                deviation = abs(y_test - y_ideal)  # Abweichung, absoluter Abstand, berechnen
                # Bedingung der Aufgabe durch die Methode point_coparison überprüfen
                islessthanfactor2 = Mathematics.point_comparison(y_test, y_ideal)

                # Prüfen, ob der minimale Abstand größer als der aktuelle Abstand ist.
                if deviation < min_deviation:
                    min_deviation = deviation  # Wenn erfüllt, neuer minimaler Abstand
                    
                    # Prüfen ob die Bedingung islessthanfactor2 erfüllt ist
                    if islessthanfactor2 == True:
                        best_ideal = ideal_name  # Wenn erfüllt, dann ideale Funktion zuweisen.
                    
            # Aktualisiere die Werte für best_ideal und min_Abweichung für die aktuelle Zeile
            result_df.at[index, 'best_ideal'] = best_ideal
            result_df.at[index, 'min_Abweichung'] = min_deviation
            result_df.sort_values('x', inplace=True)
        try:
            result_str = result_df.to_string()  # Logging Vorbereitung um beim Test das Ergebniss vollständig zu sehen.
            logging.info(f'Die Selektion wurde validiert: \n{result_str}')
            return result_df
        except Exception as e:
            logging.error(Messages.ERROR_VALIDATED_SELECTION.value.format(error=e))
            raise

@staticmethod
def create_summary_df(validated_df):
    """
    Diese Methode erzeugt ein zusammenfassendes DataFrame aus den validierten Daten.

    Methodenparameter:
    - validated_df: 
        DataFrame, das die validierten Testdaten enthält.
    
    Rückgabewert:
    - summary_df: 
        Neues DataFrame mit den Spalten X (Test Funktion), 
        Y1 (Test Funktion), Delta Y (Abweichung), 
        Nummer der Idealen Funktion.
    """

    # 'validated_df' enthält unter anderem die Spalten ['x', 'y', 'best_ideal', 'min_Abweichung']
    # Diese sollen in das neue Dataframe integriert werden
    # Erstellung eines neuen DataFrames mit den notwendigen Spalten
    summary_df = validated_df[['x', 'y', 'min_Abweichung', 'best_ideal']].copy()

    # Neues zusammenfassenden Dataframe mit den umbenannten Spalten.
    summary_df.columns = ['X (Test Funktion)', 'Y1 (Test Funktion)', 'Delta Y (Abweichung)', 'Nummer der Idealen Funktion']

    return summary_df          

