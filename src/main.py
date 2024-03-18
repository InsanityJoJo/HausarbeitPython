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
from src.gui_elemets import Gui
import logging
import time
import warnings

def main():
    '''
    Dies ist die Hauptmethode für das Ausführen des Programms. Über User Input werden die 
    Parameter
    '''
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
    logging.info("Start des Programms.")  
    start_time = time.time()  # Zeit zu beginn des Programms
    print("Programmstart")
    print(" ")
    # Festlegen der csv Dateien durch User input
    print("Wählen sie die Trainingsdaten.")
    train_data_path = Gui.select_file("Auswahl der Trainingsdaten.")
    print("Wählen sie die Daten der idealen Funktionen.")
    ideal_data_path = Gui.select_file("Auswahl der idealen Funktionen.")
    print("Wählen sie die Testdaten.")
    test_data_path =  Gui.select_file("Auswahl der Testdaten.")
    
    # Loader Instanzen je csv Datei
    logging.info("Datenladen beginnt")
    train_loader = DataLoader(train_data_path)  # Loader für die train.csv
    ideal_loader = DataLoader(ideal_data_path)  # Loader für die ideal.csv
    test_loader = DataLoader(test_data_path)  # Loader für die test.csv
    

    # Laden der Daten als Dataframe
    train_df = train_loader.load_data()  # Trainingsdaten als Dataframe
    ideal_df = ideal_loader.load_data()  # Idealfunktionen als Dataframe
    test_df = test_loader.load_data()  # Testdaten als Dataframe
    print("Daten wurden geladen")
    print(" ")
    print("Überprüfen des Formats der Trainingsdaten...")
    print(train_loader.validate_csv_format(train_df).value)
    print(" ")
    print("Überprüfen des Formats der idealen Funktionen...")
    print(ideal_loader.validate_csv_format(ideal_df).value)
    print(" ")
    print("Überprüfen des Formats der Testdaten...")
    print(test_loader.validate_csv_format(test_df).value)
    print(" ")
    # Verarbeitung der Daten
    # Durchführen der Mean Squared Error Berechnung
    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
    print("Mean squared Error wurde berechnet")
    
    # Durchführen der Validierung der Testdaten.
    result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)
    print("Die Validierung der Selektion wurde durchgeführt")
    print(" ")

    # Festlegen des Speicherorts der SQLite Datenbank durch User input
    print("Wählen sie die Datenbank")
    db_path = Gui.select_file("Wählen sie die Datenbank")
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
        Summery.add_df_to_tbl(result_df, engine)  # summery_df an Tabelle Summery anfügen
        
        session.commit()  # Speichern
        print("Die Daten wurden in die Datenbank geladen")
    except:
        # Bei Fehlern Änderungen zurücknehmen
        session.rollback()
        raise
    
    finally:
        # Session schließen
        session.close()    
   
    # Optionale Visualisierung
    if Gui.ask_user("Visualisierung", "Möchten Sie eine detailierte Visualisierung aller Programmphasen?"):
        print("Visualisierung wird durchgeführt...")
        vis = Visualisierung(show_plots=True)
        vis.plot_train_data(train_df)
        vis.plot_ideal_funktions(ideal_df)
        vis.plot_test_data(test_df)
        vis.plot_mse_result(mse_df, train_df, ideal_df)
        vis.plot_validation_results(result_df)    
    
    elif Gui.ask_user("Visualisierung der Ergebnisse","Möchten Sie nur die Ergebnisse visualisieren?"):
        print("Visualisierung wird durchgeführt...")
        vis = Visualisierung(show_plots=True)
        vis.plot_validation_results(result_df)
    
    Gui.end_message("Programmende", f"Die Erbenisse sind gespeichert in:\n{db_path}")
    end_time = time.time()  # Zeit zum Ende des Programms
    logging.info(f"Ende des Programms. Gesammtlaufzeit: {end_time - start_time:.2f} Sekunden")
    print("Programmende")
    
if __name__ == "__main__":
    main()

