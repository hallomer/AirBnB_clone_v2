#!/usr/bin/python3
"""This module defines a class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id',
                                        onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True))


class Place(BaseModel, Base):
    """This class defines a place by various attributes"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place",
                           cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",
                             backref="place_amenities", viewonly=False)
