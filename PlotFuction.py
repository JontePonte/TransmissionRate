
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider


def plot_values(data):
    """ plot the results in a nice graph """

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.5)
    sp, = plt.plot(self.t, self.S_l, color="blue")
    plt.axis([0, self.time_max, 0, 1])

    ax_slider1 = plt.axes([0.2, 0.2, 0.7, 0.05])
    s_trans = Slider(ax=ax_slider1,
                     label="Transmission",
                     valmin=0,
                     valmax=10)

    ax_slider2 = plt.axes([0.2, 0.1, 0.7, 0.05])
    s_recov = Slider(ax=ax_slider2,
                     label="Recovery",
                     valmin=0,
                     valmax=10)

    plt.show()

    while True:
        self.transmission = s_trans.val
        self.simulate()
        plt.draw()