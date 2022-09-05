#!/usr/bin/python3
"""State class for AirBnb project"""
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class that creates states table"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, \
                              delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ cities """
            from models import storage
            citiesList = []
            for city in storage.all(City).values():
                if self.id == city.state_id:
                    citiesList.append(city)
            return citiesList
