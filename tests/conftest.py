import pytest
from sqlalchemy.orm import sessionmaker
from src.base_tbl import Base
from database.engine import engine
import logging
from src.status_messages import Messages



@pytest.fixture(scope="module")
def db_session():
    '''
    Diese Methode setzt die DB auf einen bekannten Zustand vor dem Test. - Setup
    Der Test kann dann mit Testdaten ausgeführt werden. 
    Nach dem Test wird die Kotrolle der Session an diese Methode zurückgegeben, 
    anschließend wird der Ausgangstzustand wiederhergestellt. - Teardown
    '''

    # Datenbank wird vor den Test gesetzt- Setup
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session  # Gibt die Kontrolle an den Test zurück

    # Teardown
    # Versuch die Tabelle zu löschen und den Ausgangszustand wiederherzustellen:
    try:
        session.close()
        Base.metadata.drop_all(engine)
        logging.info(Messages.TABLE_DROPPED.value)
    except Exception as e:
        # Error Nachricht, wenn dies nicht klappt.
        logging.error(Messages.ERROR_TABLE_DROPPED.value.format(error=e))
        raise