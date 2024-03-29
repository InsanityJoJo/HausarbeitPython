# Hausarbeit im Kurs Python
Dies ist das Programm für die Hausarbeit im Kurs Programmieren mit Python.
Mit diesem Programm werden Datensätze von Trainingsdaten, Idealen Funktionen und Testdaten aus CSV-Dateien ausgelesen.
Der Datensatz von 50 Idealen Funktionen wird mit 4 Trainingsfunktionen verglichen.
Jeder Trainingsfunktion wird die Ideale Funktion mit der kleinsten quadratischen Abweichung zugeordnet. 
Anschließend werden die so ausgewählten, vier idealen Funktionen mit Testdaten validiert. 
Zu jedem Testdatenpunkt wird die Y-Abweichung zu den ausgewälten Funktionen berechnet.
Ist Bedingung (y_punkt-y_ideal)^2 < sqr(2)*y_punkt^2 erfüllt, wird der Punkt der Funktion zugeordnet.
Die Daten werden in einer SQLite DB gespeischert. Dem Benutzer werden über ein Dialogfenster
Visualisierungsmöglichkeiten angeboten. 

## Einrichten
Anweisungen zur Einrichtung der Arbeitsumgebung und Installation aller notwendigen Abhängigkeiten.

> conda env create -f environment.yml
Dieser Befehl erstellt eine neue Conda-Umgebung mit dem Namen "HausarbeitPython".
Um diese Umgebung zu aktivieren, verwenden Sie den Befehl:
> conda activate HausarbeitPython

## Benutzung
Navigieren Sie in das Verzeichnis in dem die Datei main.py liegt.
Beispielsweise:
(HausarbeitPython) C:\Users\user\Dev\python\HausarbeitPython\src>
Um das Programm zu starten führen sie bitte die Datei main.py aus.
> python main.py

Sie werden nun durch den Dialog auf der Konsole und die GUI-Elemente geleitet. 

