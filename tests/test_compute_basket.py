import unittest

from ekinox_technical_test import compute_basket


class TestComputeBasket(unittest.TestCase):
    def test_case_1(self):
        """
        Test 3 UNIQUE movies from franchise
        """
        data = ['Back to the Future 1',
                'Back to the Future 2', 'Back to the Future 3']
        base_price = 20
        franchises = [{'name': 'Back to the Future',
                       'price': 15, 'discount_per_movie': {2: 10, 3: 20}}]
        result = compute_basket.compute_basket_price(
            data, base_price, franchises)
        self.assertEqual(result, 36)

    def test_case_2(self):
        """
        Test 2 UNIQUE movies from franchise
        """
        data = ['Back to the Future 1', 'Back to the Future 3']
        base_price = 20
        franchises = [{'name': 'Back to the Future',
                       'price': 15, 'discount_per_movie': {2: 10, 3: 20}}]
        result = compute_basket.compute_basket_price(
            data, base_price, franchises)
        self.assertEqual(result, 27)

    def test_case_3(self):
        """
        Test 1 movie from franchise
        """
        data = ['Back to the Future 1']
        base_price = 20
        franchises = [{'name': 'Back to the Future',
                       'price': 15, 'discount_per_movie': {2: 10, 3: 20}}]
        result = compute_basket.compute_basket_price(
            data, base_price, franchises)
        self.assertEqual(result, 15)

    def test_case_4(self):
        """
        Test 3 UNIQUE movies from franchise + 1 duplicate movie from franchise
        """
        data = ['Back to the Future 1', 'Back to the Future 2',
                'Back to the Future 3', 'Back to the Future 2']
        base_price = 20
        franchises = [{'name': 'Back to the Future',
                       'price': 15, 'discount_per_movie': {2: 10, 3: 20}}]
        result = compute_basket.compute_basket_price(
            data, base_price, franchises)
        self.assertEqual(result, 48)

    def test_case_5(self):
        """
        Test 3 UNIQUE movies from franchise + 1 movie not from franchise
        """
        data = ['Back to the Future 1', 'Back to the Future 2',
                'Back to the Future 3', 'La chèvre']
        base_price = 20
        franchises = [{'name': 'Back to the Future',
                       'price': 15, 'discount_per_movie': {2: 10, 3: 20}}]
        result = compute_basket.compute_basket_price(
            data, base_price, franchises)
        self.assertEqual(result, 56)

    def test_case_6(self):
        """
        Test 2 UNIQUE movies from franchise + 1 duplicate movie from franchise
        """
        data = ['Back to the Future 1',
                'Back to the Future 2', 'Back to the Future 2']
        base_price = 20
        franchises = [{'name': 'Back to the Future',
                       'price': 15, 'discount_per_movie': {2: 10, 3: 20}}]
        result = compute_basket.compute_basket_price(
            data, base_price, franchises)
        self.assertEqual(result, 40.5)


if __name__ == '__main__':
    unittest.main()
