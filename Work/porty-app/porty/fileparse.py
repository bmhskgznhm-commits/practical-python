# fileparse.py
import csv
from pprint import pprint
import logging
log = logging.getLogger(__name__)


def parse_file(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a file into a list of records
    :param lines: A list of strings representing the lines in the file
    :param select: A list of column names to select (optional)
    :param types: A list of functions to convert column values (optional)
    :param has_headers: A boolean indicating if the file has headers (optional)
    :param delimiter: The delimiter used in the file (optional)
    :return: A list of dictionaries or a tuple representing the records in a file
    """
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')
    if types and not isinstance(types, list):
        raise TypeError('types must be a list of functions')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip empty rows
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [row[index] for index in indices]

        # Apply type conversion to the row if specified
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple depending on whether headers are present
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
