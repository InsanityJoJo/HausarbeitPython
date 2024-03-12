from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from src.status_messages import Messages
import logging

class Train(Base):
    '''
    Diese Klasse ist das modell für die Tabelle der Trainingsdaten in der DB
    Sie erbt von der Klasse Base

    Aufbau Tabelle:
        Spalten: id, x, y1, ..., y4
        Zeilen: befüllung durch Padas Dataframe

    Methoden:

    add_df_to_tbl: Hinzüfügen von Daten aus einem Dataframe
     
    '''
    __tablename__ = 'Trainingsdaten'
    id = Column(Integer, primary_key=True)
    x = Column(Float, name='X')
    y1 = Column(Float, name='Y1 (Training Funktion)')
    y2 = Column(Float, name='Y2 (Training Funktion)')
    y3 = Column(Float, name='Y3 (Training Funktion)')
    y4 = Column(Float, name='Y4 (Training Funktion)')

    @classmethod
    def add_df_to_tbl(cls, df, engine):
        '''
        Diese Methode überschreibt die der Oberklasse. Sie nennt die Spalten des Dataframes um,
        so dass sie an die der Tabelle passen. Sie fügt die Daten dann an die Tabelle an. 
        '''
        # Umbenennen der Spalten im DataFrame entsprechend der Datenbanktabelle Train
        df_renamed = df.rename(columns={
            'x': 'X',
            'y1': 'Y1 (Training Funktion)',
            'y2': 'Y2 (Training Funktion)',
            'y3': 'Y3 (Training Funktion)',
            'y4': 'Y4 (Training Funktion)',
        })
        try:
            df_renamed.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)
            # Konfiguration der Logging Info-Nachrichten im positiven Fall
            logging.info(Messages.DATA_INSERTED.value.format(table_name=cls.__tablename__))

        except Exception as e:
            # Konfiguration der Logging Error- Nachrichten im negativen Fall
            logging.error(Messages.ERROR_DATA_INSERTED.value.format(table_name=cls.__tablename__, error=e))
            raise