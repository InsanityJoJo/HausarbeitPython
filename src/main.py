from src.data_loading import DataLoader
from database.engine import get_engine
from src.train_tbl import Train
from src.ideal_tbl import Ideal
from src.exp_tbl import Test
from src.mse_results_tbl import Result
from src.validation_result_tbl import Summery
from src.math_logic import Mathematics
from src.visualisation import Visualisierung

# import logging

# logging.basicConfig(level=logging.INFO)


# Weitere benötigte Importe hier

def main():
    '''
    Dies ist die Hauptmethode für das Ausführen des Programms. Über User Input werden die 
    Parameter
    '''
    print("Programmstart")
    
    # Festlegen der csv Dateien durch User input
    train_data_path = input("Geben Sie den Pfad zur CSV-Datei der Trainingsdaten ein: ")
    ideal_data_path = input("Geben Sie den Pfad zur CSV-Datei der Idealen Funktionen ein: ")
    test_data_path = input("Geben Sie den Pfad zur CSV-Datei der Testdaten ein: ")
    
    # Loader Instanzen je csv Datei
    train_loader = DataLoader(train_data_path)  # Loader für die train.csv
    ideal_loader = DataLoader(ideal_data_path)  # Loader für die ideal.csv
    test_loader = DataLoader(test_data_path)  # Loader für die test.csv

    # Laden der Daten als Dataframe
    train_df = train_loader.load_data()  # Trainingsdaten als Dataframe
    ideal_df = ideal_loader.load_data()  # Idealfunktionen als Dataframe
    test_df = test_loader.load_data()  # Testdaten als Dataframe
   
    # Festlegen des Speicherorts der SQLite Datenbank durch User input
    db_path = input("Bitte geben Sie den Pfad zur Datenbank ein (z.B. C:/path/to/database.db): ")
    engine = get_engine(db_path)

    # Erstellen der Tabellen und anfügend der geladenen Daten
    Train.add_df_to_tbl(train_df, engine)  # train_df an Tabelle Train anfügen
    Ideal.add_df_to_tbl(ideal_df, engine)  # ideal_df an Tabelle Ideal anfügen
    Test.add_df_to_tbl(test_df, engine)  # test_df an Tabelle Test anfügen

    # Verarbeitung der Daten
    # Durchführen der Mean Squared Error Berechnung
    mse_df = Mathematics.calculate_min_mse(train_df, ideal_df)
    Result.add_df_to_tbl(mse_df, engine)  # mse_df an Tabelle Result anfügen

    # Durchführen der Validierung der Testdaten.
    validated_df = Mathematics.validate_dfs(mse_df, ideal_df, test_df)
    Summery.add_df_to_tbl(validated_df, engine)  # validated_df an Tabelle Summery anfügen
    
    # Optionale Visualisierung
    visualize = input("Möchten Sie die Ergebnisse visualisieren? (ja/nein): ")
    if visualize.lower() == "ja":
        print("Visualisierung wird durchgeführt...")
        Visualisierung.plot_validation_results(validated_df)
    
    print("Programmende")

if __name__ == "__main__":
    main()

