"""
图形界面
"""
from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt

def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    points = list(p for p in all_points if min(x1, x2) < p.x < max(x1, x2) and min(y1, y2) < p.y < max(y1, y2))
    # points = list(p for p in all_points if p.x > 0)
    for point in points:
        print(str(point))


def toggle_selector(event):
    print(' Key pressed.', event.key)
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print(' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print(' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)


def plot(points):
    fig, current_ax = plt.subplots() # make a new plotting range
    global all_points
    all_points = points
    x = list(point.x for point in points)
    y = list(point.y for point in points)
    plt.scatter(x, y)  # plot something

    print("\n      click  -->  release")

    # drawtype is 'box' or 'line' or 'none'
    toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                           drawtype='box', useblit=False,
                                           button=[1, 3],  # don't use middle button
                                           spancoords='pixels',
                                           minspanx=5, minspany=5,
                                           interactive=True)
    plt.connect('key_press_event', toggle_selector)
    plt.show()
