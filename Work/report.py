# report.py
#
# Exercise 2.4 & 6
import csv


def read_portfolio(filename):
    """
    Opens a given portfolio file and 
    reads it into a list of dictionaries
    """
    portfolio = []
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)  # Skip the header row
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    """
    Reads a set of prices such as a dict. where the keys 
    of the dict. are the stock names and the values in the
    dict. are the stock prices.
    """
    prices = []
    with open(filename) as file:
        rows = csv.reader(file)
        for row in rows:
            while len(row) == 2:
                price_data = {
                    'name': row[0],
                    'price': float(row[1])
                }

                prices.append(price_data)
                break

    return prices


def compute(filename, filename_prices):
    """
    Computes the gain/loss for each stock in the portfolio
    based on the current prices.
    """
    gain_loss_report = []
    portfolio = read_portfolio(filename)
    prices = read_prices(filename_prices)
    price_dict = {price['name']: price['price'] for price in prices}
    current_value = 0.0

    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        purchase_price = holding['price']
        current_price = price_dict.get(name, 0)
        current_value += current_price * shares

        gain_loss = round((current_price - purchase_price) * shares, 2)
        gain_loss_report.append({
            'name': name,
            'shares': shares,
            'purchase_price': purchase_price,
            'current_price': current_price,
            'gain_loss': gain_loss
        })

    return gain_loss_report, current_value
