import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(5*np.pi*t)
l, = plt.plot(t,s)

viewwindow = 0.1

axpos = plt.axes([0.25, 0.1, 0.65, 0.03])
axslider = Slider(axpos, '', t[0]+viewwindow, t[-1]-viewwindow, valinit=(t[-1]+t[0])/2.0)

def update(val):
    new_pos = axslider.val
    ax.set_xbound(new_pos-viewwindow, new_pos+viewwindow)
    fig.canvas.draw_idle()

update(axslider.val)
axslider.on_changed(update)

plt.show()