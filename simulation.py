import matplotlib.pyplot as plt

def simulation(path, vehicle):
    plt.cla()
    plt.plot(path.cx, path.cy)
    plt.plot(vehicle.traj_x, vehicle.traj_y)
    plt.pause(0.001)