from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import sessionmaker
from .base_tbl import Base
from .status_messages import Messages
import logging


class Summery(Base):
    '''
    Diese Klasse ist das Modell für die Tabelle der Zusammenfassung Ergebnisse in der DB.
   

    Aufbau Tabelle:
        Spalten: 
            - id: Integer
            - x_punkt: Float
            - y_punkt: Float
            - abweichung: Float
            - y_Ideal: String
        Zeilen: 
            - befüllt durch df

    Methoden:

    add_df_to_tbl: 
        Die Methode überschreibt die Methode add_df_to_tbl der Oberklasse, 
        da nicht alle Informationen aus dem DF in die Tabelle angefügt werden.
        Hinzüfügen von Daten aus Dataframe mit dem Aufbau:
            Spalten:
                x, y, ..., best_ideal, min_Abweichung
            
            (Beispiel):
                    x          y    y36   y11        y2        y33 best_ideal  min_Abweichung
                96 -20.0 -19.347134  100.0 -20.0  0.408082  20.124610        y11        0.652866
                66 -20.0  99.261604  100.0 -20.0  0.408082  20.124610        y36        0.738396
                89 -18.1  35.745747   90.5 -18.1  0.731991  18.237598        y33       17.508149
                54 -17.5  16.389914   87.5 -17.5  0.219440  17.642279        y33        1.252365
                42 -17.4  16.138560   87.0 -17.4  0.120944  17.543089        y33        1.404529
                ...

    '''
    
    __tablename__ = 'Zusammenfassung'
    id = Column(Integer, primary_key=True)
    x_punkt = Column(Float, name='X (Test Funktion)')
    y_punkt = Column(Float, name='Y1 (Test Funktion)')
    abweichung = Column(Float, name='Delta Y (Abweichung)')
    y_Ideal = Column(String, name='Nummer der Idealen Funktion')

    @classmethod
    def add_df_to_tbl(cls, df, engine):
        '''
        Diese Methode überschreibt die der Oberklasse. Sie erstellt ein neues 
        DataFrame aus dem übergeben, da nicht alle Spalten benötigt werden.
        Die Spalten werden nach den Anforderungen der Aufgabe umbenannt.
        Sie fügt die Daten dann an die Tabelle an.
         
        '''
    
        # Auswahl der benötigten Spalten und Umbenennung entsprechend der Datenbanktabelle
        df_to_insert = df[['x', 'y', 'min_Abweichung', 'best_ideal']].rename(columns={
            'x': 'X (Test Funktion)',
            'y': 'Y1 (Test Funktion)',
            'min_Abweichung': 'Delta Y (Abweichung)',
            'best_ideal': 'Nummer der Idealen Funktion',
        })
        try:
            df_to_insert.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)
            # Konfiguration der Logging Info-Nachrichten im positiven Fall
            logging.info(Messages.DATA_INSERTED.value.format(table_name=cls.__tablename__))

        except Exception as e:
            # Konfiguration der Logging Error- Nachrichten im negativen Fall
            logging.error(Messages.ERROR_DATA_INSERTED.value.format(table_name=cls.__tablename__, error=e))
            raise