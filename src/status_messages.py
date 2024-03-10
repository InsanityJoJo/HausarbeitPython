from enum import Enum, auto

class Messages(Enum):
    '''
    Diese Klasse beinhaltet alle Systemnachrichten des Proramms.
    Hier werden Nachrichten angepasst.
    '''

    # Nachricht für den FileNotFoundError des Konstruktors von DataLoader
    # Aufruf über statische Methode file_not_found_msg, wegen f string.
    FILE_NOT_FOUND = "Die Datei {file_path} konnte nicht gefunden werden"  

    # Nachricht für den TypeError des Konstruktors von DataLoader
    # Aufruf über statische Methode file_wrong_type_msg, wegen f string.
    FILE_WRONG_TYPE = "Die Datei {file_path} ist nicht vom Typ .csv"
    
    
    # Nachricht: validiert richtiges CVS Format für Testdaten
    VALID_TEST = "Die Daten stimmen mit dem Format der Testdaten überein"

    # Nachricht: validiert richtiges CVS Format für Trainingsdaten
    VALID_TRAINING = "Die Daten stimmen mit dem Format der Trainingsdaten überein"
    
    # Nachricht: validiert richtiges CVS Format für Idealdaten
    VALID_IDEAL = "Die Daten stimmen mit dem Format der Idealen Funktionen überein"  
    
    # Nachricht: Fehlermeldung bei falschem CVS Format
    INVALID_CSV_FORMAT = "Die Datei hat das nicht das gewünschte Format.\
        Für Testdaten sind Spaten x, y erlaubt.\
            Für Trainingsdaten sind die Spaten x, y1, ..., y4 erlaubt.\
                Für die idealen Funktionen sind die Spaten x, y1, ..., y50 erlaubt."  
    
    # Logging Nachrichten:
    
    # Logging Nachricht zur Information, wenn die Datei im DataLoader geladen wurde.
    FILE_LOADED = "Datei {file_path} wurde geladen."
    
    # Logging Nachricht zur Information, wenn die Datei im DataLoader geladen wurde.
    ERROR_FILE_LOADED = "Datei {file_path} konnte nicht geladen werden: {error}."

    # Logging Nachricht, wenn die Daten an eine Tabelle angefügt wurden
    DATA_INSERTED = "Daten wurden erfolgreich in die Tabelle {table_name} eingefügt."

    # Logging Error, wenn ein Fehler beim Einfügen der Daten passiert ist
    ERROR_DATA_INSERTED = "Fehler beim Einfügen der Daten in {__tablename__}: {error}"
    
    # Logging Nachricht, wenn die Testdaten wieder gelöscht wurden. 
    TABLE_DROPPED = "Tabelle wurde im Testfall gelöscht."

    # Logging Error, wenn die Testdaten nicht gelöscht wurden
    ERROR_TABLE_DROPPED = "Fehler beim Löschen der Tabelle der Testdaten: {error}"

    # Logging Nachricht, wenn der Mean Squared Error erfolgreich berechnet wurde.
    MSE_CALCULATED = "Berechnung MSE erfolgreich: {result}"

    # Logging Error, wenn der Mean Squared Error nicht berechnet werden konnte.
    ERROR_MSE_CALCULATED = "Die Berechung des MSE mit {actual} und {predicted} schlug fehl: {error}"
    
    # Logging Nachricht, wenn die Selektion der Idealen Funktionen validiert wurde
    VALIDATED_SELECTION = "Berechnung erfolgreich."

    # Logging Error, wenn ein Fehler bei der Validierung der Selektion vorliegt.
    ERROR_VALIDATED_SELECTION = "Fehler bei der Berechnung: {error}"
    
    # Logging Nachricht wenn due DB neu erstellt wurde-
    DATABASE_CREATED = "Die Datenbank existiert nicht und wird erstellt an der Stelle {db_path}."

    # Logging Nachricht wenn die DB bereits existiert.
    DATABASE_EXISTS = "Verbindung zur bestehenden Datenbank {db_path} hergestellt."
    
    @staticmethod
    def file_not_found_msg(file_path):
        '''
        Statische Methode zur Arbeit mit f-Strings der Fehler Nachricht.
        '''
        return Messages.FILE_NOT_FOUND.value.format(file_path=file_path)
    
    @staticmethod
    def file_wrong_type_msg(file_path):
        '''
        Statische Methode zur Arbeit mit f-Strings der Fehler Nachricht.
        '''
        return Messages.FILE_WRONG_TYPE.value.format(file_path=file_path)