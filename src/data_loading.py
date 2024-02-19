import pandas as pd
import os
from src.status_messages import Messages

class DataLoader:
    ''' 
    Diese Klasse enhält Methoden für:
    - das Auswählen der Datei über den Pfad
    - das Lesen der Daten aus der CSV-Datei
    '''
    def __init__(self, file_path):
        '''
        Der Konstruktor legt den Pfad der CSV-Datei fest. 
        Hier wird zudem sicher gestellt, dass die Datei existiert vom Typ CSV ist.

        Methodenparameter:
        - self
        - file_path
        '''
        # Sollte die Datei nicht existieren, wird eine FileNotFoundError geworfen.
        if not os.path.exists(file_path):
            # raised den FileNotFoundError mit eigener Nachricht.
            raise FileNotFoundError(Messages.file_not_found_msg(file_path=file_path))

        # Sollte die Datei nicht auf .csv oder .CSV enden, dann wird ein TypeError geworfen.
        elif not file_path[-4:].lower() == ".csv":
            # wirft den TypeError mit eigener Nachricht
            raise TypeError(Messages.file_wrong_type_msg(file_path=file_path))
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

    def validate_csv_format(self, df):
        '''
        Diese Methode ist für die Validierung des Formats der aus den CSVs erstellten Dataframes zuständig.
        Es wird überprüft ob die Daten dem Format der Trainigs, Ideal oder Testdaten entsprechen. 
        Die erlaubten Spalten sind in diesen Sets hart einprogrammiert, da laut Aufgabenstellung nur solche Daten zu erwarten sind.
        
        Die Validierung ist optional, da das Programm auch mit anderen Formaten arbeiten könnte.
        Wichtig ist nur, dass die x-Werte in der esten Spalte stehen.

        Ist das Format nicht das der Beispieldatensätze, so wird ein ValueError mit eigener Nachricht übergeben.
        
        Methodenparameter:
        - self
        - df: Dataframe, dass durch das Programm verwendet werden soll
        '''

        # Sets der erlaubten Spalten        
        valid_columns_lists = [
            ['x', 'y'],  # Format der Testdaten
            ['x', 'y1', 'y2', 'y3', 'y4'],  # Format der Trainingsdaten
            ['x'] + [f'y{i}' for i in range(1, 51)]  # Format der idealen Funktionen
        ]
        # Aus dem Dataframe werden die Spalten als Listen mit den erlaubten Spalten verglichen.
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