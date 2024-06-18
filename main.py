# Importing needed classes
from Environment import *
from simulation import *


def main():
    TargetPath = path(50)

    while(True):
        simulation(TargetPath)


if __name__ == "__main__":
    main()