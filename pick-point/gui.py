"""
图形界面
"""
from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots() # make a new plotting range
selected_points = []


def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    points = list(p for p in all_points if min(x1, x2) < p.x < max(x1, x2) and min(y1, y2) < p.y < max(y1, y2))
    for point in points:
        if selected_points.__contains__(point):
            selected_points.remove(point)
        else:
            selected_points.append(point)
        print(str(point))

    # 将选中的坐标重新打印，显示出来
    offsets = np.c_[list(point.x for point in selected_points), list(point.y for point in selected_points)]
    selected_sc.set_offsets(offsets)


def toggle_selector(event):
    print(' Key pressed.', event.key)
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print(' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print(' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)





def plot(points):
    global all_points
    all_points = points
    x = list(point.x for point in points)
    y = list(point.y for point in points)
    ax.scatter(x, y)  # plot something
    global selected_sc
    selected_sc = ax.scatter([], [])
    selected_sc.set_color("yellow")

    print("\n      click  -->  release")

    # drawtype is 'box' or 'line' or 'none'
    toggle_selector.RS = RectangleSelector(ax, line_select_callback,
                                           drawtype='box', useblit=False,
                                           button=[1, 3],  # don't use middle button
                                           spancoords='pixels',
                                           minspanx=5, minspany=5,
                                           interactive=False)
    plt.connect('key_press_event', toggle_selector)
    plt.show()
