import matplotlib.pyplot as plt

def simulation(path, vehicle):
    plt.cla()

    plt.plot(path.cx, path.cy, linewidth=2, label='Path')
    plt.plot(vehicle.traj_x, vehicle.traj_y, linewidth=2, label='Vehicle trajectory')
    plt.plot(vehicle.x, vehicle.y)

    plt.title("Vehicle path tracking assignment")
    plt.legend()
    plt.grid()

    plt.pause(0.001)