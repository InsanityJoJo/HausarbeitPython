import tkinter as tk
from tkinter import filedialog, messagebox, Button

class Gui:
    '''
    Diese Klasse sogt für Benutzerfreundlichkeit 
    im Programm. Es werden verschiedene Gui-Elemente
    für die Benutzereingaben bereitgestellt.

    Methoden:
    - select_file(): Auswahl von Dateien
    - ask_user_for_visualizations(): Auswahmöglichkeiten Für die Visualiserung
    - end_message(): Hinweis für den User
    '''
    def select_file(prompt_message):
        '''
        Diese Methode erzeugt einen Auswahldialog,
        über welchen der Benutzer Dateien auswählen kann.
        Die Methode wird für die Auswahl der CSV-Dateien
        und der Datenbank angewendet. 

        Methodenparameter:
        - prompt_message: String, Titel des Auswahldialogfensters
        
        Rückgabewerte: 
        - file_path: String, Pfad zur ausgewählten Datei
        '''
        root = tk.Tk()  # Erstellen eines Fensterns
        root.withdraw()  # schließen des Fenster, nur Funktion benötigt.
          # Öffnet den Dialig zur Dateiauswahl
        file_path = filedialog.askopenfilename(title=prompt_message)

        if not file_path:  # Falls kein Dateipfad ausgewählt wurde
            print("Keine Datei ausgewählt. Das Programm wird beendet.")
            exit()  # Beendet das Programm

        return file_path

    def create_visualisation_window(state, vis, train_df, ideal_df, test_df, mse_df, result_df, on_close):
        '''
        Erzeugt ein Fenster mit Buttons für die Visualisierung der 
        verschiedenen Datensätze
        und einen Button zum Beenden der Visualisierung.
        
        Parameters:
        - state: ProgramState, für den aktuellen Stand des Programms
        - vis: Instanz der Visualisierungsklasse
        - train_df, ideal_df, test_df, mse_df, result_df: 
            DataFrames für die Visualisierung
        - on_close(): Callback-Funktion um nach Schließen des Fensters
            ein Weiterlaufen zu ermöglichen
        
        '''
        root = tk.Tk()
        root.title("Visualisierungsoptionen")  # Titel
        root.geometry('400x300+400+200')  # Größe und Position

        def close_window():
            """
            Setzt den Visualisierungsstatus auf abgeschlossen
            und schließt das Fenster.
            """
            state.visualisations_completed = True
            on_close()  # Callback funktion
            root.destroy()

        # Button für die Visualisierung der Trainingsdaten
        Button(root, text="Visualisiere Trainingsdaten", 
            command=lambda: vis.plot_train_data(train_df)).pack(pady=10)

        # Button für die Visualisierung der idealen Funktionen
        Button(root, text="Visualisiere Ideale Funktionen", 
            command=lambda: vis.plot_ideal_funktions(ideal_df)).pack(pady=10)

        # Button für die Visualisierung der Testdaten
        Button(root, text="Visualisiere Testdaten", 
            command=lambda: vis.plot_test_data(test_df)).pack(pady=10)

        # Button für die Visualisierung der Mean-Squared-Error-Berechnung
        Button(root, text="Visualisiere MSE Berechnung", 
            command=lambda: vis.plot_mse_result(mse_df, train_df, ideal_df)).pack(pady=10)

        # Button für die Visualisierung der Validierung der Selektion
        Button(root, text="Visualisiere das Endergebnis", 
            command=lambda: vis.plot_validation_results(result_df)).pack(pady=10)

        # Button zum Beenden der Visualisierung und Schließen des Fensters
        Button(root, text="Beenden", command=close_window).pack(pady=20)

        root.mainloop()

    def end_message(title, info):
        '''
        Diese Methode erzeugt eine Hinweisfenster mit
        dem Button "ok".

        Methodenparameter:
        - title: String, Titel des Fensters
        - info: Sting, Hinweis der angezeigt wird

        Rückgabewert:
        None, implizit, da nur ein Fenster erzeugt wird.      
        '''    
        root = tk.Tk()  # Erstellen eines Fensterns
        root.withdraw()  # schließen des Fenster, nur Funktion benötigt.
        # Informationen am Ende des Programms
        messagebox.showinfo(title, info)