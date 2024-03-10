from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import sessionmaker
from .base_tbl import Base


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
    id = Column(Integer, primary_key=True)  # Identifier
    x_punkt = Column(Float)  # X-Koordinate Test
    y_punkt = Column(Float)  # Y-Koordinate Test
    abweichung = Column(Float)  # Abweichung von der idealen Funktion
    y_Ideal = Column(String)  # Name der Idealen Funktion
    
    @classmethod
    def add_df_to_tbl(cls, df, engine):
        '''
        Diese Methode fügt ein Dataframe an die Tabelle an. Das Dataframe muss, 
        wie oben beschrieben mindestens die Spalten  x, y, best_ideal, min_Abweichung enhalten
        Methodenparameter:
            - cls: Aufruf der Klasse selbst, da Klassenmethode
            - df: Padas Dataframe, dass die Daten enthält die angefgt werden sollen
            - engine: SQLite Datenbank in der die Tabelle angefügt werden soll
        
        
        '''
        # Umwandeln des DataFrames in das gewünschte Format und Einfügen in die DB
        records = df.to_dict('records')  # Wandelt den DataFrame in eine Liste von Dictionaries um
        for record in records:
            insert_dict = {
                'x_punkt': record['x'],
                'y_punkt': record['y'],
                'abweichung': record['min_Abweichung'],
                'y_Ideal': record['best_ideal']
            }
            # Erstellen des Objekts für die Einfügung
            obj = cls(**insert_dict)  # Entpacken der Werte des Dictionaries über den Konstuktor der Klasse obj
            engine.session.add(obj)  # Anfügen von obj an die Tabelle
        engine.session.commit()  # Änderungen in der Datenbank speichern