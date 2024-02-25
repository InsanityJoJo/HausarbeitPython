from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from database.engine import engine
from src.status_messages import Messages
import logging

class DataTableTest(Base):
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
    x_punkt = Column(Float)
    y_punkt = Column(Float)
    # y_Ideal = Column(Float)
    # abweichung = Column(Float)



