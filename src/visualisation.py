import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
        axes[0, 0].set_title('Übersicht aller Daten')
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
        axes[1, 0].set_title('Übersicht aller Daten')
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
        # Umschmelzen des DataFrames in ein langes Format
        df_long = pd.melt(df, id_vars=[x_col], var_name='Variable', value_name='Wert')
        
        plt.figure(figsize=(25, 10))
        sns.scatterplot(data=df_long, x=x_col, y='Wert', hue='Variable')
        plt.title("Visualisierung aller Idealen Funktionen")
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