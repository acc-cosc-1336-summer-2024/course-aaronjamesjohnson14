import unittest

from src.examples.h_strings.strings import test_config
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
        

    def test_get_hamming_distance(self):
        self.assertEqual(7,get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))

    
    def test_get_dna_compliment(self):
        self.assertEqual("ACCGGGTTTT", get_dna_complement("AAAACCCGGT"))