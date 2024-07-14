#

import unittest

from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_get_p_distance(self):

        test_list_1 = ['T','T','T','C','C','A','T','T','T','A']
        test_list_2 = ['G','A','T','T','C','A','T','T','T','C']

        self.assertEqual(.4, get_p_distance(test_list_1, test_list_2))

    def test_get_p_distance_matrix(self):

        test_matrix_list = [

            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
]
        
        test_matrix_expected_results = [
                    
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
]
        self.assertEqual(test_matrix_expected_results, get_p_distance_matrix(test_matrix_list))
