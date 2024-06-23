# Importing needed classes and librarys
from classes.Path import *
from simulation import *
from classes.Vehicle import *
from classes.PurePursuitAlgo import *
from classes.StanleyController import *

import numpy as np
import argparse # This module used for running the file from command line with arguments


# The function chackes the distance between the vehicle and last point on the path
# When this distance is smaller than a thershold -> the vehicle arrived on target
def arrived_to_target(path, vehicle, ArrivingThreshold):
    DistFromTarget = np.hypot((path.PathPositionsList[-1][0] - vehicle.pos[0]), (path.PathPositionsList[-1][1] - vehicle.pos[1]))
    if DistFromTarget <= ArrivingThreshold:
        return True
    return False
    

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

    # Define vehicles
    Vehicle = vehicle(x0=args.x0, y0=args.y0, psi=args.psi, v=args.v, BiasServoAngle=0)
    BiasVehicle = vehicle(x0=args.x0, y0=args.y0, psi=args.psi, v=args.v, BiasServoAngle=0.018)

    #Creating the algorithms objects
    PurePursuitTracking = PurePursuitAlgo(TargetPath, Vehicle, lookahead_distance=4.0)
    StanleyTracking = StanleyController(TargetPath, Vehicle)

    # Initialzing simulation time. The thresahold will be in seconds
    SimTime = 0

    # Two conditions for the simulation to run: (not arriving the target) or (time limit)
    while(not arrived_to_target(TargetPath, Vehicle, ArrivingThreshold=0.4) and SimTime < 300):
        simulation(TargetPath, Vehicle, BiasVehicle)

        # Below you can choose between two control startgies (Pure pursuit or Stanley control)
        SteeringCommand_Pursuit = PurePursuitTracking.calculate_steering_angle()   # Pure Pursuit
        SteeringCommand_Stanley = StanleyTracking.calculate_steering_angle()      # Stanley controller

        # Start moving one Vehicle. 
        Vehicle.set_steering_angle(SteeringCommand_Pursuit)
        Vehicle.update(delta_t=0.1)

        # Start moving the second vehicle.
        BiasVehicle.set_steering_angle(SteeringCommand_Pursuit) # Adding 5 deg bias of steering angle
        #BiasVehicle.update(delta_t=0.1) # Uncomment this line to plot only one vehicle

        SimTime += 0.1 # Just for time measurment

    show_results(TargetPath, Vehicle, BiasVehicle)


if __name__ == "__main__":
    main()