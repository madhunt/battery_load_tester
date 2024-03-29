#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    ''''''

    # get location to data file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(dir_path, "DATAFILE.TXT")

    data = np.loadtxt(data_path)

    # sample rate is 1000 ms
    t_samp = 1     # sec
    t_max = len(data) / t_samp / 3600 # hr
    t = np.linspace(0, t_max, len(data))


    fig, ax = plt.subplots(1, 1, tight_layout=True)

    ax.plot(t, data)

    ax.set_ylim([1.0, 1.25])

    ax.set_xlabel("Time (hr)")
    ax.set_ylabel("Voltage (V)")
    ax.grid()

    plt.show()

    return


if __name__ == "__main__": 
    main()