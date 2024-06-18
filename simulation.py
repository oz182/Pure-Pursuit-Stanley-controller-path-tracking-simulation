import matplotlib.pyplot as plt

TIME_INTERVAL = 1  # Global constant

fig, ax = plt.subplots(figsize=(10, 10))

def simulation(env):
    ax.clear()
    ax.set_xlim([0, env.width])
    ax.set_ylim([0, env.height])

    plt.plot(5,6)