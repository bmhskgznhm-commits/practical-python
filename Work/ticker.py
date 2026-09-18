from follow import follow
import csv
import report
import tableformat
import sys


def select_columns(rows, indices):
    '''
    Selects columns from a list of rows.
    :param rows: An iterable of rows.
    :param indices: A list of column indices to select.
    :yield: A row with only the selected columns.
    '''
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    '''
    Converts the types of values in a list of rows.
    :param rows: An iterable of rows.
    :param types: A list of types to convert to.
    :yield: A row with values converted to the specified types.
    '''
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    '''
    Converts a list of rows into a list of dictionaries.
    :param rows: An iterable of rows.
    :param headers: A list of column headers.
    :return: A dictionary for each row.
    '''
    return (dict(zip(headers, row)) for row in rows)


def parse_stock_data(lines):
    '''
    Parses stock data from a list of lines.
    :param lines: An iterable of lines containing stock data.
    :return: A list of dictionaries representing the parsed stock data.
    '''
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile, logfile, fmt):
    '''
    Displays stock data for a given portfolio.
    :param portfile: The name of the portfolio file.
    :param logfile: The name of the log file to follow.
    :param fmt: The format to display the data in.
    '''
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_table_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row(
            [row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


def main(args):
    '''
    The main entry point for the ticker program.
    :param args: A list of command-line arguments.
    '''
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])


if __name__ == '__main__':
    main(sys.argv)
