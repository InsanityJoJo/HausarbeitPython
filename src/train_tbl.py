from sqlalchemy import Column, Float, Integer
from .base_tbl import Base
from database.engine import engine


class Train(Base):
    __tablename__ = 'Trainingsdaten'
    id = Column(Integer, primary_key=True,)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

    @classmethod
    def add_df_to_tbl(cls, df):
        df.to_sql(cls.__tablename__, con=engine, if_exists='append', index=False)