import unittest
from translator import english_to_french, french_to_english

class TestTranslationFunctions(unittest.TestCase):

    def test_english_to_french(self):
        # null check (nothing provided)
        self.assertEqual(english_to_french(), '')
        # null check (provided empty string '')
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_french_to_english(self):
        # null check (nothing provided)
        self.assertEqual(french_to_english(), '')
        # null check (provided empty string '')
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()