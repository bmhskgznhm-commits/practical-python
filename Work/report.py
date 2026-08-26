# report.py
import sys
import fileparse


def read_portfolio(filename):
    """
    Opens a given portfolio file and
    reads it into a list of dictionaries
    :param filename: The name of the file containing the portfolio data.
    :return: A list of dictionaries, each representing a stock holding with keys 'name', 'shares', and 'price'.
    """
    return fileparse.parse_file(filename, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename):
    """
    Reads a set of prices such as a dict. where the keys
    of the dict. are the stock names and the values in the
    dict. are the stock prices.
    :param filename: The name of the CSV file containing the stock prices.
    :return: A dictionary mapping stock names to their current prices.
    """
    return dict(fileparse.parse_file(filename, types=[str, float], has_headers=False))


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
        name = holding['name']
        shares = holding['shares']
        purchase_price = holding['price']
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
    :param portfolio: A list of dictionaries representing the stock holdings.
    :param prices: A dictionary mapping stock names to their current prices.
    :return: A list of tuples, each containing (name, shares, current_price, change).
    """
    report = []  # Final rows to print in the summary table

    # Create a compact tuple for each stock with live price and change.
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)

    return report


def print_report(report):
    """
    Prints a formatted report of the stock portfolio.
    :param report: A list of tuples, each containing (name, shares, current_price, change).
    """
    print(f"{'-'*15} {'Stock Report'} {'-'*15}")  # Title banner
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f"{'-'*10} {'-'*10} {'-'*10} {'-'*10}")  # Divider line
    for row in report:
        # Print each row using fixed-width columns for alignment.
        print(
            f"{row[0]:>10s} {row[1]:>10d} {'$' + f'{row[2]:.2f}':>10s} {'$' + f'{row[3]:.2f}':>10s}")


if len(sys.argv) == 3:  # Use command-line arguments when both filenames are given
    portfolio_file = sys.argv[1]
    prices_file = sys.argv[2]
else:
    # Prompt for filenames and fall back to the default data files if blank.
    portfolio_file = input('Enter the portfolio filename: ')
    if portfolio_file == '':
        portfolio_file = 'C://Users//noahz//practical-python//Work//Data//portfolio.csv'
    prices_file = input('Enter the prices filename: ')
    if prices_file == '':
        prices_file = 'C://Users//noahz//practical-python//Work//Data//prices.csv'


def portfolio_report(portfolio_file, prices_file):
    """
    Generates and prints a report of the stock portfolio.
    :param portfolio_file: The name of the CSV file containing the portfolio data.
    :param prices_file: The name of the CSV file containing the current stock prices.
    """
    # Load data, build the report rows, and print the summary.
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)


# Run the report with the chosen files
portfolio_report(portfolio_file, prices_file)
