"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from child.models import Child


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


'''
class ChildCreateTest(TestCase):
    def create_child(self):
        child = Child(
            first_name='miha',
            last_name='piha',

        )
'''