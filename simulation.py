import matplotlib.pyplot as plt

def simulation(path):
    plt.cla()
    plt.plot(path.cx, path.cy)
    plt.show()