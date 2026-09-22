# report.py
import sys
from . import fileparse
from . import tableformat
from . import portfolio


def read_portfolio(filename, **opts):
    """
    Opens a given portfolio file and
    reads it into a list of dictionaries
    :param filename: The name of the file containing the portfolio data.
    :return: A list of dictionaries, each representing a stock holding with keys 'name', 'shares', and 'price'.
    """
    with open(filename) as lines:
        return portfolio.Portfolio.from_file(lines, **opts)


def read_prices(filename):
    """
    Reads a set of prices such as a dict. where the keys
    of the dict. are the stock names and the values in the
    dict. are the stock prices.
    :param filename: The name of the CSV file containing the stock prices.
    :return: A dictionary mapping stock names to their current prices.
    """
    with open(filename) as lines:
        return dict(fileparse.parse_file(lines, types=[str, float], has_headers=False))


def compute(filename, filename_prices):
    """
    Computes the gain/loss for each stock in the portfolio
    based on the current prices.
    :param filename: The name of the CSV file containing the portfolio data.
    :param filename_prices: The name of the CSV file containing the current stock prices.
    :return: A tuple containing:
             - A list of dictionaries with gain/loss information for each holding.
             - The current value of the portfolio.
             - The total gain/loss for the portfolio.
    """
    gain_loss_report = []  # Store the gain/loss result for each holding
    portfolio = read_portfolio(filename)
    prices = read_prices(filename_prices)
    price_dict = prices
    current_value = 0.0  # Running total of current portfolio value

    # Compare each holding's purchase price to the current market price.
    for holding in portfolio:
        name = holding.name
        shares = holding.shares
        purchase_price = holding.price
        current_price = price_dict.get(name, 0)  # Use 0 if a price is missing
        current_value += current_price * shares  # Add this holding's current value

        # Compute the gain or loss for this individual stock.
        gain_loss = round((current_price - purchase_price) * shares, 2)
        gain_loss_report.append({
            'name': name,
            'shares': shares,
            'purchase_price': purchase_price,
            'current_price': current_price,
            'gain_loss': gain_loss
        })
        total_gain_loss = round(sum(item['gain_loss']
                                    # Running total across holdings
                                    for item in gain_loss_report), 2)

    return gain_loss_report, current_value, total_gain_loss


def make_report(portfolio, prices):
    """
    Takes a list of stocks and dictionary of prices as input
    and returns a list of tuples containing the rows of the
    table above.
    :param portfolio: A list of Stock objects representing the stock holdings.
    :param prices: A dictionary mapping stock names to their current prices.
    :return: A list of tuples, each containing (name, shares, current_price, change)
    """
    report = []  # Final rows to print in the summary table

    # Create a compact tuple for each stock with live price and change.
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        report.append(summary)

    return report


def print_report1(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tupels.
    :param reportdata: A list of tuples, each containing (name, shares, price, change).
    :param formatter: A TableFormat instance to handle the formatting of the table.
    '''
    formatter.title(f"{'-'*15} {'Stock Report'} {'-'*15}")
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:.2f}', f'{change:.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    """
    Generates and prints a report of the stock portfolio.
    :param portfolio_file: The name of the CSV file containing the portfolio data.
    :param prices_file: The name of the CSV file containing the current stock prices.
    """
    # Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    # Create the report data
    report = make_report(portfolio, prices)

    # Format and print the report
    formatter = tableformat.create_table_formatter(fmt)
    print_report1(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    main(sys.argv)
