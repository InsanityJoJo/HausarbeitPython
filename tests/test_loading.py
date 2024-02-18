import pytest
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
    - Exception (FileNotFoundError) mit eigener Nachricht, wenn die Datei nicht existiert     
    '''
    # laden einer des Beispieldatensatzes der Trainingsdaten
    loader = DataLoader("data/example_data/train.csv")
    data = loader.load_data()
    # Check, dass Daten geladen wurden
    assert data is not None
    # Check, dass Daten nicht leer sind.
    assert len(data) > 0

    # Dieser Testfall prüft den FileNotFoundError bei nicht existierenden Dateien.    
    with pytest.raises(FileNotFoundError) as exc_info:
        loader2 = DataLoader("non_existent_file.csv")
        data = loader2.load_data()
    # Check, dass hier die erwatete Fehlermedung übergeben wurde.
    assert "Die Datei non_existent_file.csv konnte nicht gefunden werden" in str(exc_info.value)