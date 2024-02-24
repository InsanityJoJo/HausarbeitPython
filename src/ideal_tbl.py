from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from database.engine import engine
import logging
from src.status_messages import Messages

class Ideal(Base):
    '''
    Diese Klasse ist das modell für die Tabelle der Idealen Funktionen in der DB
    Sie erbt von der Klasse Base

    Aufbau Tabelle:
        Spalten: id, x, y1, ..., y50
        Zeilen: befüllung durch Padas Dataframe

    Methoden:

    add_df_to_tbl: Hinzüfügen von Daten aus einem Dataframe
     
    '''
    __tablename__ = 'ideale_funktionen'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    
    
 
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
            logging.error(Messages.ERROR_DATA_INSERTED.value.format(table_name=cls.__tablename__, e=e))

# Füge dynamisch Spalten für y1 bis y50 hinzu
for i in range(1, 51):
    setattr(Ideal, f'y{i}', Column(Float))



