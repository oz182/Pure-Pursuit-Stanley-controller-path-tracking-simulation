from Environment import *

from simulation import *

def main():
    # Create a new environment, add obstacles and goal.
    envFrame = Env(40, 30)

    while(True):
        simulation(envFrame)


if __name__ == "__main__":
    main()