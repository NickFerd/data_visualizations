import unittest
from country_codes import get_country_code


class CountryCodesTestCase(unittest.TestCase):
    """Tests for 'country_codes.py'."""

    def test_COUNTRIES(self):
        """Test correct output for counties in Pygal dict.
            COUNTRIES"""
        code = get_country_code('Brazil')
        self.assertEqual(code, 'br')

    def test_other(self):
        """Test countries that are in other list"""
        code = get_country_code('Bolivia')
        self.assertEqual(code, 'bo')

    def test_no_result(self):
        code = get_country_code('AAAA')
        self.assertEqual(code, None)


if __name__ == '__main__':
    unittest.main()