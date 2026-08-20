# report.py
# NEED TO ADD COMMENTS AND ADDITIONAL INFO TO F'NS
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
    prices = {}
    with open(filename) as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

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
        total_gain_loss = round(sum(item['gain_loss']
                                for item in gain_loss_report), 2)

    return gain_loss_report, current_value, total_gain_loss


def make_report(portfolio, prices):
    """
    Takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples containing the rows of the 
    table above.
    """
    report = []

    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)

    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

print(f"{'-'*15} {'Stock Report'} {'-'*15}")
headers = ('Name', 'Shares', 'Price', 'Change')
print(
    f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f"{'-'*10} {'-'*10} {'-'*10} {'-'*10}")
for row in report:
    print(f"{row[0]:>10s} {row[1]:>10d} {'$' + f'{row[2]:.2f}':>10s} {
          '$' + f'{row[3]:.2f}':>10s}")
