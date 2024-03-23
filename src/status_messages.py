from enum import Enum

class Messages(Enum):
    '''
    Diese Klasse beinhaltet alle Systemnachrichten des Proramms.
    Hier werden Nachrichten angepasst.
    '''
    # Klasse Dataloader
    # Nachricht für den FileNotFoundError des Konstruktors von DataLoader
    FILE_NOT_FOUND = "Die Datei {file_path} konnte nicht gefunden werden."  

    # Nachricht für den TypeError des Konstruktors von DataLoader
    FILE_WRONG_TYPE = "Die Datei {file_path} ist nicht vom Typ .csv"
        
    # Nachricht: validiert richtiges CVS Format für Testdaten
    VALID_TEST = "Die Daten stimmen mit dem Format der Testdaten überein."

    # Nachricht: validiert richtiges CVS Format für Trainingsdaten
    VALID_TRAINING = "Die Daten stimmen mit dem Format der Trainingsdaten überein."
    
    # Nachricht: validiert richtiges CVS Format für Idealdaten
    VALID_IDEAL = "Die Daten stimmen mit dem Format der Idealen Funktionen überein."  
    
    # Nachricht: Fehlermeldung bei falschem CVS Format
    INVALID_CSV_FORMAT = "Die Datei hat das nicht das gewünschte Format.\
        Für Testdaten sind Spaten x, y erlaubt.\
            Für Trainingsdaten sind die Spaten x, y1, ..., y4 erlaubt.\
                Für die idealen Funktionen sind die Spaten x, y1, ..., y50 erlaubt."  
        
    # Logging Nachricht zur Information, wenn die Datei im DataLoader geladen wurde.
    FILE_LOADED = "Datei {file_path} wurde geladen."
    
    # Logging Nachricht zur Information, wenn die Datei im DataLoader geladen wurde.
    ERROR_FILE_LOADED = "Datei {file_path} konnte nicht geladen werden: {error}."


    # Klasse Base
    # Logging Nachricht, wenn die Daten an eine Tabelle angefügt wurden
    DATA_INSERTED = "Daten wurden erfolgreich in die Tabelle {table_name} eingefügt."

    # Logging Error, wenn ein Fehler beim Einfügen der Daten passiert ist
    ERROR_DATA_INSERTED = "Fehler beim Einfügen der Daten in {__tablename__}: {error}"
    
    # Pytest fixture db_session
    # Logging Nachricht, wenn die Testdaten wieder gelöscht wurden. 
    TABLE_DROPPED = "Tabelle wurde im Testfall gelöscht."

    # Logging Error, wenn die Testdaten nicht gelöscht wurden
    ERROR_TABLE_DROPPED = "Fehler beim Löschen der Tabelle der Testdaten: {error}"


    # Klasse Mathematics
    # Logging Nachricht, wenn der Mean Squared Error erfolgreich berechnet wurde.
    MSE_CALCULATED = "Berechnung MSE erfolgreich: {result}"

    # Logging Error, wenn der Mean Squared Error nicht berechnet werden konnte.
    ERROR_MSE_CALCULATED = "Die Berechung des MSE mit {actual} und {predicted} schlug fehl: {error}"
    
    # Logging Nachricht, wenn die Selektion der Idealen Funktionen validiert wurde
    VALIDATED_SELECTION = "Berechnung erfolgreich."

    # Logging Error, wenn ein Fehler bei der Validierung der Selektion vorliegt.
    ERROR_VALIDATED_SELECTION = "Fehler bei der Berechnung: {error}"

    # Logging Nachricht, als Übersicht über die Dataframes die verarbeitet werden sollen.
    DATAFRAME_OVERVIEW = "mse_df: {mse_df}\
            ideal_df: {ideal_df}\
            test_df: {test_df}"

    # Logging Nachricht, Übersicht über die vier idealen Funktionen
    IDEAL_FUNKTION_NAMES = "ideal_funktion_names: {ideal_funktion_names}"

    # Logging Nachricht, Übersicht über das DF mit vier idealen Funktionen
    FILTERED_IDEAL_DF = "filtered_ideal_df: {filtered_ideal_df}"

    # Logging Nachricht, Übersicht result df
    RESULT_DF = "result_df: {result_df}"

    # Logging Nachricht, Übersicht result df String
    RESULT_DF_STRING = "Die Selektion wurde validiert: \n{result_str}"


    # engine get_engine
    # Logging Nachricht wenn due DB neu erstellt wurde.
    DATABASE_CREATED = "Die Datenbank existiert nicht und wird erstellt an der Stelle {db_path}."

    # Logging Nachricht wenn die DB bereits existiert.
    DATABASE_EXISTS = "Verbindung zur bestehenden Datenbank {db_path} hergestellt."

    # Main Methode
    # Nachricht zu Programmstart
    START_PROGRAM = "Programmstart"

    # Nachricht zu Beginn des Logging
    PROGRAM_START = "Start des Programms."

    # Nachrichten für die Auswahl der Daten durch den Benutzer
    SELECT_TRAINING_DATA = "Wählen sie die Trainingsdaten."
    SELECT_IDEAL_FUNCTIONS = "Wählen sie die Daten der idealen Funktionen."
    SELECT_TEST_DATA = "Wählen sie die Testdaten."
    
    # Label des Gui-Elemets für die Auswahl
    PROMPT_TRAINING_DATA = "Auswahl der Trainingsdaten."
    PROMPT_IDEAL_FUNCTIONS = "Auswahl der idealen Funktionen."
    PROMPT_TEST_DATA = "Auswahl der Testdaten."

    # Nachrichten für das Laden der Daten
    DATA_LOADING_STARTS = "Datenladen beginnt"
    DATA_LOADED = "Daten wurden geladen"
    
    # Nachrichten für die Formatsprüfung
    CHECK_TRAINING_DATA_FORMAT = "Überprüfen des Formats der Trainingsdaten..."
    CHECK_IDEAL_FUNCTIONS_FORMAT = "Überprüfen des Formats der idealen Funktionen..."
    CHECK_TEST_DATA_FORMAT = "Überprüfen des Formats der Testdaten..."    

    # Nachricht für MSE-Berechnung
    MSE_CALCULATED_INFO = "Mean squared Error wurde berechnet"
    # Nachricht für Validierung
    VALIDATION_COMPLETED_INFO = "Die Validierung der Selektion wurde durchgeführt"
    
    # Nachrichten für die Datenbankauswahl und das Laden der Daten
    SELECT_DATABASE = "Wählen sie die Datenbank"
    DATA_LOADED_TO_DB = "Die Daten wurden in die Datenbank geladen"

    # Nachricht, wenn die Visualisierung abgeschlossen ist
    VISUALIZATION_COMPLETED = "Visualisierung abgeschlossen"
    
    # Nachrichten zum Ende des Programms
    PROGRAM_END_RESULTS = "Die Ergebnisse sind gespeichert in:\n{db_path}"
    PROGRAM_END_LOG = "Ende des Programms. Gesamtlaufzeit: {duration:.2f} Sekunden"
    PROGRAM_END = "Programmende"