from sqlalchemy import Column, Float, Integer
from .base_tbl import Base

class Test(Base):
    '''
    Diese Klasse ist das modell für die Tabelle der Testdaten
    Sie erbt von der Klasse Base

    Aufbau Tabelle:
        Spalten: id,
        Zeilen: 

    Methoden:

    add_df_to_tbl: Hinzüfügen von Daten aus einem Dataframe
     
    '''
    __tablename__ = 'Test-Daten-Tabelle'
    id = Column(Integer, primary_key=True)
    x_punkt = Column(Float)
    y_punkt = Column(Float)
