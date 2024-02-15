import pandas as pd

class DataLoader:
    ''' 
    Diese Klasse läd aus die Daten aus den CSV-Dateien.
    '''
    def __init__(self, file_path):
        '''
        Diese Methode legt den Pfad der CSV-Datei fest
        '''
        self.file_path = file_path
    
    def load_data(self):
        return pd.read_csv(self.file_path)