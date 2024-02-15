import pytest
from src.data_loading import DataLoader
'''
Dieser Test soll sicherstellen, dass ein Laden der Daten aus einer CSV möglichlich ist.
'''
def test_can_load_csv_data():
    '''
    Test des Dataloaders in src/data_loading.py 
    '''
    loader = DataLoader("data/example_data/train.csv")
    data = loader.load_data()
    assert data is not None
    assert len(data) > 0

    