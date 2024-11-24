import unittest
from Laba2 import is_valid_snils

# Правильный ли снилс или нет
class TestSnilsFunctions(unittest.TestCase):
    def test_is_valid_snils(self):
        # Правильно
        self.assertTrue(is_valid_snils("123-456-789 01"))
        self.assertTrue(is_valid_snils("880-055-535 35"))
        self.assertTrue(is_valid_snils("666-666-666 36"))
        self.assertTrue(is_valid_snils("000-000-000 00"))
        # Неправильно
        self.assertFalse(is_valid_snils("12345678901"))
        self.assertFalse(is_valid_snils("123-45-6789 01"))
        self.assertFalse(is_valid_snils("TUS-OVA-ONE <3"))
        self.assertFalse(is_valid_snils(""))

if __name__ == "__main__":
    unittest.main()