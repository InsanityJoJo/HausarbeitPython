from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from src.status_messages import Messages
import logging

class Ideal(Base):
    '''
    Diese Klasse ist das Model für die Tabelle,
    der Idealen Funktionen in der Datenbank.
    Sie erbt von der Klasse Base.

    Aufbau Tabelle:
        Spalten: id, x, y1, ..., y50
        Zeilen: befüllung durch Padas Dataframe

    Methoden:
    - add_df_to_tbl: Daten aus Pandas Dataframe an Tabelle anfügen
     
    '''
    __tablename__ = 'IdealeFunktionen'
    id = Column(Integer, primary_key=True)
    x = Column(Float, name='X')

    @classmethod
    def add_df_to_tbl(cls, df, engine):
        '''
        Diese Methode überschreibt die der Oberklasse. 
        Sie nennt die Spalten des Dataframes um,
        so dass sie an die vorgeschriebenen, der Tabelle passen. 
        Sie fügt die Daten dann an die Tabelle an. 
                
        Methondenparameter:
        - df: Pandas Dataframe der idealen Funktionen
        - engine: Die Verbindung zur Datenbank in der
                  die Tabelle erstellt werden soll.

        Rückgabewert:
        - None (implizit), es werden Daten an die Tabelle angefügt.          
        '''
        # Umbenennen der Spalten im DataFrame entsprechend der Datenbanktabelle Train
        # Erstellen eines Dictionarys für die Umbenennung der Spalten
        rename_dict = {'x': 'X',} | {f'y{i}': f'Y{i} (Ideale Funktion)' for i in range(1, 51)}

        # Anwenden der Umbenennung
        df_renamed = df.rename(columns=rename_dict)

        try:
            # Anfügen der Daten
            df_renamed.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)
            # Konfiguration der Logging Info-Nachrichten im positiven Fall
            logging.info(Messages.DATA_INSERTED.value.format(table_name=cls.__tablename__))

        except Exception as e:
            # Konfiguration der Logging Error- Nachrichten im negativen Fall
            logging.error(Messages.ERROR_DATA_INSERTED.value.format(table_name=cls.__tablename__, error=e))
            raise

# Dynamisch Spalten für y1 bis y50 anfügen
for i in range(1, 51):
        setattr(Ideal, f'y{i}', Column(Float, name=f'Y{i} (Ideale Funktion)'))
