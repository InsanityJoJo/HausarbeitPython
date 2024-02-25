from sqlalchemy import Column, Float, Integer, String
from .base_tbl import Base
from src.status_messages import Messages
import logging
from database.engine import engine


class Result(Base):
    '''
    Diese Klasse ist das modell für die Tabelle der Ergebnisse in der DB
    Sie erbt von der Klasse Base

    Aufbau Tabelle:
       

    Methoden:

    add_df_to_tbl: Hinzüfügen von Daten aus einem Dataframe
     
    '''
    __tablename__ = 'Ergebnisse'
    id = Column(Integer, primary_key=True)
    y_train_col = Column(String)
    best_ideal_col = Column(String)
    min_mse = Column(Float)