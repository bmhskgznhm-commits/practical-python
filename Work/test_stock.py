import unittest
import stock


class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = stock.Stock('TestStock(GOOG)', 100, 490.1)

    def test_initialization(self):
        self.assertEqual(self.stock.name, 'TestStock(GOOG)')
        self.assertEqual(self.stock.shares, 100)
        self.assertEqual(self.stock.price, 490.1)

    def test_cost_calculation(self):
        self.assertEqual(self.stock.cost, 49010.0)

    def test_sell_shares(self):
        self.stock.sell(20)
        self.assertEqual(self.stock.shares, 80)

    def test_buy_shares(self):
        self.stock.buy(50)
        self.assertEqual(self.stock.shares, 150)

    def test_sell_negative_shares_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.stock.sell(-10)

    def test_buy_negative_shares_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.stock.buy(-5)

    def test_shares_type_error(self):
        with self.assertRaises(TypeError):
            self.stock.shares = 'not an integer'


if __name__ == '__main__':
    unittest.main()
