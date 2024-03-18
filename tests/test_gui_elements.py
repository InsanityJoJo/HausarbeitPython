import unittest
from unittest.mock import patch
from src.gui_elemets import Gui

class TestGui(unittest.TestCase):
    '''
    Diese Klasse testet die Klasse Gui.

    '''
    @patch('src.gui_elemets.Gui.select_file')
    def test_select_file(self, mock_select_file):
        # Rückgabe des Dateipfads simulieren
        mock_select_file.return_value = 'data/example_data/ideal.csv'
        result = Gui.select_file("Bitte wählen Sie eine Datei aus")
        self.assertEqual(result, 'data/example_data/ideal.csv')

    
    @patch('src.gui_elemets.Gui.ask_user')
    def test_ask_user_yes(self, mock_askyesno):
        # Simuliere eine "Ja"-Antwort
        mock_askyesno.return_value = True
        result = Gui.ask_user("Titel", "Frage?")
        self.assertTrue(result)

    @patch('src.gui_elemets.Gui.ask_user')
    def test_ask_user_no(self, mock_askyesno):
        # Simuliere eine "Nein"-Antwort
        mock_askyesno.return_value = False
        result = Gui.ask_user("Titel", "Frage?")
        self.assertFalse(result)

    @patch('src.gui_elemets.Gui.end_message')
    def test_end_message(self, mock_showinfo):
        # Prüfe, ob die Methode `showinfo` aufgerufen wird
        Gui.end_message("Ende", "Das Programm ist beendet")
        mock_showinfo.assert_called_once_with("Ende", "Das Programm ist beendet")

if __name__ == '__main__':
    unittest.main()    