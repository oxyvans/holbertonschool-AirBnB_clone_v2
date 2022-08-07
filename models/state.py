#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import Base, BaseModel
from models.city import City
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state")

    if models.storageType != "db":
        @property
        def cities(self):
            """ getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            cities = []
            cityInstances = models.storage.all(City)
            for value in cityInstances.values():
                if value.state_id == self.id:
                    cities.append(value)
            return cities
