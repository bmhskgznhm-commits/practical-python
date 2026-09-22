# Exercises 4.1 - 4.4
from . import typedproperty


class Stock:
    name = typedproperty.String('name')
    shares = typedproperty.Integer('shares')
    price = typedproperty.Float('price')

    def __init__(self, name, shares, price):
        '''
        :param name: A string representing the stock name.
        :param shares: An integer representing the number of shares.
        :param price: A float representing the price per share.
        '''
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer for shares')
        self._shares = value

    @property
    def cost(self):
        '''
        Calculate the total cost of the stock.
        :returns: The total cost as a float.
        '''
        return self.shares * self.price

    def sell(self, shares):
        '''
        Sell a number of shares of the stock.
        :param shares: An integer representing the number of shares to sell.
        '''
        if shares < 0:
            raise ValueError("Number of shares to sell must be non-negative.")

        self.shares -= shares

    def buy(self, shares):
        '''
        Buy a number of shares of the stock.
        :param shares: An integer representing the number of shares to buy.
        '''
        if shares < 0:
            raise ValueError("Number of shares to buy must be non-negative.")

        self.shares += shares

    def __repr__(self):
        '''
        Return a string representation of the stock object.
        :returns: A string representing the stock object.
        '''
        return f'Stock({self.name!r}, {self.shares}, {self.price})'
