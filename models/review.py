#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(600), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
