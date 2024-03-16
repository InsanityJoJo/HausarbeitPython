import pytest
from sqlalchemy.orm import sessionmaker
from src.base_tbl import Base
from database.engine import get_engine
import logging
from src.status_messages import Messages
import os



@pytest.fixture(scope="module")
def engine_fixture():
    '''
    Diese Methode legt die DB für die Tests fest.
    '''
    # Pfad zur DB
    db_path = "C:/Users/liebs/Dev/python/HausarbeitPython/data/sqlite_db/database.db"

    # Erzeugt die Engine und gibt sie zurück
    return get_engine(db_path)

@pytest.fixture(scope="module")
def db_session(engine_fixture):
    '''
    Diese Methode setzt die DB auf einen bekannten Zustand vor dem Test. - Setup
    Der Test kann dann mit Testdaten ausgeführt werden. 
    Nach dem Test wird die Kotrolle der Session an diese Methode zurückgegeben, 
    anschließend wird der Ausgangstzustand wiederhergestellt. - Teardown
    '''
    Base.metadata.create_all(engine_fixture)
    Session = sessionmaker(bind=engine_fixture)
    session = Session()
    yield session  # Gibt die Kontrolle an den Test zurück

    # Teardown
    # Versuch die Tabelle zu löschen und den Ausgangszustand wiederherzustellen:
    try:
        session.close()
        Base.metadata.drop_all(engine_fixture)
        logging.info(Messages.TABLE_DROPPED.value)
    except Exception as e:
        # Error Nachricht, wenn dies nicht klappt.
        logging.error(Messages.ERROR_TABLE_DROPPED.value.format(error=e))
        raise