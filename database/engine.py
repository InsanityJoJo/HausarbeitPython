import os
import logging
from sqlalchemy import create_engine
from src.status_messages import Messages


def get_engine(db_path, echo=True):
    '''
    Diese Methode erstellt die Datenbank. 
    Der Speicherort der DB wird durch den User festgelegt.

    Methodenparameter:
        - db_path: Pfad an dem die BD erstellt oder 
                    mit der verbunden werden soll

    Rückgabewert:
        - engine: Gibt die Datenbank zurück.      
    '''
    # Prüfen, ob die Datenbank bereits existiert
    db_exists = os.path.exists(db_path)

    # Erstellen des Engine Objekts
    engine = create_engine(f'sqlite:///{db_path}', echo=echo)

    if not db_exists:
        logging.info(Messages.DATABASE_CREATED.value.format(db_path=db_path))
    else:
        logging.info(Messages.DATABASE_EXISTS.value.format(db_path=db_path))
    return engine


   

 