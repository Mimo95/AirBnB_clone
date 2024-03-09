#!/usr/bin/python3
"""Unittest for class Place
"""
import unittest
import datetime
import os


from models.place import Place



class TestPlace(unittest.TestCase):
    """
    Test case class to validate the ID generation of Place class.
    """

    def test_name(self):
        p = Place()
        self.assertEqual(type(p.name), str)
    
    def test_city_id(self):
        p = Place()
        self.assertEqual(type(p.city_id), str)

    def test_user_id(self):
        p = Place()
        self.assertEqual(type(p.user_id), str)
    
    def test_description(self):
        p = Place()
        self.assertEqual(type(p.description), str)

    def test_number_rooms(self):
        p = Place()
        self.assertEqual(type(p.number_rooms), int)
    
    def test_number_bathrooms(self):
        p = Place()
        self.assertEqual(type(p.number_bathrooms), int)
    
    def test_max_guest(self):
        p = Place()
        self.assertEqual(type(p.max_guest), int)

    def test_price_by_night(self):
        p = Place()
        self.assertEqual(type(p.price_by_night), int)
    
    def test_latitude(self):
        p = Place()
        self.assertEqual(type(p.latitude), float)

    def test_longitude(self):
        p = Place()
        self.assertEqual(type(p.longitude), float)

    def test_amenity_ids(self):
        p = Place()
        self.assertEqual(type(p.amenity_ids), list)

    def test_idType(self):
        p = Place()
        self.assertEqual(type(p.id), str)

    def test_id0(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_created_atType(self):
        p1 = Place()
        self.assertEqual(type(p1.created_at), datetime.datetime)

    def test_created_at0(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.created_at, p2.created_at)

    def test_updated_atType(self):
        p1 = Place()
        self.assertEqual(type(p1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.updated_at, p2.updated_at)

    def test_upd_created_at(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.created_at, p2.updated_at)
    
    def test_kwargs(self):
        p = Place()
        c = p.to_dict()
        c_new = Place(**c)
        self.assertEqual(c_new.__str__(), p.__str__())

    def test_kwargsType(self):
        p = Place()
        c = p.to_dict()
        c_new = Place(**c)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        p = Place()
        c = p.to_dict()
        c_new = Place(**c)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        p = Place()
        c = p.to_dict()
        c_new = Place(**c)
        self.assertFalse(p is c_new)

class TestPlace_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of Place class.
    """
    def test_str1(self):
        p = Place()
        self.assertEqual(p.__str__(), f"[{p.__class__.__name__}] ({p.id}) {p.__dict__}")

    def test_str2(self):
        p = Place()
        p.name = "PName"
        p.description = "hello"
        self.assertEqual(p.__str__(), f"[{p.__class__.__name__}] ({p.id}) {p.__dict__}")
    
    def test_strErr(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.__str__(4)

    
class TestPlace_save(unittest.TestCase):
    """
    Test case class to validate the save method of Place class.
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
        p = Place()
        p.name = "PName"
        updated_at_before_save = p.updated_at
        p.save()
        updated_at_after_save = p.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        p = Place()
        p.name = "PName"
        created_at_before_save = p.created_at
        p.save()
        created_at_after_save = p.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        p = Place()
        p.name = "PName"
        str_before_save = p.__str__()
        p.save()
        str_after_save = p.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestPlace_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of Place class.
    """

    def test_todict(self):
        p = Place()
        
        dict = dict = {
            'id': p.id,
            'created_at': p.created_at.isoformat(),
            'updated_at': p.updated_at.isoformat(),
            '__class__': p.__class__.__name__,
        }
        self.assertEqual(p.to_dict(), dict)

    def test_todictType(self):
        p = Place()
        c = p.to_dict()
        self.assertEqual(type(c["created_at"]), str)

    def test_todictType2(self):
        p = Place()
        c = p.to_dict()
        self.assertEqual(type(c["updated_at"]), str)
    
    def test_dictErr(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.to_dict(5)
