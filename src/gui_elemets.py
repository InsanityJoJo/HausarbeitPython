import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Gui:
    '''
    Diese Klasse sogt für Benutzerfreundlichkeit 
    im Programm. Es werden verschiedene Gui-Elemente
    für die Benutzereingaben bereitgestellt.

    Methoden:
    - select_file(): Auswahl von Dateien
    - ask_user(): Einfacher Ja/Nein User-Dialog
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

    def ask_user(title, question):
        '''
        Diese Methode erzeugt einen einfachen Unserdialog
        in Form eines Fensters mit ja/nein Option.

        Methodenparameter:
        - title: String, Titel des Fensters
        - question: String, Frage an den User

        Rückgabewert:
        - response: Boolean, True bei "Ja"
        '''
        root = tk.Tk()  # Erstellen eines Fensterns
        root.withdraw()  # schließen des Fenster, nur Funktion benötigt.

        # Diealogfenster mit Ja/Nein Optionen
        response = messagebox.askyesno(title, question)

        # Gibt True zurück, wenn 'Ja' ausgewählt wurde, sonst False
        return response

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