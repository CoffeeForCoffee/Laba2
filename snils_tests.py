import unittest
import os
from Laba2 import is_valid_snils, find_snils_in_file

# Тестирование
class TestSnilsFunctions(unittest.TestCase):
    # Тесты на правильный снилс
    def test_valid_snils(self):
        self.assertTrue(is_valid_snils("123-456-789 01"))
        self.assertTrue(is_valid_snils("880-055-535 35"))
        self.assertTrue(is_valid_snils("666-666-666 36"))
        self.assertTrue(is_valid_snils("000-000-000 00"))

    # Тесты на неправильный снилс
    def test_invalid_snils(self):
        self.assertFalse(is_valid_snils("12345678901"))
        self.assertFalse(is_valid_snils("123-45-6789 01"))
        self.assertFalse(is_valid_snils("TUS-OVA-ONE <3"))
        self.assertFalse(is_valid_snils(""))

    #Тесты для поиска в файле
    def test_find_snils_in_file(self):
        # Создаем тестовый файл для проверки
        test_filename = "test_snils.txt"
        with open(test_filename, "w", encoding="utf-8") as file:
            file.write("123-456-789 01\n")
            file.write("880-055-535 35\n")
            file.write("amogus??\n")
            file.write("666-666-666 36\n")

        # Проверяем, что там корректные снилсы
        found_snils = find_snils_in_file(test_filename)
        self.assertEqual(found_snils, ["123-456-789 01", "880-055-535 35", "666-666-666 36"])

        os.remove(test_filename)

if __name__ == "__main__":
    unittest.main()