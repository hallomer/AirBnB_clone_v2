#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """returns the list of Cities"""
            from models import storage
            cities_list = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
