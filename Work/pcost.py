# pcost.py

import sys
import csv


def portfolio_cost(filename):
    '''
    Computes total cost (shares * price) of a portfolio file
    '''

    total_cost = 0.0

    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename: ')

cost = portfolio_cost(filename)
print(f'Total Cost: ${cost:,.2f}')
