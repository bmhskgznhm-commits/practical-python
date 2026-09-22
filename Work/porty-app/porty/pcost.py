# pcost.py

import sys
from . import report


def portfolio_cost(filename):
    '''
    Computes total cost (shares * price) of a portfolio file
    :param filename: The name of the file containing the portfolio data.
    :return: The total cost of the portfolio.
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print(f'TOTAL COST: ${portfolio_cost(filename):,.2f}')


if __name__ == '__main__':
    main(sys.argv)
