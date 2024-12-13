import unittest
from date import is_valid_date, find_dates_in_text

class TestDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(is_valid_date("28.02.2024"))
        self.assertTrue(is_valid_date("29.02.2020"))  # Високосный год
        self.assertTrue(is_valid_date("01.01.2000"))

    def test_invalid_date(self):
        self.assertFalse(is_valid_date("30.02.2024"))  # Февраль не может иметь 30 дней
        self.assertFalse(is_valid_date("31.04.2023"))  # Апрель имеет только 30 дней
        self.assertFalse(is_valid_date("29.02.2023"))  # Невисокосный год

    def test_find_dates_in_text(self):
        text = "28.02.2024 и 30.02.2024, а также 31.04.2023."
        expected_dates = ["28.02.2024"]
        self.assertEqual(find_dates_in_text(text), expected_dates)

if __name__ == '__main__':
    unittest.main()
