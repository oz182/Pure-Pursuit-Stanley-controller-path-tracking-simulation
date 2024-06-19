import numpy as np
import math

# This path object automaticlly creates the path when called
# The path coordinates will be in a global referance frame
class path:
    def __init__(self, PathLength):

        self.PathLength = PathLength

        # Create an array of "x axis" dots
        self.cx = np.arange(0, PathLength, 0.5) # (start, length, space)

        # attach the function to the x axis from above. The function shape is the path
        self.cy = [math.sin(x_index / 8.0) * x_index / 5.0 for x_index in self.cx]

        # Create a list of tupels for every cx and cy pair
        PathPositionsList = list(zip(self.cx, self.cy))