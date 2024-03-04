import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class Visualisierung:
    '''
    In dieser Klasse werden die Plot für die Visualisierung des Projekts implementiert.

    Methoden:

    '''
    def __init__(self):
        '''Konstruktor'''
        sns.set_theme(style="darkgrid")
        # Definiere eine Farbpalette für y1 bis y4
        self.colors = ['blue', 'orange', 'green', 'red']


    def plot_train_data(self, df, x_col):
        '''
        Diese Methode visualisiert die Trainingsdaten
        '''
        fig, axes = plt.subplots(2, 5, figsize=(25, 8))  # 2 Zeilen, 5 Spalten von Plots

        # Erste Zeile: Übersichtsplot mit allen Daten als Punkte
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4']):
            sns.scatterplot(data=df, x=x_col, y=col, ax=axes[0, 0], label=col, color=self.colors[i])
        axes[0, 0].set_title('Übersicht aller Trainingsdaten')
        axes[0, 0].legend()

        # Erste Zeile: Detaillierte Punktplots für jede y-Spalte
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4'], start=1):
            sns.scatterplot(data=df, x=x_col, y=col, ax=axes[0, i], color=self.colors[i-1])
            axes[0, i].set_title(f'Detailansicht {col} (Punkte)')
            # Anpassen der y-Achsenbereiche falls nötig, speziell für y3
            if col == 'y3':
                axes[0, i].set_ylim([-5, 5])

        # Zweite Zeile: Übersichtsplot mit allen Daten
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4']):
            axes[1, 0].plot(df[x_col], df[col], label=col, color=self.colors[i])
        axes[1, 0].set_title('Übersicht aller Trainingsdaten')
        axes[1, 0].legend()       
        # Zweite Zeile: Detaillierte Linienplots für jede y-Spalte
        for i, col in enumerate(['y1', 'y2', 'y3', 'y4'], start=1):
            axes[1, i].plot(df[x_col], df[col], color=self.colors[i-1])
            axes[1, i].set_title(f'Detailansicht {col} (Linien)')
            # Anpassen der y-Achsenbereiche falls nötig, speziell für y3
            if col == 'y3':
                axes[1, i].set_ylim([-5, 5])

        plt.tight_layout()
        plt.show()

    def plot_ideal_funktions(self, df, x_col):
        '''
        Diese Methode visualisiert die idealen Funktionen
        '''
        # Berechne die mittleren Y-Werte für jede Funktion
        mean_values = df.drop(columns=[x_col]).mean().sort_values()
        # Teile die Funktionen basierend auf ihren mittleren Y-Werten in 6 Cluster ein
        clusters = np.array_split(mean_values, 6)
        cluster_labels = {col: f"Cluster {i+1}" for i, cluster in enumerate(clusters) for col in cluster.index}

        # Erstelle eine neue Spalte im langen Format DataFrame für die Cluster-Zugehörigkeit
        df_long = pd.melt(df, id_vars=[x_col], var_name='Variable', value_name='Wert')
        df_long['Cluster'] = df_long['Variable'].map(cluster_labels)

        # Erstelle 6 Subplots (3x2)
        fig, axes = plt.subplots(2, 3, figsize=(25, 12), sharex=True)
        
        for i, cluster in enumerate(clusters):
            cluster_df = df_long[df_long['Cluster'] == f"Cluster {i+1}"]
            ax = axes[i // 3, i % 3]  # Bestimme die Position des Subplots

            # Visualisiere die Funktionen des Clusters
            sns.scatterplot(data=cluster_df, x=x_col, y='Wert', hue='Variable', palette='Set2', ax=ax)
            ax.set_title(f"{cluster_df['Cluster'].iloc[0]}")
            ax.legend(title='Funktion', bbox_to_anchor=(1.05, 1), loc='upper left')
            
            # Anpassen des y-Achsenbereichs basierend auf den Funktionen im Cluster
            y_min = cluster_df['Wert'].min()
            y_max = cluster_df['Wert'].max()
            puffer = (y_max - y_min) * 0.1  # 10% Puffer
            ax.set_ylim([y_min - puffer, y_max + puffer])

        plt.suptitle("Visualisierung der idealen Funktionen nach Clustern mit angepassten y-Achsenbereichen")
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Anpassen für den Titel
        plt.show()

    def plot_test_data(self, df, x_col):
        '''
        Diese Methode visualisiert die idealen Funktionen
        '''        
        # Umschmelzen des DataFrames in ein langes Format
        df_long = pd.melt(df, id_vars=[x_col], var_name='Variable', value_name='Wert')
        
        plt.figure(figsize=(25, 10))
        sns.scatterplot(data=df_long, x=x_col, y='Wert', hue='Variable')
        plt.title("Visualisierung aller Testdaten")
        plt.show()

    def plot_mse_result(self, mse_df, train_df, ideal_df):
        '''
        Diese Methode visualisiert das Ergebnis der MSE Berechung
        '''
        plt.figure(figsize=(12, 8))

        # Durchlaufe jede Zeile in mse_df, um sowohl Trainingsdaten als auch ideale Funktionen zu plotten
        for _, row in mse_df.iterrows():
            train_col = row['y_train_col']
            ideal_col = row['best_ideal_col']
            color = self.colors[mse_df.index[mse_df['best_ideal_col'] == ideal_col][0]]  # Farbe basierend auf der Position

            # Plotten der Trainingsdaten
            plt.plot(train_df['x'], train_df[train_col], label=f"Trainingsdaten: {train_col}", color=color, linestyle='--')
            
            # Plotten der idealen Funktion
            plt.plot(ideal_df['x'], ideal_df[ideal_col], label=f"Ideale Funktion: {ideal_col}", color=color)

        plt.title("Visualisierung der MSE-Berechnungsergebnisse")
        plt.xlabel("X-Wert")
        plt.ylabel("Y-Wert")
        plt.legend()
        plt.grid(True)
        plt.show()


    def plot_validation_results(self, result_df):
        plt.figure(figsize=(12, 8))

        # Zeichne jede ideale Funktion mit Linien
        ideal_cols = ['y36', 'y11', 'y2', 'y33']
        for i, col in enumerate(ideal_cols):
            plt.plot(result_df['x'], result_df[col], label=col, color=self.colors[i])

        # Zeichne die Testdaten-Punkte basierend auf der Zuordnung zu den idealen Funktionen
        # Da die Farbzuweisung dynamisch ist, basiert sie auf der Position der idealen Funktion in ideal_cols
        for index, row in result_df.iterrows():
            # Bestimme den Index der idealen Funktion in der Liste ideal_cols
            ideal_index = ideal_cols.index(row['best_ideal']) if row['best_ideal'] in ideal_cols else -1
            color = self.colors[ideal_index] if ideal_index != -1 else 'black'
            plt.scatter(row['x'], row['y'], color=color, edgecolor='w', zorder=5)
            plt.text(row['x'], row['y'], f"{row['min_Abweichung']:.2f}", fontsize=9, ha='right')

        plt.title("Kombinierte Visualisierung der idealen Funktionen und Testdaten")
        plt.xlabel("X-Wert")
        plt.ylabel("Y-Wert")
        plt.legend(title="Ideale Funktionen")
        plt.grid(True)
        plt.show()


