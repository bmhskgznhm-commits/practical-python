# pcost.py

import sys
import csv


def portfolio_cost(filename):
    '''
    Computes total cost (shares * price) of a portfolio file
    '''

    total_cost = 0.0

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except ValueError:
                print('Bad row:', row)

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total Cost: ${cost:,.2f}')


# Exercise 1_27 'The Original'
total_cost = 0.0


with open('Data/portfolio.csv', 'rt') as file:
    headers = next(file)
    for line in file:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        total_cost += shares * price


print(f'Total Cost: ${total_cost:,.2f}')
