from src.data_loading import DataLoader
from database.engine import get_engine
from sqlalchemy.orm import sessionmaker
from src.train_tbl import Train
from src.ideal_tbl import Ideal
from src.exp_tbl import Test
from src.mse_results_tbl import Result
from src.validation_result_tbl import Summery
from src.base_tbl import Base
from src.math_logic import Mathematics
from src.visualisation import Visualisierung
import tkinter as tk
from tkinter import filedialog
import logging

def select_file():
    root = tk.Tk()
    root.withdraw()  # keine Gui Fenster, daher direkt wieder geschlossen
    file_path = filedialog.askopenfilename()  # Öffnet den Dialig zur Dateiauswahl
    return file_path
 
def main():
    '''
    Dies ist die Hauptmethode für das Ausführen des Programms. Über User Input werden die 
    Parameter
    '''
    logging.basicConfig(level=logging.INFO)
    print("Programmstart")
    
    # Festlegen der csv Dateien durch User input
    print("Wählen sie die Trainingsdaten. ")
    train_data_path = select_file()
    print("Wählen sie die Daten der idealen Funktionen. ")
    ideal_data_path = select_file()
    print("Wählen sie die Testdaten. ")
    test_data_path =  select_file()
    
    # Loader Instanzen je csv Datei
    train_loader = DataLoader(train_data_path)  # Loader für die train.csv
    ideal_loader = DataLoader(ideal_data_path)  # Loader für die ideal.csv
    test_loader = DataLoader(test_data_path)  # Loader für die test.csv
    
    # Laden der Daten als Dataframe
    train_df = train_loader.load_data()  # Trainingsdaten als Dataframe
    ideal_df = ideal_loader.load_data()  # Idealfunktionen als Dataframe
    test_df = test_loader.load_data()  # Testdaten als Dataframe
    print("Daten wurden geladen")

    # Verarbeitung der Daten
    # Durchführen der Mean Squared Error Berechnung
    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
    print("Mean squared Error wurde berechnet")

    # Durchführen der Validierung der Testdaten.
    result_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)
    print("Die Validierung der Selektion wurde durchgeführt")

    # Festlegen des Speicherorts der SQLite Datenbank durch User input
    print("Wählen sie die Datenbank")
    db_path = select_file()
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
    visualize = input("Möchten Sie die Ergebnisse visualisieren? (ja/nein): ")
    if visualize.lower() == "ja":
        print("Visualisierung wird durchgeführt...")
        vis = Visualisierung(show_plots=True)
        vis.plot_validation_results(result_df)
    
    print("Programmende")
    
if __name__ == "__main__":
    main()

