import pytest
import pandas as pd
from src.data_loading import DataLoader
from src.status_messages import Messages


class TestDataLoader:
    '''
    Dieser Test soll sicherstellen, 
    dass ein Laden der Daten aus einer CSV möglichlich ist.
    '''
    def test_load_data(self):
        '''
        Test des Dataloaders in src/data_loading.py
        Testfälle: 
        - Kann eine bestehende CSV-Datei geladen werden
        - ist die geladene Datei ein Padas Dataframe
        - Exception (FileNotFoundError) mit eigener Nachricht,
        wenn die Datei nicht existiert.
        - Exception (TypeError) mit eigener Nachricht, 
        wenn die Datei keine Endung mit .csv hat.     
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

        # Dieser Testfall prüft den FileNotFoundError 
        # bei nicht existierenden Dateien.    
        with pytest.raises(FileNotFoundError) as fnfexc_info:
            loader2 = DataLoader("non_existent_file.csv")
            data2 = loader2.load_data()
        # Check, dass hier die erwatete Fehlermedung übergeben wurde.
        assert "Die Datei non_existent_file.csv konnte nicht gefunden werden" in str(
            fnfexc_info.value
            )

        # Dier Testfall prüft den TypeEror der geworfen werden soll, 
        # wenn eine nicht-csv Datei geladen werden soll.
        with pytest.raises(TypeError) as teexc_info:
            loader3 = DataLoader("data/example_data/textdatei.txt")
            data3 = loader3.load_data()
        # Check, dass hier die erwatete Fehlermedung übergeben wurde.
        assert "Die Datei data/example_data/textdatei.txt ist nicht vom Typ .csv" in str(
            teexc_info.value
            )



    def test_validate_csv_format(self):
        '''
        Die Methode enthält Testfälle für die Validierung 
        des Formats der Trainings-, Test- und Idealdaten.
        Sowie wie die Üperfrügung der Fehlernachricht 
        wenn das Format invalid ist.
        '''

        # Dieser Testfall überrüft, of eine CSV-Datei die dem Format
        # der Trainingsdaten entspricht validiert erfolgreich validiert werden kann.
        loader_train = DataLoader("data/example_data/train.csv")
        data_train = loader_train.load_data()
        assert loader_train.validate_csv_format(data_train) == Messages.VALID_TRAINING

        # Dieser Testfall überrüft, of eine CSV-Datei die dem Format
        # der idealen Funktion entspricht validiert erfolgreich validiert werden kann.
        loader_ideal = DataLoader("data/example_data/ideal.csv")
        data_ideal = loader_ideal.load_data()
        assert loader_ideal.validate_csv_format(data_ideal) == Messages.VALID_IDEAL

        # Dieser Testfall überrüft, of eine CSV-Datei die dem Format 
        # der Testdaten entspricht validiert erfolgreich validiert werden kann.
        loader_test = DataLoader("data/example_data/test.csv")
        data_test = loader_test.load_data()
        assert loader_test.validate_csv_format(data_test) == Messages.VALID_TEST
        
        # Dieser Testfall überprüft, den ValueError der geworfen werden soll,
        # wenn eine CSV-Datei nicht das gewünschte Format hat.
        with pytest.raises(ValueError) as exc_info:
            loader_wrong = DataLoader("data/example_data/wrongformat.csv")
            data_wrong = loader_wrong.load_data()
            loader_wrong.validate_csv_format(data_wrong)
        assert exc_info.value.args[0] == Messages.INVALID_CSV_FORMAT.name