#!/usr/bin/python3
"""Unittest for class Review
"""
import unittest
import datetime
import os


from models.review import Review



class TestReview(unittest.TestCase):
    """
    Test case class to validate the ID generation of Review class.
    """

    def test_place_id(self):
        r = Review()
        self.assertEqual(type(r.place_id), str)

    def test_user_id(self):
        r = Review()
        self.assertEqual(type(r.user_id), str)

    def test_text(self):
        r = Review()
        self.assertEqual(type(r.text), str)

    def test_idType(self):
        r1 = Review()
        self.assertEqual(type(r1.id), str)

    def test_id0(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_created_atType(self):
        r1 = Review()
        self.assertEqual(type(r1.created_at), datetime.datetime)

    def test_created_at0(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.created_at, r2.created_at)

    def test_updated_atType(self):
        r1 = Review()
        self.assertEqual(type(r1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.updated_at, r2.updated_at)

    def test_upd_created_at(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.created_at, r2.updated_at)
    
    def test_kwargs(self):
        r = Review()
        c = r.to_dict()
        c_new = Review(**c)
        self.assertEqual(c_new.__str__(), r.__str__())

    def test_kwargsType(self):
        r = Review()
        c = r.to_dict()
        c_new = Review(**c)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        r = Review()
        c = r.to_dict()
        c_new = Review(**c)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        r = Review()
        c = r.to_dict()
        c_new = Review(**c)
        self.assertFalse(r is c_new)

class TestReview_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of Review class.
    """

    def test_str1(self):
        r = Review()
        self.assertEqual(r.__str__(), f"[{r.__class__.__name__}] ({r.id}) {r.__dict__}")

    def test_str2(self):
        r = Review()
        r.name = "My First Model"
        r.my_number = 89
        self.assertEqual(r.__str__(), f"[{r.__class__.__name__}] ({r.id}) {r.__dict__}")

    def test_strErr(self):
        r = Review()
        with self.assertRaises(TypeError):
            r.__str__(4)

    
class TestReview_save(unittest.TestCase):
    """
    Test case class to validate the save method of Review class.
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
        r = Review()
        r.name = "My First Model"
        r.my_number = 89
        updated_at_before_save = r.updated_at
        r.save()
        updated_at_after_save = r.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        r = Review()
        r.name = "My First Model"
        r.my_number = 89
        created_at_before_save = r.created_at
        r.save()
        created_at_after_save = r.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        r = Review()
        r.name = "My First Model"
        r.my_number = 89
        str_before_save = r.__str__()
        r.save()
        str_after_save = r.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestReview_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of Review class.
    """

    def test_todict(self):
        r = Review()
        
        dict = dict = {
            'id': r.id,
            'created_at': r.created_at.isoformat(),
            'updated_at': r.updated_at.isoformat(),
            '__class__': r.__class__.__name__,
        }
        self.assertEqual(r.to_dict(), dict)

    def test_todictType(self):
        r = Review()
        c = r.to_dict()
        self.assertEqual(type(c["created_at"]), str)

    def test_todictType2(self):
        r = Review()
        c = r.to_dict()
        self.assertEqual(type(c["updated_at"]), str)
    
    def test_dictErr(self):
        r = Review()
        with self.assertRaises(TypeError):
            r.to_dict(5)
