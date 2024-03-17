from sqlalchemy import Column, Float, Integer, String
from .base_tbl import Base
from src.status_messages import Messages
import logging


class Result(Base):
    '''
    Diese Klasse ist das Modell für die Tabelle der Ergebnisse
    der Berechung des Mean-Squared-Error.
    Sie erbt von der Klasse Base

    Aufbau Tabelle:
    - Spalten: id, y_train_col, best_ideal_col, min_mse
    - Zeilen: durch Pandas Dataframe befüllt.

    Methoden:
    - add_df_to_tbl: Hinzüfügen von Daten aus einem Dataframe
     
    '''
    __tablename__ = 'Ergebnisse'
    id = Column(Integer, primary_key=True)
    y_train_col = Column(String)
    best_ideal_col = Column(String)
    min_mse = Column(Float)