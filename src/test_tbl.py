from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from database.engine import engine
from src.status_messages import Messages
import logging

class Test(Base):
    '''
    Diese Klasse ist das modell für die Tabelle der Testdaten und der Ergebnisse in der DB
    Sie erbt von der Klasse Base

    Aufbau Tabelle:
        Spalten: id,
        Zeilen: 

    Methoden:

    add_df_to_tbl: Hinzüfügen von Daten aus einem Dataframe
     
    '''
    __tablename__ = 'Testdaten'
    id = Column(Integer, primary_key=True)

    @classmethod
    def add_df_to_tbl(cls, df):
        '''
        Diese Methode fügt Daten aus einem DataFrame an die Tabelle an
        '''
        try:
            df.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)
            # Konfiguration der Logging Info-Nachrichten im positiven Fall
            logging.info(Messages.DATA_INSERTED.value.format(table_name=cls.__tablename__))

        except Exception as e:
            # Konfiguration der Logging Error- Nachrichten im negativen Fall
            logging.error(Messages.ERROR_DATA_INSERTED.value.format(table_name=cls.__tablename__, error=e))

