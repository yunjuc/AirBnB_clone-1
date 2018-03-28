#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import city
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", back_populates='state',
                              cascade='all, delete')
    else:
        @property
        def cities (self):
            '''
            Getter for cities
            '''
            all_cities = models.storage.all(City)
            cities = []
            print(all_cities)
            for key, obj in all_cities.items():
                if key == state_id:
                    cities.append(obj)
            return cities
