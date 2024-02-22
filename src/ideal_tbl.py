from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from database.engine import engine


class Ideal(Base):
    __tablename__ = 'ideale_funktionen'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    # Dynamisch erzeugte y-Spalten wie zuvor besprochen
    
 
    @classmethod
    def add_df_to_tbl(cls, df):
        df.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)

# Füge dynamisch Spalten für y1 bis y50 hinzu
for i in range(1, 51):
    setattr(Ideal, f'y{i}', Column(Float))



