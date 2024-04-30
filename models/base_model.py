#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """The base class for all storage objects"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel
        Args:
            *args: Unused
            **kwargs: Key/value pairs of attributes
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = val

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Print/str representation of the BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into a dictionary"""
        dictionary = {}
        for key, val in self.__dict__.items():
            if key != "_sa_instance_state":
                dictionary[key] = val
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)