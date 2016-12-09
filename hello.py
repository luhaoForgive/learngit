import time
import matplotlib.pyplot as plt
# import Variables
# coding: utf-8



def  draw_line():
    plt.ion()
    x1=0
    y1=0
    i=0
    plt.figure()
    plt.grid()
    plt.title("Real time current")
    plt.ylabel("mA")
    plt.xlabel("Time")
    while 1:
        # while Variables.is_draw:
            time.sleep(0.5)
            # device.read_values(uimeter)
            # Variables.volt = device.voltage
            # Variables.mah = device.power_mah
            # Variables.mwh = device.power_mwh
            # Variables.temp =device.temperature_c
            x2 = i
            # y2 = device.current
            y2 = 10
            plt.plot([x1,x2],[y1,y2],color='black')
            plt.draw()
            x1 = x2
            y1 = y2
            i= i+0.5
        # time.sleep(1)
    plt.ioff()


# Variables.is_draw = 1

draw_line()