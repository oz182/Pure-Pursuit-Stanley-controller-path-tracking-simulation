# Importing needed classes
from Environment import *
from simulation import *
from Vehicle import *
from PurePursuitAlgo import *

import numpy as np

# The function chackes the distance between the vehicle and last point on the path
# When this distance is smaller than a thershold -> the vehicle arrived on target
def arrived_to_target(path, vehicle, ArrivingThreshold):
    DistFromTarget = np.hypot((path.PathPositionsList[-1][0] - vehicle.pos[0]), (path.PathPositionsList[-1][1] - vehicle.pos[1]))
    if DistFromTarget <= ArrivingThreshold:
        return True
    return False
    
    pass


def main():
    TargetPath = path(PathLength=50)
    Vehicle = vehicle(x0=0.1,y0=0.1,psi0=0.0,v0=1.0)
    TrackingAlgo = PurePursuitAlgo(TargetPath, Vehicle, lookahead_distance=2.0)

    SimTime = 0 # Initialzing simulation time. The thresahold will be in seconds

    while(not arrived_to_target(TargetPath, Vehicle, ArrivingThreshold=0.4) or SimTime >= 300):
        simulation(TargetPath, Vehicle)
        SteeringCommand = TrackingAlgo.calculate_steering_angle()
        Vehicle.set_steering_angle(SteeringCommand)
        Vehicle.update(delta_t=0.2)

        SimTime += 0.2


if __name__ == "__main__":
    main()