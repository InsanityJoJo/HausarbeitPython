from sqlalchemy import Column, Float, Integer
from .base_tbl import Base


class Result(Base):
    __tablename__ = 'Ergebnisse'
    id = Column(Integer, primary_key=True)   