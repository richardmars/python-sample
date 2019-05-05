from gui import plot
from data_types import Point
from datasource import read_points

points = read_points("test.xlsx")

plot(points)
