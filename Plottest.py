import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider

vals = np.linspace(-np.pi,np.pi,100)
xgrid, ygrid = np.meshgrid(vals,vals)

def f(x, y, b):
    return np.sin(x * b)
b = 5

ax = plt.subplot(111)
plt.subplots_adjust(left=0.15, bottom=0.25)
fig = plt.imshow(f(xgrid, ygrid, b), cm.gray)
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

axb = plt.axes([0.15, 0.1, 0.65, 0.03])
sb = Slider(axb, 'b', 0.1, 10.0, valinit=b)


def update(val):
    fig.set_data(f(xgrid, ygrid, val))


sb.on_changed(update)


plt.show()