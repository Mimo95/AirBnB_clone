#!/usr/bin/python3
"""Unittest for class City
"""
import unittest
import datetime
import os


from models.city import City



class TestCity(unittest.TestCase):
    """
    Test case class to validate the ID generation of City class.
    """

    def test_name(self):
        c = City()
        self.assertEqual(type(c.name), str)
    
    def test_state_id(self):
        c = City()
        self.assertEqual(type(c.state_id), str)

    def test_idType(self):
        c = City()
        self.assertEqual(type(c.id), str)

    def test_id0(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_created_atType(self):
        c1 = City()
        self.assertEqual(type(c1.created_at), datetime.datetime)

    def test_created_at0(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.created_at, c2.created_at)

    def test_updated_atType(self):
        c1 = City()
        self.assertEqual(type(c1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.updated_at, c2.updated_at)

    def test_upd_created_at(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.created_at, c2.updated_at)
    
    def test_kwargs(self):
        c = City()
        cc = c.to_dict()
        c_new = City(**cc)
        self.assertEqual(c_new.__str__(), c.__str__())

    def test_kwargsType(self):
        c = City()
        cc = c.to_dict()
        c_new = City(**cc)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        c = City()
        cc = c.to_dict()
        c_new = City(**cc)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        c = City()
        cc = c.to_dict()
        c_new = City(**cc)
        self.assertFalse(c is c_new)

class TestCity_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of City class.
    """

    def test_str1(self):
        c = City()
        self.assertEqual(c.__str__(), f"[{c.__class__.__name__}] ({c.id}) {c.__dict__}")

    def test_str2(self):
        c = City()
        c.name = "CityName"
        c.my_number = 89
        self.assertEqual(c.__str__(), f"[{c.__class__.__name__}] ({c.id}) {c.__dict__}")

    def test_strErr(self):
        c = City()
        with self.assertRaises(TypeError):
            c.__str__(4)

    
class TestCity_save(unittest.TestCase):
    """
    Test case class to validate the save method of City class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_update(self):
        c = City()
        c.name = "CityName"
        c.my_number = 89
        updated_at_before_save = c.updated_at
        c.save()
        updated_at_after_save = c.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        c = City()
        c.name = "CityName"
        c.my_number = 89
        created_at_before_save = c.created_at
        c.save()
        created_at_after_save = c.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        c = City()
        c.name = "CityName"
        c.my_number = 89
        str_before_save = c.__str__()
        c.save()
        str_after_save = c.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestCity_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of City class.
    """

    def test_todict(self):
        c = City()
        
        dict = dict = {
            'id': c.id,
            'created_at': c.created_at.isoformat(),
            'updated_at': c.updated_at.isoformat(),
            '__class__': c.__class__.__name__,
        }
        self.assertEqual(c.to_dict(), dict)

    def test_todictType(self):
        c = City()
        cc = c.to_dict()
        self.assertEqual(type(cc["created_at"]), str)

    def test_todictType2(self):
        c = City()
        cc = c.to_dict()
        self.assertEqual(type(cc["updated_at"]), str)
    
    def test_dictErr(self):
        c = City()
        with self.assertRaises(TypeError):
            c.to_dict(5)
