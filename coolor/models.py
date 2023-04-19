from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Pallete(Base):

    __tablename__ = "pallete"

    id = Column(Integer,primary_key=True,index=True)
    color1 = Column(String)
    color2 = Column(String)
    color3 = Column(String)
    color4 = Column(String)
    color5 = Column(String) 