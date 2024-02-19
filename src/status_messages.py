from enum import Enum, auto

class Messages(Enum):
    '''
    Diese Klasse beinhaltet alle Systemnachrichten des Proramms.
    Hier werden Nachrichten angepasst.
    '''
    VALID_TEST = auto()  # Nachricht: validiert richtiges CVS Format für Testdaten
    VALID_TRAINING = auto()  # Nachricht: validiert richtiges CVS Format für Trainingsdaten
    VALID_IDEAL = auto()  # Nachricht: validiert richtiges CVS Format für Idealdaten
    INVALID_CSV_FORMAT = auto()  # Nachricht: Fehlermeldung bei falschem CVS Format
