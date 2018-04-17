#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    amenities = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='place', viewonly=False)
    else:
        @property
        def reviews(self):
            '''Getter for reviews'''
            all_reviews = models.storage.all(Review)
            reviews = []
            for key, obj in all_reviews.items():
                if obj.places.id == self.id:
                    reviews.append(obj)
            return reviews

        @property
        def amenities(self):
            '''Getter for amenities, return amenity_ids'''
            all_amenities = models.storage.all(Amenity)
            for key, obj in all_amenities.items():
                if obj.id in self.amenity_ids:
                    amenities.append(obj)
            return amenities

        @amenities.setter
        def amenities(self, obj=None):
            '''Setter for amenity_ids'''
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
            else:
                return
