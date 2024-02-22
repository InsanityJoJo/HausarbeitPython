from sqlalchemy import Column, Float, Integer
from .base_tbl import Base


class Train(Base):
    __tablename__ = 'Trainingsdaten'
    id = Column(Integer, primary_key=True,)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)