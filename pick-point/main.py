from gui import plot
from data_types import Point

points = list(Point(x, x*x) for x in range(10))

plot(points)
