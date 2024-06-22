# Importing needed classes and librarys
from Path import *
from simulation import *
from Vehicle import *
from PurePursuitAlgo import *
from StanleyController import *

import numpy as np
import argparse # This module used for running the file from command line with arguments


# The function chackes the distance between the vehicle and last point on the path
# When this distance is smaller than a thershold -> the vehicle arrived on target
def arrived_to_target(path, vehicle, ArrivingThreshold):
    DistFromTarget = np.hypot((path.PathPositionsList[-1][0] - vehicle.pos[0]), (path.PathPositionsList[-1][1] - vehicle.pos[1]))
    if DistFromTarget <= ArrivingThreshold:
        return True
    return False
    
    pass

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Run vehicle path tracking simulation.')
    parser.add_argument('-x0', type=float, help='Initial x position of the vehicle')
    parser.add_argument('-y0', type=float, help='Initial y position of the vehicle')
    parser.add_argument('-psi', type=float, help='Initial heading angle of the vehicle')
    parser.add_argument('-v', type=float, help='Initial velocity of the vehicle')
    
    args = parser.parse_args()
    
    # Define the needed objects

    TargetPath = path(PathLength=50)

    #Vehicle = vehicle(x0=0.1,y0=0.1,psi0=0.0,v0=1.0)
    Vehicle = vehicle(x0=args.x0, y0=args.y0, psi=args.psi, v=args.v)

    PurePursuitTracking = PurePursuitAlgo(TargetPath, Vehicle, lookahead_distance=4.0)
    StanleyTracking = StanleyController(TargetPath, Vehicle)

    SimTime = 0 # Initialzing simulation time. The thresahold will be in seconds

    # Two conditions for the simulation to run: (not arriving the target) or (time limit)
    while(not arrived_to_target(TargetPath, Vehicle, ArrivingThreshold=0.4) and SimTime < 300):
        simulation(TargetPath, Vehicle)

        # Below you can choose between two control startgies (Pure pursuit or Stanley control)

        #SteeringCommand = PurePursuitTracking.calculate_steering_angle()
        SteeringCommand = StanleyTracking.calculate_steering_angle()

        Vehicle.set_steering_angle(SteeringCommand)
        Vehicle.update(delta_t=0.1)

        SimTime += 0.1

    show_results(TargetPath, Vehicle)


if __name__ == "__main__":
    main()