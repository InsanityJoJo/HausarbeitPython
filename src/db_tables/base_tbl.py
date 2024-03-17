from sqlalchemy.orm import DeclarativeBase
import logging
from src.status_messages import Messages

class Base(DeclarativeBase):
    '''
    Diese Klasse ist die Oberklasse der Tabellen Klassen Ideal in ideal_tbl.py, 
    Train in train_tbl.py, Test in exp_tbl.py, Results in results_tbl.py.

    In dieser Klasse wird die Funktionalität definniert ein pandas Dataframe
    an eine Tabelle anzufügen.

    Methoden
    - add_df_to_tbl: Anfügen eines Padas Dataframe an die Tabelle
    '''

    @classmethod
    def add_df_to_tbl(cls, df, engine):
        '''
        Diese Methode fügt Daten aus einem DataFrame an die Tabelle an.
        
        Methodenparameter
        - df: Padas Dataframe, dass angefügt werden soll
        - engine: Die Verbindung zur Datenbank in der
                  die Tabelle erstellt werden soll.

        Rückgabewert:
        - None (implizit), es werden Daten an die Tabelle angefügt. 
        '''
        try:
            df.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)
            # Konfiguration der Logging Info-Nachrichten im positiven Fall
            logging.info(Messages.DATA_INSERTED.value.format(table_name=cls.__tablename__))

        except Exception as e:
            # Konfiguration der Logging Error- Nachrichten im negativen Fall
            logging.error(Messages.ERROR_DATA_INSERTED.value.format(table_name=cls.__tablename__, error=e))
            raise