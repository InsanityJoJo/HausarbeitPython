import pytest
import pandas as pd
from src.data_loading import DataLoader
'''
Dieser Test soll sicherstellen, dass ein Laden der Daten aus einer CSV möglichlich ist.
'''
def test_load_data():
    '''
    Test des Dataloaders in src/data_loading.py
    Testfälle: 
    - Kann eine bestehende CSV-Datei geladen werden
    - ist die geladene Datei ein Padas Dataframe
    - Exception (FileNotFoundError) mit eigener Nachricht, wenn die Datei nicht existiert.
    - Exception (TypeError) mit eigener Nachricht, wenn die Datei keine Endung mit .csv hat.     
    '''
    # laden einer des Beispieldatensatzes der Trainingsdaten
    loader = DataLoader("data/example_data/train.csv")
    data1 = loader.load_data()

    # Check, dass Daten geladen wurden
    assert data1 is not None
    
    # Check, dass Daten nicht leer sind.
    assert len(data1) > 0
    
    # Check, dass die Daten vom type Dataframe sind
    assert type(data1) == pd.DataFrame

    # Dieser Testfall prüft den FileNotFoundError bei nicht existierenden Dateien.    
    with pytest.raises(FileNotFoundError) as fnfexc_info:
        loader2 = DataLoader("non_existent_file.csv")
        data2 = loader2.load_data()
    # Check, dass hier die erwatete Fehlermedung übergeben wurde.
    assert "Die Datei non_existent_file.csv konnte nicht gefunden werden" in str(fnfexc_info.value)

    # Dier Testfall prüft den TypeEror der geworfen werden soll, wenn eine nicht-csv Datei geladen werden soll.
    with pytest.raises(TypeError) as teexc_info:
        loader3 = DataLoader("data/example_data/textdatei.txt")
        data3 = loader3.load_data()
    # Check, dass hier die erwatete Fehlermedung übergeben wurde.
    assert "Die Datei data/example_data/textdatei.txt ist nicht vom Typ .csv" in str(teexc_info.value)

    # Dieser Testfall überprüft, den ValueError der geworfen werden soll, wenn eine CSV-Datei nicht das gewünschte Format hat.
    with pytest.raises(ValueError) as veexc_info:
        loader4 = DataLoader("data/example_data/wrongformat.csv")
        data4 = loader4.load_data()
        loader4.validate_csv_format(data4)

    assert "Die CSV-Datei hat nicht das richtige Format." in str(veexc_info.value)