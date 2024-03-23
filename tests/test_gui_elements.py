import unittest
from unittest.mock import patch, Mock
from src.gui_elements import Gui

class TestGui(unittest.TestCase):
    '''
    Diese Klasse testet die Klasse Gui.
    
    Testmethoden:
    - test_select_file()
    - test_end_message()

    '''
    @patch('src.gui_elements.Gui.select_file')
    def test_select_file(self, mock_select_file):
        # Rückgabe des Dateipfads simulieren
        mock_select_file.return_value = 'data/example_data/ideal.csv'
        result = Gui.select_file("Bitte wählen Sie eine Datei aus")
        self.assertEqual(result, 'data/example_data/ideal.csv')

    @patch('src.gui_elements.Gui.end_message')
    def test_end_message(self, mock_showinfo):
        # Prüfe, ob die Methode `showinfo` aufgerufen wird
        Gui.end_message("Ende", "Das Programm ist beendet")
        mock_showinfo.assert_called_once_with("Ende", "Das Programm ist beendet")

if __name__ == '__main__':
    unittest.main()    