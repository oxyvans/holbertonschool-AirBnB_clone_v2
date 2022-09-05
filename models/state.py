#!/usr/bin/python3
"""State class for AirBnb project"""
from os import getenv
import models
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

    else:
        if models.storage != "db":
            @property
            def cities(self):
                """ cities """
                citiesList = []
                for city in models.storage.all(City).values():
                    if self.id == city.state_id:
                        citiesList.append(models.storage.all(City)[city])
                return citiesList
