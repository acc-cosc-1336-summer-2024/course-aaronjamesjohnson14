#
import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_three_roles(self):
        
        die = Die()

        for i in range(1 , 4):

            die.roll()
            role_value = die.get_rolled_value()

            self.assertEqual(True, role_value <= 6 and role_value >= 1)

            




