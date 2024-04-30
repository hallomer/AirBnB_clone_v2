#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """Defines a user's state"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """Get the list of city instances related to this state"""
        city_list = []
        for city in models.storage.all(models.City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list