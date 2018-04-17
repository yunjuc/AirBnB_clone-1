#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = 'amenities'
    if getenv('DBStorage') == 'db':
        name = Column(String(128), nullable=False)
        from models.place import place_amenity
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ""
