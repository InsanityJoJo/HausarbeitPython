from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from src.status_messages import Messages
import logging

class Test(Base):
    '''
    Diese Klasse ist das Modell für die Tabelle der Testdaten
    Sie erbt von der Klasse Base

    Aufbau Tabelle:
        Spalten: id, x_punkt, y_punkt
        Zeilen: durch df befüllt

    Methoden:
    - add_df_to_tbl: Hinzüfügen von Daten aus einem Dataframe
     
    '''
    __tablename__ = 'Testdaten'
    id = Column(Integer, primary_key=True)
    x_punkt = Column(Float)
    y_punkt = Column(Float)
    
    @classmethod
    def add_df_to_tbl(cls, df, engine):
        '''
        Diese Methode überschreibt die der Oberklasse. 
        Sie nennt die Spalten des Dataframes um,
        so dass sie an die vorgegebenen, der Tabelle passen. 
        Sie fügt die Daten dann an die Tabelle an. 
        
        Methondenparameter:
        - df: Pandas Dataframe der Testdaten
        - engine: Die Verbindung zur Datenbank in der
                  die Tabelle erstellt werden soll.

        Rückgabewert:
        - None (implizit), es werden Daten an die Tabelle angefügt. 
        '''
        # Umbenennen der Spalten im DataFrame entsprechend der Datenbanktabelle Train
        df_renamed = df.rename(columns={
            'x': 'x_punkt',
            'y': 'y_punkt' 
        })
        try:
            # Daten anfügen
            df_renamed.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)
            # Konfiguration der Logging Info-Nachrichten im positiven Fall
            logging.info(Messages.DATA_INSERTED.value.format(table_name=cls.__tablename__))

        except Exception as e:
            # Konfiguration der Logging Error- Nachrichten im negativen Fall
            logging.error(Messages.ERROR_DATA_INSERTED.value.format(table_name=cls.__tablename__, error=e))
            raise