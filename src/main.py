from src.data_loading import DataLoader
from database.engine import get_engine
from sqlalchemy.orm import sessionmaker
from src.db_tables.train_tbl import Train
from src.db_tables.ideal_tbl import Ideal
from src.db_tables.exp_tbl import Test
from src.db_tables.mse_results_tbl import Result
from src.db_tables.validation_result_tbl import Summery
from src.db_tables.base_tbl import Base
from src.math_logic import Mathematics
from src.visualisation import Visualisierung
from src.gui_elements import Gui
from src.status_messages import Messages
import logging
import time
import warnings
import sys

class ProgramState:
    def __init__(self):
        self.visualisations_completed = False

def main():
    '''
    Dies ist die Hauptmethode um das Programm auszuführen.

    Anpassungen:
    Der Logging-Level ist auf "WARN" gesetzt.
    Zu Informations- und Debuggin-Zwecken kann der Logging-Level auf INFO
    gesetzt werden. Das Programm loggt alle wesentlichen Schritte und Daten, 
    so dass eine Überprüfung durch den Benutzer in der Konsole möglich ist.

    Es werden Warnungen gefiltert, die das Seaborn-Paket betreffen. 
    Auch dies ist optional.
    
    Ablauf:
    Zu Beginn wird der ProgramState initialisiert
    Über diesen wird kontrolliert die Visualisierung
    abgeschlossen wurde.
    
    Nach der Statnachricht werden über User Input die CSV-Dateien
    übergeben. Anschließend wird das Format der Dateien validiert.

    Anschließend erfolgt die Berechnung von Mean-Squared-Error und
    der Validierung der Selektion.

    Durch User Input wird nun die Datenbank festgelegt, in der die
    Tabellen erstellt werden. 

    Die Verbindung zur Datenbank wird erstellt
    Eine Session wird geöffnet.
    Die Tabellen werden geladen und die Dataframes werden angefügt.
    Bei einem Fehler werden die Änderungen zurückgerollt.
    Fehler oder nicht, am Ende der Operationen wird die Session geschlossen.

    Die optionale Visualisierung wird durch ein einfach Gui-Fester ermöglicht.
    Je nach Wunsch des Users können Plots zu Trainingsdaten, Idealen Funktionen,
    Testdaten, MSE-Berechnung und die Ergebnisse der Validierung der Selektion
    ausgewählt werden. 
    Mit dem Button "Beenden" wird state auf True gesetzt
    und es wird der Enddialog mit dem Speicherort der Datenbank angezeigt.


    '''
    # Initialisiere den Zustand des Programms
    state = ProgramState()

    # Logging und Warnungen anpassen
    # Logging lvl kann hier angepasst werden
    # Zum Debugging werde alle Funktionen
    # umfangreich auf logging lvl INFO geloggt
    # Dafür bitte hier ändern.
    logging.basicConfig(level=logging.WARN)
    # Logging sqlalchemy anpassen
    logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)
    # warnungen filtern
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)

    # Logging info zum Start des Programms
    logging.info(Messages.PROGRAM_START.value)
    start_time = time.time()  # Zeit zu beginn des Programms
    print(Messages.START_PROGRAM.value)
    print(" ")

    # Festlegen der csv Dateien durch User input
    print(Messages.SELECT_TRAINING_DATA.value)
    train_data_path = Gui.select_file(Messages.PROMPT_TRAINING_DATA.value)
    print(Messages.SELECT_IDEAL_FUNCTIONS.value)
    ideal_data_path = Gui.select_file(Messages.PROMPT_IDEAL_FUNCTIONS.value)
    print(Messages.SELECT_TEST_DATA.value)
    test_data_path = Gui.select_file(Messages.PROMPT_TEST_DATA.value)
    
    # Loader Instanzen je csv Datei
    logging.info(Messages.DATA_LOADING_STARTS.value)
    train_loader = DataLoader(train_data_path)  # Loader für die train.csv
    ideal_loader = DataLoader(ideal_data_path)  # Loader für die ideal.csv
    test_loader = DataLoader(test_data_path)  # Loader für die test.csv
    
    # Laden der Daten als Dataframe
    train_df = train_loader.load_data()  # Trainingsdaten als Dataframe
    ideal_df = ideal_loader.load_data()  # Idealfunktionen als Dataframe
    test_df = test_loader.load_data()  # Testdaten als Dataframe
    print(Messages.DATA_LOADED.value)
    print(" ")
    print(Messages.CHECK_TRAINING_DATA_FORMAT.value)
    print(train_loader.validate_csv_format(train_df).value)
    print(" ")
    print(Messages.CHECK_IDEAL_FUNCTIONS_FORMAT.value)
    print(ideal_loader.validate_csv_format(ideal_df).value)
    print(" ")
    print(Messages.CHECK_TEST_DATA_FORMAT.value)
    print(test_loader.validate_csv_format(test_df).value)
    print(" ")
    # Verarbeitung der Daten
    # Durchführen der Mean Squared Error Berechnung
    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
    print(Messages.MSE_CALCULATED_INFO.value)
    
    # Durchführen der Validierung der Testdaten.
    result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)
    print(Messages.VALIDATION_COMPLETED_INFO.value)
    print(" ")

    # Festlegen des Speicherorts der SQLite Datenbank durch User input
    print(Messages.SELECT_DATABASE.value)
    db_path = Gui.select_file(Messages.SELECT_DATABASE.value)
    engine = get_engine(db_path)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Erstellen der Tabellen und anfügend der geladenen Daten
        Train.add_df_to_tbl(train_df, engine)  # train_df an Tabelle Train anfügen
        Ideal.add_df_to_tbl(ideal_df, engine)  # ideal_df anTabelle Ideal anfügen
        Test.add_df_to_tbl(test_df, engine)  # test_df an Tabelle Test anfügen
        Result.add_df_to_tbl(mse_df, engine)  # mse_df an Tabelle Result anfügen
        Summery.add_df_to_tbl(result_df, engine)  # summery_df an Tabelle Summery 
        
        session.commit()  # Speichern
        print(Messages.DATA_LOADED_TO_DB.value)
    except:
        # Bei Fehlern Änderungen zurücknehmen
        session.rollback()
        raise
    
    finally:
        # Session schließen
        session.close()    
   
   
    # Prüfung ob die Visualisierung abgeschlossen ist
    def on_visualisation_closed():
        if state.visualisations_completed:
            print(Messages.VISUALIZATION_COMPLETED.value)
            # Aufruf der Endnachricht des Programms
            Gui.end_message(Messages.PROGRAM_END.value, Messages.PROGRAM_END_RESULTS.value.format(db_path=db_path))
            end_time = time.time()  # Zeit zum Ende des Programms
            # Logging Nachricht zum Ende des Programms
            logging.info(Messages.PROGRAM_END_LOG.value.format(duration=end_time - start_time))
            print(Messages.PROGRAM_END.value)
            sys.exit()

    # Optionale Visualisierung
    vis = Visualisierung(show_plots=True)
    # Aufruf zur Erstellung des Visualisierungsfensters
    Gui.create_visualisation_window(state, vis, train_df, ideal_df, test_df, mse_df, result_df, on_visualisation_closed)   
        
if __name__ == "__main__":
    main()

