# pcost.py

import sys
import report


def portfolio_cost(filename):
    '''
    Computes total cost (shares * price) of a portfolio file
    :param filename: The name of the file containing the portfolio data.
    :return: The total cost of the portfolio.
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s['shares'] * s['price'] for s in portfolio])


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename: ')
    if filename == '':
        filename = 'C://Users/noahz/practical-python/Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total Cost: ${cost:,.2f}')
