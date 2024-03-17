import pandas as pd
import os
from src.status_messages import Messages
import logging

class DataLoader:
    ''' 
    Diese Klasse enhält Methoden für:
    
    Methoden:
    - load_data() Liest eine CVS Datei und gibt ein Dataframe zurück
    - validate_cvs_format() Validiert das Format der CSV Datei
  
    '''
    def __init__(self, file_path):
        '''
        Dem Konstruktor wird der Pfad der CSV-Datei übergeben. 
        Wenn die Datei nicht existiert wird ein FileNotFoundError
        geworfen. 
        Der Konstruktor stellt sicher, dass mit dem Pfad
        eine .csv oder .CSV Datei übergeben wird.

        Methodenparameter:
        - file_path
        '''
        # Sollte die Datei nicht existieren, wird eine FileNotFoundError geworfen.
        if not os.path.exists(file_path):
            # wirft den FileNotFoundError mit eigener Nachricht.
            raise FileNotFoundError(Messages.FILE_NOT_FOUND.value.format(file_path=file_path))

        # Sollte die Datei nicht auf .csv oder .CSV enden, dann wird ein TypeError geworfen.
        elif not file_path[-4:].lower() == ".csv":
            # wirft den TypeError mit eigener Nachricht
            raise TypeError(Messages.FILE_WRONG_TYPE.value.format(file_path=file_path))
        else:
            self.file_path = file_path

    def load_data(self):
        '''
        Diese Methode liest die im Dateipfad über den Konstruktor
        übergebene CSV-Datei. Sie wandelt den Inhalt der Datei in 
        ein Pandas Dataframe und gibt dieses zurück. Wenn es zum 
        Fehler kommt wird dieser mit einer eingenen Nachricht zurückgegeben.
                
        Rückgabewert:
        - Dataframe aus den Daten der CSV-Datei
        '''
        try:
            # Inhalte aus csv in Dataframe laden.
            df = pd.read_csv(self.file_path)
            logging.info(Messages.FILE_LOADED.value.format(file_path=self.file_path))
            return df
        except Exception as e:
            logging.error(Messages.ERROR_FILE_LOADED.value.format(file_path=self.file_path, error=e))
            raise

    def validate_csv_format(self, df):
        '''
        Diese Methode ist für die Validierung des Formats,
        der aus den CSVs erstellten Dataframes zuständig.
        Es wird überprüft ob die Daten dem Format der Trainigsdaten,
        Idealen Funktionen oder Testdaten entsprechen. 
        Die erlaubten Spalten sind vorgegeben in der Aufgabenstellung 
        und werden daher überprüft.
        
        Ist das Format nicht das der Beispieldatensätze, 
        so wird ein ValueError mit eigener Nachricht übergeben.
        
        Methodenparameter:
        - df: Dataframe, dass durch das Programm verwendet werden soll
        
        Rückgabewert:
        - Rückmeldung als String
        '''

        # Sets der erlaubten Spalten        
        valid_columns_lists = [
            ['x', 'y'],  # Format der Testdaten
            ['x', 'y1', 'y2', 'y3', 'y4'],  # Format der Trainingsdaten
            ['x'] + [f'y{i}' for i in range(1, 51)]  # Format der idealen Funktionen
        ]
        # Aus dem Dataframe werden die Spalten als Listen,
        # mit den erlaubten Spalten verglichen.
        # Listen, weil die Reihenfolge eine Rolle spielt.
        df_columns = df.columns.tolist()
    
        # Überprüfung des Formates der Testdaten.
        if df_columns == valid_columns_lists[0]:
            return Messages.VALID_TEST
        
        # Überprüfung des Formates der Trainingsdaten.
        elif df_columns == valid_columns_lists[1]:
            return Messages.VALID_TRAINING
        
        # Überprüfung des Formates der idealen Funktionen.
        elif df_columns == valid_columns_lists[2]:
            return Messages.VALID_IDEAL
        
        # in allen anderen Fällen wird ein ValueError geworfen.
        else:   
            raise ValueError(Messages.INVALID_CSV_FORMAT.name)
