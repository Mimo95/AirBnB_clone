#!/usr/bin/python3
"""Unittest for class Amenity
"""
import unittest
import datetime
import os

from models.amenity import Amenity



class TestAmenity(unittest.TestCase):
    """
    Test case class to validate the ID generation of Amenity class.
    """

    def test_name(self):
        a = Amenity()
        self.assertEqual(type(a.name), str)

    def test_idType(self):
        a1 = Amenity()
        self.assertEqual(type(a1.id), str)

    def test_id0(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_created_atType(self):
        a1 = Amenity()
        self.assertEqual(type(a1.created_at), datetime.datetime)

    def test_created_at0(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.created_at, a2.created_at)

    def test_updated_atType(self):
        a1 = Amenity()
        self.assertEqual(type(a1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.updated_at, a2.updated_at)

    def test_upd_created_at(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.created_at, a2.updated_at)
    
    def test_kwargs(self):
        a = Amenity()
        c = a.to_dict()
        c_new = Amenity(**c)
        self.assertEqual(c_new.__str__(), a.__str__())

    def test_kwargsType(self):
        a = Amenity()
        c = a.to_dict()
        c_new = Amenity(**c)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        a = Amenity()
        c = a.to_dict()
        c_new = Amenity(**c)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        a = Amenity()
        c = a.to_dict()
        c_new = Amenity(**c)
        self.assertFalse(a is c_new)

class TestAmenity_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of Amenity class.
    """
    def test_str1(self):
        a = Amenity()
        self.assertEqual(a.__str__(), f"[{a.__class__.__name__}] ({a.id}) {a.__dict__}")

    def test_str2(self):
        a = Amenity()
        a.name = "My First Model"
        self.assertEqual(a.__str__(), f"[{a.__class__.__name__}] ({a.id}) {a.__dict__}")

    def test_strErr(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.__str__(4)

    
class TestAmenity_save(unittest.TestCase):
    """
    Test case class to validate the save method of Amenity class.
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
        a = Amenity()
        a.name = "My First Model"
        updated_at_before_save = a.updated_at
        a.save()
        updated_at_after_save = a.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        a = Amenity()
        a.name = "My First Model"
        created_at_before_save = a.created_at
        a.save()
        created_at_after_save = a.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        a = Amenity()
        a.name = "My First Model"
        str_before_save = a.__str__()
        a.save()
        str_after_save = a.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestAmenity_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of Amenity class.
    """

    def test_todict(self):
        a = Amenity()
        
        dict = dict = {
            'id': a.id,
            'created_at': a.created_at.isoformat(),
            'updated_at': a.updated_at.isoformat(),
            '__class__': a.__class__.__name__,
        }
        self.assertEqual(a.to_dict(), dict)

    def test_todictType(self):
        a = Amenity()
        c = a.to_dict()
        self.assertEqual(type(c["created_at"]), str)

    def test_todictType2(self):
        a = Amenity()
        c = a.to_dict()
        self.assertEqual(type(c["updated_at"]), str)
    
    def test_dictErr(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.to_dict(5)
