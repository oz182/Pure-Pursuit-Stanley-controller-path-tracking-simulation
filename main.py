# Importing needed classes
from Environment import *
from simulation import *
from Vehicle import *
from PurePursuitAlgo import *


def main():
    TargetPath = path(PathLength=50)
    Vehicle = vehicle(x0=0.1,y0=0.1,psi0=0.0,v0=1.0)
    TrackingAlgo = PurePursuitAlgo(lookahead_distance=2.0)

    while(True):
        simulation(TargetPath, Vehicle)
        #SteeringCommand = TrackingAlgo.calculate_lookahead_point(TargetPath,Vehicle)
        SteeringCommand = 10
        Vehicle.set_steering_angle(SteeringCommand)
        Vehicle.update(0.2)
        print(Vehicle.pos)



if __name__ == "__main__":
    main()