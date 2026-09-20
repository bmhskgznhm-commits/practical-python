import stock
import fileparse


class Portfolio:
    '''
    A collection of stock holdings.
    '''

    def __init__(self):
        '''
        Initializes a new Portfolio instance.
        '''
        self._holdings = []

    @classmethod
    def from_file(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_file(
            lines, select=['name', 'shares', 'price'], types=[str, int, float], **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self

    def append(self, holding):
        '''
        Adds a new stock holding to the portfolio.
        :param holding: An instance of the Stock class representing a stock holding.
        :raises TypeError: If the provided holding is not an instance of the Stock class.
        '''
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a stock instance')
        self._holdings.append(holding)

    def __iter__(self):
        '''
        :return: An iterator over the portfolio's holdings.
        '''
        return self._holdings.__iter__()

    def __len__(self):
        '''
        :return: The number of holdings in the portfolio.
        '''
        return len(self._holdings)

    def __getitem__(self, index):
        '''
        :param index: The index of the holding to return.
        :return: The holding at the specified index.
        '''
        return self._holdings[index]

    def __contains__(self, name):
        '''
        Checks if a holding with the specified name is in the portfolio.
        :param name: The name of the holding to check for.
        :return: True if the holding is in the portfolio, False otherwise.
        '''
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self):
        '''
        :return: The total cost of all holdings in the portfolio.
        '''
        return sum(s.shares * s.price for s in self._holdings)

    def tabulate_shares(self):
        '''
        Tabulates the total number of shares for each stock in the portfolio.
        :return: A Counter object with the total number of shares for each stock in the portfolio.
        '''
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
