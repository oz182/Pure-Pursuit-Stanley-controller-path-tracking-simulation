# VehicleDynamicsSimulation_Assignment
Vehicle Dynamic simulation - Entry Programming Assignment

This assignment is a simualtion of path tracking vehicle (bicycle kinematic model) using two kind of algorithms: Pure Pursuit and stanley controller.

To run the simulation, open command line from the project's dicrectory and run the following command:
'''terminal
python3 main.py -x0 0 -y0 0 -psi 0 -v 1.0
 '''
 You can set differnt initial values for the vehicle.

In this README file I will describe the various classes in this assignment:

1. Path - Consturcting the path of which is the tarcking target
    Input: Path length along the x axis
    Output: List of tupels - coordinates (x,y) which draws a custom sinus based graph

2. Vehicle - A mobile system who is able to move on a 2D space, contains the properties which help describe its kinematic behivour
    Inputs:
    Outputs:

3. ServoDynamics - The class simulate a steering servo with a 2nd order behivour
    Inputs:
    Outputs:

4. PurePursuitAlgo - The path tracking algorithm "Pure Pursuit"
    Inputs:
    Outputs:

5. StanleyController - Another path tracking algorithm "Stanley"
    Inputs:
    Outputs:

Other then that, the "Simulation.py" file, contains the needed code for illustarting an animation
of the algorithm.
