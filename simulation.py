import matplotlib.pyplot as plt
import numpy as np
import math

fig1, ax1 = plt.subplots(figsize=(10,7))


def simulation(path, vehicle):
    ax1.clear()

    ax1.plot(path.cx, path.cy, linewidth=2, label='Path')
    ax1.plot(vehicle.traj_x, vehicle.traj_y, linewidth=2, label='Vehicle trajectory')
    ax1.plot(vehicle.x, vehicle.y)

    ax1.set_title("Vehicle path tracking assignment")
    ax1.set_xlabel("Global X")
    ax1.set_ylabel("Global Y")
    ax1.legend()
    ax1.grid()

    plt.pause(0.01)


def show_results(path, vehicle):

    fig1.show()

    fig2, ax2 = plt.subplots()

    TimeListPsi = np.arange(0, len(vehicle.traj_psi), 1) # a list length of all psi samples, with dt spaces

    ax2.clear()

    vehicle.traj_psi = np.asarray(vehicle.traj_psi) * (180/math.pi) # convert list from rad to deg

    ax2.plot((TimeListPsi / 10), vehicle.traj_psi, "-r")
    ax2.set_title("Vehicle Yaw position over time")
    ax2.set_xlabel("Time[s]")
    ax2.set_ylabel("Yaw [deg]")
    ax2.grid(True)
    fig2.show()

    plt.show()