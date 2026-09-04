class TableFormatter:
    def title(self, title):
        '''
        Emit the table title.
        :param title: A string representing the table title.
        '''
        raise NotImplementedError()

    def headings(self, headers):
        '''
        Emit the table headings.
        :param headers: A list of strings representing the table headings.
        '''
        raise NotImplementedError()

    def row(self, rows):
        '''
        Emit the table rows.
        :param rows: A list of tuples representing the table rows.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def title(self, title):
        print(title)

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(('-' * 10 + ' ')*len(headers))

    def row(self, rowdata):
        for r in rowdata:
            print(f"{r:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    def title(self, title):
        print(title)

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def title(self, title):
        print(f"<h1>{title}</h1>")

    def headings(self, headers):
        print("<table>")
        print("<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>")

    def row(self, rowdata):
        print("<tr>" + "".join(f"<td>{r}</td>" for r in rowdata) + "</tr>")


class FormatError(Exception):
    pass


def create_table_formatter(fmt):
    '''
    Create a table formatter based on the format string.
    :param fmt: A string representing the table format type ('txt', 'csv', or 'html').
    :returns: A table formatter instance corresponding to the specified format.
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format '{fmt}'")


def print_table(objects, formatter, headers=None):
    '''
    Make a nicely formatted table from a list of objects and attributes.
    :param objects: A list of objects containing the data to display in the table.
    :param formatter: A table formatter instance to use for formatting the table.
    :param headers: A list of strings representing the attributes to display as table headings.
    '''
    if headers:
        formatter.title("Stock Table")
        formatter.headings(headers)
    for obj in objects:
        rowdata = [str(getattr(obj, attr)) for attr in headers]
        formatter.row(rowdata)
