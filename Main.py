
""" A model of transmission rate in a population """
import matplotlib.pyplot as plt


class TransmissionRate:
    """ Create transmission curves based on transmission rate and recovery rate """
    def __init__(self):
        # Start values
        self.N = 1
        self.I_start = 0.001
        self.S_start = self.N - self.I_start
        self.R_start = 0

        # Transmission rate and recovery rate
        self.transmission = 3.2
        self.recovery = 0.23

        # Time variables
        self.time = 0
        self.time_max = 30

        # Resolution, high value ==> high resolution, must be integer
        self.resolution = 100

        # Variables
        self.I = self.I_start       # I for infected
        self.S = self.S_start       # S for susceptible
        self.R = self.R_start       # R for recovered

        self.I_rate = 0
        self.R_rate = 0

        # List for plot
        self.S_l = []
        self.I_l = []
        self.R_l = []
        self.time_l = list(range(int(self.time_max * self.resolution)))

        # Run the calculations
        self.simulate()

        # Do the plot
        self.plot_results()

    def simulate(self):
        """ Do all the calculations and save results """
        while self.time < self.time_max:

            # the infected growth rate is based on the number of infected and susceptible + transmission rate
            self.I_rate = self.transmission * self.I * self.S / self.resolution

            # Recovery rate is based on the number of infected and recovery rate
            self.R_rate = self.recovery * self.I / self.resolution

            # New values on susceptible, infected and recovered are calculated
            self.S = self.S - self.I_rate
            self.I = self.I + self.I_rate - self.R_rate
            self.R = self.R + self.R_rate

            # Save values in lists
            self.S_l.append(self.S)
            self.I_l.append(self.I)
            self.R_l.append(self.R)

            self.time += 1 / self.resolution

    def plot_results(self):
        """ plot the results in a nice graph """
        # Fix time variable
        t = []
        for time in self.time_l:
            t.append(time / self.resolution)

        # Do all the plot stuff
        plt.plot(t, self.S_l)
        plt.plot(t, self.I_l)
        plt.plot(t, self.R_l)

        plt.legend(labels=["Susceptible", "Infected", "Recovered"], loc="right")
        plt.title('Infection transmission rate')
        plt.xlabel('Time')
        plt.ylabel('Amount')
        plt.grid(True)
        plt.show()


run = TransmissionRate()
