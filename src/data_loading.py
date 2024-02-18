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

        # Sollte die Datei nicht auf .csv enden, dann wird ein TypeError geworfen.
        elif not file_path[-4:] == ".csv":
            # wirft den TypeError mit eigener Nachricht
            raise TypeError(f"Die Datei {file_path} ist nicht vom Typ .csv")
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
        - df: Dataframe, dass durch das Programm verwendet werden soll
        '''

        # Sets der erlaubten Spalten        
        valid_columns_lists = [
            ['x', 'y'],  # Format der Testdaten
            ['x', 'y1', 'y2', 'y3', 'y4'],  # Format der Trainingsdaten
            ['x'] + [f'y{i}' for i in range(1, 51)]  # Format der idealen Funktionen
        ]
        if not any(df.columns.tolist() == valid_columns for valid_columns in valid_columns_lists):
            raise ValueError("Die CSV-Datei hat nicht das richtige Format.")