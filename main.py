# Importing needed classes
from Environment import *
from simulation import *
from Vehicle import *
from PurePursuitAlgo import *


def main():
    TargetPath = path(PathLength=100)
    Vehicle = vehicle(x0=0.1,y0=0.1,psi0=0.0,v0=1.0)
    TrackingAlgo = PurePursuitAlgo(TargetPath, Vehicle, lookahead_distance=1.5)

    while(True):
        simulation(TargetPath, Vehicle)
        SteeringCommand = TrackingAlgo.calculate_steering_angle()
        Vehicle.set_steering_angle(SteeringCommand)
        print(SteeringCommand)
        Vehicle.update(delta_t=0.2)


if __name__ == "__main__":
    main()