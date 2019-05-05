import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets  import RectangleSelector

xdata = np.linspace(0,9*np.pi, num=301)
ydata = np.sin(xdata)*np.cos(xdata*2.4)

fig, ax = plt.subplots()
line, = ax.plot(xdata, ydata)
point, = ax.plot([],[], marker="o", color="crimson")
text = ax.text(0,0,"")

def line_select_callback(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata

    mask= (xdata > min(x1,x2)) & (xdata < max(x1,x2)) & \
          (ydata > min(y1,y2)) & (ydata < max(y1,y2))
    xmasked = xdata[mask]
    ymasked = ydata[mask]

    if len(xmasked) > 0:
        xmax = xmasked[np.argmax(ymasked)]
        ymax = ymasked.max()
        tx = "xmax: {:.3f}, ymax {:.3f}".format(xmax,ymax)
        point.set_data([xmax],[ymax])
        text.set_text(tx)
        text.set_position((xmax,ymax))
        fig.canvas.draw_idle()


rs = RectangleSelector(ax, line_select_callback,
                       drawtype='box', useblit=False, button=[1],
                       minspanx=5, minspany=5, spancoords='pixels',
                       interactive=True)

plt.show()