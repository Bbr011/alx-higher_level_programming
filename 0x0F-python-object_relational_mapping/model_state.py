#!/usr/bin/python3
"""the class definition of a State"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """states class"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement = True, unique = True, primery_key = True, nullable = False)
    name = Column(string(128), nullable = False)
