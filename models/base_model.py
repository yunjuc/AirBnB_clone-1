#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import uuid
import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    '''
        Base class for other classes to be used for the duration.
    '''
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow(),
                        nullable=False)

    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
        else:
            try:
                kwargs["created_at"] = datetime.datetime\
                    .strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                kwargs["updated_at"] = datetime.datetime\
                    .strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            except:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.datetime.utcnow()
                self.updated_at = datetime.datetime.utcnow()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.isoformat()
        cp_dct['created_at'] = self.created_at.isoformat()
        try:
            cp_dct.pop("_sa_instance_state")
        except KeyError:
            pass
        return (cp_dct)

    def delete(self):
        '''
        Method to delete current instance from the storage
        '''
        models.storage.delete(self)
