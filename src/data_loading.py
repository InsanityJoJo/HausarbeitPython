import pandas as pd
import os

class DataLoader:
    ''' 
    Diese Klasse enhält Methoden für:
    - das Auswählen der Datei über den Pfad
    - das Lesen der Daten aus der CSV-Datei
    '''
    def __init__(self, file_path):
        '''
        Diese Methode legt den Pfad der CSV-Datei fest. Sie stellt sicher, dass die Datei existiert.

        Methodenparameter:
        - self
        - file_path
        '''
        # Sollte die Datei nicht existieren, wird eine FileNotFoundError geworfen.
        if not os.path.exists(file_path):
            # raised den FileNotFoundError mit eigener Nachricht.
            raise FileNotFoundError(f"Die Datei {file_path} konnte nicht gefunden werden")
            
        else:
            
            self.file_path = file_path

    def load_data(self):
        '''
        Diese Methode ermöglicht das lesen der CSV-Datei.
        Methodenparameter:
        - self
        
        Rückgabewert:
        - Dataframe aus den Daten der CSV-Datei
        '''


        return pd.read_csv(self.file_path)

