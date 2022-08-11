#!/usr/bin/python3
"""
    Test Case For user Model and its Test
"""
from models.base_model import BaseModel
from models.user import User
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models


class TestUser(unittest.TestCase):
    """
        unitesst for user class
    """

    def issub_class(self):
        """
            test if User class is sub class of base model
        """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "update_at"))

    def test_email(self):
        """
            test class attribute email
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if models.sType == "db":
            self.assertEqual(user.email, None)
        else:
            pass

    def test_password(self):
        """
            test class attribute password
        """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        if models.sType == "db":
            self.assertEqual(user.password, None)
        else:
            pass

    def test_name(self):
        """
            test class atribute first_name and last_name
        """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertTrue(hasattr(user, "first_name"))
        if models.sType == "db":
            self.assertEqual(user.first_name, None)
            self.assertEqual(user.last_name, None)
        else:
            pass

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        user = User()
        dict_con = user.to_dict()
        self.assertEqual(dict_con["__class__"], "User")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            user.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            user.updated_at.strftime(time_format))
