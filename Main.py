""" A model of transmission rate in a population """

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider
from PlotFuction import *


class TransmissionRate:
    """ Create transmission curves based on transmission rate and recovery rate """

    def __init__(self):
        # Start values
        self.N = 1
        self.I_start = 0.001
        self.S_start = self.N - self.I_start
        self.R_start = 0
        self.D_start = 0

        # Transmission rate and recovery rate
        self.transmission = 3.2
        self.recovery = 0.23
        self.departure = 0.01

        # Additional variables
        self.infection_capacity = 0.3
        self.departure_without_help = 0.04

        # Time variables
        self.time = 0
        self.time_max = 25
        self.t = []

        # Resolution, high value ==> high resolution, must be integer
        self.resolution = 10

        # Variables
        self.I = self.I_start  # I for infected
        self.S = self.S_start  # S for susceptible
        self.R = self.R_start  # R for recovered
        self.D = self.D_start  # D for departed

        self.I_rate = 0
        self.R_rate = 0
        self.D_rate = 0

        # List for plot
        self.S_l = []
        self.I_l = []
        self.R_l = []
        self.D_l = []
        self.time_l = list(range(int(self.time_max * self.resolution)))

        # Run the calculations
        self.simulate()

        # Do the plot
        self.plot_results()

    def simulate(self):
        """ Do all the calculations and save results """
        while self.time < self.time_max:
            """ Calculate all the rates. Divide with resolution """
            # the infected growth rate is based on the number of infected and susceptible + transmission rate
            self.I_rate = self.transmission * self.I * self.S / self.resolution

            # Recovery rate is based on the number of infected and recovery rate
            self.R_rate = self.recovery * self.I / self.resolution

            # Departure rate is base on the number of infected and departure rate
            # The rate changes for Infected over the infection capacity
            if self.I <= self.infection_capacity:
                self.D_rate = self.departure * self.I / self.resolution
            elif self.I > self.infection_capacity:
                self.D_rate = (self.departure * self.infection_capacity
                               + self.departure_without_help * (self.I - self.infection_capacity)) / self.resolution

            """ Use the rates to calculate the next values and save them """
            # New values on susceptible, infected and recovered are calculated
            self.S = self.S - self.I_rate
            self.I = self.I + self.I_rate - self.R_rate - self.D_rate
            self.R = self.R + self.R_rate
            self.D = self.D + self.D_rate

            # Save values in lists
            self.S_l.append(self.S)
            self.I_l.append(self.I)
            self.R_l.append(self.R)
            self.D_l.append(self.D)

            self.time += 1 / self.resolution
        # Fix time variable
        self.t = []
        for time in self.time_l:
            self.t.append(time / self.resolution)

    def plot_results(self):
        """ plot the results in a nice graph """

        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.5)
        sp, = plt.plot(self.t, self.S_l, color="blue")
        ip, = plt.plot(self.t, self.I_l, color="red")
        rp, = plt.plot(self.t, self.R_l, color="green")
        dp, = plt.plot(self.t, self.D_l, color="brown")
        plt.axis([0, self.time_max, 0, 1])

        ax_slider1 = plt.axes([0.2, 0.2, 0.7, 0.05])
        s_trans = Slider(ax=ax_slider1,
                         label="Transmission",
                         valmin=0,
                         valmax=10,
                         valinit=self.transmission)

        ax_slider2 = plt.axes([0.2, 0.1, 0.7, 0.05])
        s_recov = Slider(ax=ax_slider2,
                         label="Recovery",
                         valmin=0,
                         valmax=10,
                         valinit=self.recovery)

        plt.show()

        def update(a):
            self.transmission = s_trans.val
            self.simulate()
            sp.set_data(self.t, self.S_l)
            fig.canvas.draw_idle()

        s_trans.on_changed(update())


run = TransmissionRate()
