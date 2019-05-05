from xlrd import open_workbook
from data_types import Point


def read_points(filename):
    book = open_workbook(filename)
    position_sheet = book.sheet_by_index(0)
    value_sheet = book.sheet_by_index(1)

    d = dict()
    for row in range(1, position_sheet.nrows):
        key = position_sheet.cell(row, 0).value
        x = position_sheet.cell(row, 1).value
        y = position_sheet.cell(row, 2).value
        d[key] = Point(key, x, y)

    for row in range(1, value_sheet.nrows):
        key = value_sheet.cell(row, 0).value
        val = value_sheet.cell(row, 1).value
        d[key].val = val

    return d.values()


if __name__ == "__main__":
    points = read_points('test.xlsx')
    for point in points:
        print(point)
