#!/usr/bin/python3
"""Unittest for class State
"""
import unittest
import datetime
import os


from models.state import State



class TestState(unittest.TestCase):
    """
    Test case class to validate the ID generation of State class.
    """

    def test_name(self):
        s = State()
        self.assertEqual(type(s.name), str)

    def test_idType(self):
        s = State()
        self.assertEqual(type(s.id), str)

    def test_id0(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_created_atType(self):
        s1 = State()
        self.assertEqual(type(s1.created_at), datetime.datetime)

    def test_created_at0(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.created_at, s2.created_at)

    def test_updated_atType(self):
        s1 = State()
        self.assertEqual(type(s1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.updated_at, s2.updated_at)

    def test_upd_created_at(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.created_at, s2.updated_at)
    
    def test_kwargs(self):
        s = State()
        c = s.to_dict()
        c_new = State(**c)
        self.assertEqual(c_new.__str__(), s.__str__())

    def test_kwargsType(self):
        s = State()
        c = s.to_dict()
        c_new = State(**c)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        s = State()
        c = s.to_dict()
        c_new = State(**c)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        s = State()
        c = s.to_dict()
        c_new = State(**c)
        self.assertFalse(s is c_new)

class TestState_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of State class.
    """

    def test_str1(self):
        s = State()
        self.assertEqual(s.__str__(), f"[{s.__class__.__name__}] ({s.id}) {s.__dict__}")

    def test_str2(self):
        s = State()
        s.name = "StateName"
        s.my_number = 89
        self.assertEqual(s.__str__(), f"[{s.__class__.__name__}] ({s.id}) {s.__dict__}")
    

    def test_strErr(self):
        s = State()
        with self.assertRaises(TypeError):
            s.__str__(4)

    
class TestState_save(unittest.TestCase):
    """
    Test case class to validate the save method of State class.
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
        s = State()
        s.name = "StateName"
        s.my_number = 89
        updated_at_before_save = s.updated_at
        s.save()
        updated_at_after_save = s.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        s = State()
        s.name = "StateName"
        s.my_number = 89
        created_at_before_save = s.created_at
        s.save()
        created_at_after_save = s.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        s = State()
        s.name = "StateName"
        s.my_number = 89
        str_before_save = s.__str__()
        s.save()
        str_after_save = s.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestState_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of State class.
    """

    def test_todict(self):
        s = State()
        
        dict = dict = {
            'id': s.id,
            'created_at': s.created_at.isoformat(),
            'updated_at': s.updated_at.isoformat(),
            '__class__': s.__class__.__name__,
        }
        self.assertEqual(s.to_dict(), dict)

    def test_todictType(self):
        s = State()
        c = s.to_dict()
        self.assertEqual(type(c["created_at"]), str)

    def test_todictType2(self):
        s = State()
        c = s.to_dict()
        self.assertEqual(type(c["updated_at"]), str)
    
    def test_dictErr(self):
        s = State()
        with self.assertRaises(TypeError):
            s.to_dict(5)
