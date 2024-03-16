import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
from scipy.integrate import simps

class Visualisierung:
    '''
    In dieser Klasse ist die Visualisierung der Plots für das Projekts implementiert.
    
    Methoden:
    - plot_train_data: Erzeugt den Plot der Trainingsdaten.
    - plot_ideal_funktions: Erzeugt den Plot der Idealen Funktion. 
    - plot_test_data: Erzeugt den Plot der Test Daten. 
    - plot_mse_result: Erzeugt den Plot für das Ergebnis der Mean-Squared Error Nachricht.
    - plot_validation_results: Erzeugt den Plot für das Ergebnis der zugeordneten Testdaten. 
    '''
    def __init__(self, show_plots = False):
        '''
        Konstruktor
        Festlegen des Styles als "darkgrind" und einheitlicher Farben aus der Liste.
        Variable show_plots legt fest ob der Plot angezeigt werden soll. 
        True bedeutet anzeigen, False nicht anzeigen.
        Für die Tests sollen manchmal keine Plots angezeit werden,
    

        '''
        # Festlegen des Themas der Darstellung.
        sns.set_theme(style="darkgrid")
        # Festlegen der Farbpalette für die jeweiligen Funktionen
        self.colors = ['blue', 'orange', 'green', 'red']
        self.show_plots = show_plots
        

    def plot_train_data(self, df):
        '''
        Diese Methode visualisiert die Trainingsdaten.
        Sie erzeugt zwei Übersichtsplots (einen Scatterplot, einen Linienplot) 
        und vier detaillierte Plots für jede Funktion in 'y1' bis 'y4', sowohl als Scatter- 
        als auch Linienplot. Es wird angenommen, dass 'df' validiert wurde und die erforderlichen
        Spalten enthält. Andernfalls könnte es zu einem KeyError kommen.
        
        Anordnung der Plots:
        |TÜ|y1|y2|y3|y4|  <-- Erste Zeile Scatterplots
        |--|--|--|--|--|
        |TÜ|y1|y2|y3|y4|  <-- Zweite Zeile Linienplots

        Methodenparameter:
            - df: Pandas Dataframe der Trainingsdaten Aufbau Spalten: x, y1, y2, y3, y4

        Rückgabewert:
            - None implizit, da hier nur Plots erzuegt werden            
        '''

        # Erstellung eines Grids von subplots, die Zusammen dargestellt werden sollen.
        fig, axes = plt.subplots(2,  # 2 Zeilen
                                  5,  # 5 Spalten
                                    figsize=(25, 8)  # Darstellungsgröße
                                    )  

        # [0,0] Erste Zeile, erste Spalte: 
        # Übersichtsplot mit allen Daten geplottet als Punkte
        
        # Durch die vier Trainingsfunktionen iterrieren und zusammen als seaborn scatterplot darstellen.
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4']):
            sns.scatterplot(data=df,  # Auswahl des Dataframes
                             x='x',  # Auswahl der X-Werte 
                              y=col,  # Auswahl der Y-Werte, hier jeweils für alle Funktionen neu gezeichnet
                               ax=axes[0, 0],  # Auswahl des Darstellungortes im Grid
                                label=col,  # Hinzufügen der Funktion zur Legende
                                 color=self.colors[i]  # Auswahl der Farbe für die Funktion
                                 )
        
        axes[0, 0].set_title('Scatterplot über alle Trainingsdaten')  # Titel des Plots festlegen
        axes[0, 0].legend()  # Legende für diesen Plot darstellen

        # [0, 1-4] Erste Zeile, Spalten 2-5:
        # Detaillierte Punktplots für jede Trainingsfunktion

        # Durch die vier Trainingsfunktionen iterrieren und getrennte als einzelen scatterplots darstellen.
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4'], start=1):  # Beginnt mit der 2. Spalte, da die erste x ist.
            sns.scatterplot(data=df,  # Auswahl des Dataframes
                             x='x',  # Auswahl der X-Werte
                               y=col,  # Auswahl der Y-Werte
                                 ax=axes[0, i],  # Auswahl des Darstellungortes im Grid
                                   color=self.colors[i-1]   # Auswahl der Farbe für die Funktion, i-1 weil start=1
                                   )
            
            axes[0, i].set_title(f'Detailansicht {col} (Punkte)')  # Titel für den jeweiligen Plot festlegen
            
            # Anpassen des Y-Wertebereichs für y3 für eine aussagekräftige Darstellung
            if col == 'y3':
                axes[0, i].set_ylim([-5, 5])

        # [1, 0] Zweite Zeile, erste Spalte:
        # Übersichtsplot mit allen Daten als Linienplot
                
        # Durch die vier Trainingsfunktionen iterrieren und zusammen als Linienplot darstellen.                
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4']):
            axes[1, 0].plot(df['x'],  # Auswahl der X-Werte
                             df[col],  # Auswahl der Y-Werte
                               label=col,  # Funktion in die Legende einfügen
                                 color=self.colors[i])  # Farbe der Funktion auswählen

        axes[1, 0].set_title('Linienplot über alle Trainingsdaten')  # Titel des Plots festlegen
        axes[1, 0].legend()  # Legende für diesen Plot darstellen

        # [1, 1-4] Zweite Zeile, Spalten 2-5:       
        # Detaillierte Linienplots für jede Trainingsfunktion

        # Durch die vier Trainingsfunktionen iterrieren und als Lininenplots darstellen.
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4'], start=1):  # Beginnt mit der 2. Spalte, da die erste x ist.
            axes[1, i].plot(df['x'], df[col], color=self.colors[i-1])  # Auswahl für X-Werte, Y-Werte, Farbe
            axes[1, i].set_title(f'Detailansicht {col} (Linien)')  # Titel für den jeweiligen Plot festlegen
            
            # Anpassen des Y-Wertebereichs für y3 für eine aussagekräftige Darstellung
            if col == 'y3':
                axes[1, i].set_ylim([-5, 5])

        plt.tight_layout()  # Layout der Plots
        if self.show_plots:
            plt.show()  # Plotten der Diagramme

    def plot_ideal_funktions(self, df):
        '''
        Diese Methode visualisiert die Idealen Funktionen.
        Sie erzeugt sechs Übersichtsplots mit geclusterten Funktionen. Die Gruppierung der Funktionen
        ist nötig, da sie sehr unterschiedliche y-Wertebereiche, Formen, Maxima enthalten.
        Der Übersichtlichkeit sollen die 50 Funktionen in 9 Plots aufgeteilt werden
        Die Cluster werden nach der Fläche unter Kurve(AUC - Area under Curve) erstellt,
        um ähnliche Wertebereiche so zu gruppieren.
        Die Darstellugn der idealen Funktionen dient der grafischen Übersicht über die Daten.
        Es wird angenommen, dass 'df' validiert wurde und die erforderlichen
        Spalten enthält. Andernfalls könnte es zu einem KeyError kommen.
        
        Anordnung der Plots:
        |c1|c2|c3|
        |--|--|--|
        |c4|c5|c6|
        |--|--|--|        
        |c7|c8|c9|

        Methodenparameter:
            - df: Pandas Dataframe der Idealen Funktionen, Aufbau Spalten: x, y1, ..., y50


        Rückgabewert:
            - None implizit, da hier nur Plots erzuegt werden            
        '''
        
        auc_values = []  # Liste zum Speichern der AUC(Area under curve)-Werte für jede Funktion.

        # Berechnen des AUC-Werts für jede y-Spalte
        for col in df.columns[1:]:  # Überspringen der x-Spalte
            y_abs = np.abs(df[col])  # absoluter Wert der y-Werte
            auc = simps(y_abs, df['x'])  # Berechne die Fläche unter der Kurve
            auc_values.append(auc)  # Füge den Wert an die Liste an

        # Erstelle ein DataFrame, das die Funktionen und ihre AUC-Werte enthält
        func_names = df.columns[1:]  # Funktionsnamen
        auc_df = pd.DataFrame({'Funktion': func_names, 'AUC': auc_values})

        # Verwenden von auc_df um die Funktionen basierend auf ihren AUC-Werten zu clustern.
        # Einteilung der Funktionen in Quantile basierend auf ihren AUC-Werten.
        auc_df['Cluster'] = pd.qcut(auc_df['AUC'], 9, labels=False)  # Teile in 9 Cluster

        # Cluster-Information in das df einfügen
        # Dictionary von Funktionen und zugehörigen Cluster erstellen.
        function_to_cluster = auc_df.set_index('Funktion')['Cluster'].to_dict()
        # Für jede Zeile im df wird die Spalte 'Cluster' aus dem Dictionary gefüllt.
        df['Cluster'] = df.apply(lambda row: function_to_cluster[row.name] if row.name in function_to_cluster else None, axis=1)

        # Erstellen der 9 Subplots (3x3)
        fig, axes = plt.subplots(3, 3, figsize=(25, 12), sharex=True)
        
        for i in range(9):
            
            # Erstellen eine Liste von Funktionen, die zum aktuellen Cluster 'i' gehören.
            # Das Dictionary 'function_to_cluster' ordnet Funktionen ihren Clustern zu.
            cluster_functions = [func for func, cluster in function_to_cluster.items() if cluster == i]
            
            # Erstellen eines neuen DataFrames 'cluster_df' für das aktuelle Cluster.
            
            cluster_df = df[['x'] + cluster_functions].melt(  # Transformation des DataFrames von einem breiten Format (eine Spalte pro Funktion) zu einem langen Format
                id_vars=['x'],  # ID-Variable
                  var_name='Variable',  # umformen Variable
                    value_name='Wert'  # umformen Wert
                    )
            
            # Zugriff auf den i-ten Subplot innerhalb des 3x3 Grids von Subplots.
            ax = axes.flatten()[i]  # umwandeln des 2D Arrays in ein 1D Array, zugriff auf den i-ten Subplot
            
            # Erstelle einen Lineplot für das aktuelle Cluster.
            sns.lineplot(data=cluster_df,  # Dataframe, der visualisert wird
                          x='x',  # X-Achse 
                           y='Wert',  # Y-Achse
                             hue='Variable',  # Linien
                               ax=ax, # Subplot
                                 palette='Set2'  # Farbauswahl
                                 )
            
            # Setze den Titel für den aktuellen Subplot, der das Cluster repräsentiert.
            ax.set_title(f"Cluster {i+1}")
            
            # Platzieren der Legende außerhalb des Plots oben links.
            ax.legend(title='Funktion', bbox_to_anchor=(1.05, 1), loc='upper left')
            
            # Berechne das Minimum und Maximum der 'Wert'-Spalte im aktuellen Cluster,
            # um den sichtbaren Bereich der y-Achse dynamisch anzupassen.
            y_min, y_max = cluster_df['Wert'].min(), cluster_df['Wert'].max()
            
            # Füge einen Puffer von 10% zum Min- und Max-Wert hinzu, um den Plot visuell ansprechender zu gestalten.
            puffer = (y_max - y_min) * 0.1
            ax.set_ylim([y_min - puffer, y_max + puffer])
            
        plt.suptitle("Visualisierung der idealen Funktionen nach Clustern (Fläche unter Kurve)")
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        if self.show_plots:
            plt.show()  # Plotten der Diagramme

    def plot_test_data(self, df):
        '''
        Diese Methode visualisiert die Testdaten.
        Die Visualisierung ist optional. Die Darstellung ist ein scatterplot. 
        Methodenparameter:
            - df: Pandas Dataframe der Testdaten, Aufbau Spalten: x, y

        Rückgabewert:
            - None implizit, da hier nur Plots erzuegt werden  
        '''        
        # Umschmelzen des DataFrames in ein langes Format
        df_long = pd.melt(df, id_vars=['x'], var_name='Variable', value_name='Wert')
        
        plt.figure(figsize=(25, 10))
        sns.scatterplot(data=df_long, x='x', y='Wert', hue='Variable')
        plt.title("Visualisierung aller Testdaten")
        if self.show_plots:
            plt.show()  # Plott des Diagrammes

    def plot_mse_result(self, mse_df, train_df, ideal_df):
        '''
        Diese Methode visualisiert das Ergebnis der MSE Berechung.
        Die Darstellung ist ein gemeinsamer Plot von den vier idealen Funktionen,
        sowie der Trainingsdaten. Die Trainigsdaten sind in der Farbe der zugehörigen idealen Funktion dargestellt.
        Sie sind duch gestrichelte Linien verbunden. 
        Methodenparameter:
            - mse_df: Pandas Dataframe, Ergebnis der MSE-Berechnung, Spalten: y_train_col, best_ideal_col, min_mse  
            - train_df: Pandas Dataframe, Trainingsdaten, Spalten: x, y1, ..., y4
            - ideal_df: Pandas Dataframe, Aufbau Spalten, Spalten: x, y1, ..., y50
        Rückgabewert:
            - None implizit, da hier nur der Plot erzeugt wird 
        '''
        
        plt.figure(figsize=(12, 8))  # Größe festlegen

        # Durchlaufen jeder Zeile in mse_df, um die entsprechende Trainingsfunktion und die dazugehörige ideale Funktionen zu plotten
        for _, row in mse_df.iterrows():  # "_" da nur auf Zeilendaten zugegriffen wird, index wird nicht benötigt.
            train_col = row['y_train_col']  # Erheben der Trainingsfunktion
            ideal_col = row['best_ideal_col']  # Erheben der idealen Funktion
            color = self.colors[mse_df.index[mse_df['best_ideal_col'] == ideal_col][0]]  # Farbe basierend auf der Position von Trainings- und idealer Funktion

            # Plotten der Trainingsdaten, verbunden mit getrichelten Linien
            plt.plot(train_df['x'], train_df[train_col], label=f"Trainingsdaten: {train_col}", color=color, linestyle='--')
            
            # Plotten der idealen Funktion
            plt.plot(ideal_df['x'], ideal_df[ideal_col], label=f"Ideale Funktion: {ideal_col}", color=color)

        plt.title("Visualisierung der MSE-Berechnungsergebnisse")  # Festlegen des Titels
        plt.xlabel("X-Wert")  # Beschreibung X-Achse
        plt.ylabel("Y-Wert")  # Beschreibung Y-Achse
        plt.legend()  # Legende anzeigen
        plt.grid(True)  # Grid anzeigen
        if self.show_plots:
            plt.show()  # Plott des Diagrammes

    def plot_validation_results(self, result_df):
        '''
        Diese Methode visualisiert das Endergebnis des Programms. Nachdem die, duch die MSE Berechnung erhobenen idealen Funktionen,
        durch die Testdaten validiert wurden. Die Idealen Funktionen werden als Linienplot dargestellt. 
        Die Testdaten werden als Punkte in der Farbe der ihnen zugeordneten idealen Funktion dargestellt. 
        Wenn keine Zuordnung erfolgen konnte, werden die Testdaten in schwarz dargestellt. Zu den Datenpunkten wird die minimale Anweichung dargestellt.
        Methodenparameter:
            - result_df: Pandas Dataframe, Ergebnis der Validierung, Spalten: x, y, (vier ideale Funktionen), best_ideal, min_Abweichung  
        Rückgabewert:
            - None implizit, da hier nur der Plot erzeugt wird 

        '''
        plt.figure(figsize=(12, 8))  # Größe festlegen

        # Zeichnen jeder idealen Funktion als Linienplot
        ideal_cols = result_df.columns[2:6]  # Vier ideale Funktionen aus result_df
        for i, col in enumerate(ideal_cols):
            plt.plot(result_df['x'], result_df[col], label=col, color=self.colors[i]) 

        # iterrieren durch das df für die Farbzuweisung
        for index, row in result_df.iterrows():
            # Dynamische Farbzuweisung basierend auf der 'best_ideal' Spalte
            if row['best_ideal'] in ideal_cols:
                # Zuordnung der Farbe zu der entsprechenden Idealen Funktion
                color = self.colors[ideal_cols.tolist().index(row['best_ideal'])]
            else:
                # Wenn keine Zuordnung erfolgt ist, dass wird der Punkt schwarz
                color = 'black'

            # Hizufügen eines weiteren Punkts auf den Koordinaten der Testdaten,
            # Farbe ist dieselbe des Testdatenpunkts,      
            plt.scatter(row['x'], row['y'], color=color, edgecolor='w', zorder=5)
            # zu jedem Punkt wird die minimale Abweichung hinzugefügt
            plt.text(row['x'], row['y'], f"{row['min_Abweichung']:.2f}", fontsize=9, ha='right')

        plt.title("Kombinierte Visualisierung der idealen Funktionen und Testdaten")
        plt.xlabel("X-Wert")
        plt.ylabel("Y-Wert")
        plt.legend(title="Ideale Funktionen")
        plt.grid(True)
        if self.show_plots:
            plt.show()  # Plott des Diagrammes


