from sqlalchemy import Column, Float, Integer
from .base_tbl import Base

class Test(Base):
    __tablename__ = 'Testdaten'
    id = Column(Integer, primary_key=True)


