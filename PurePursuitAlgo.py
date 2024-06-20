import numpy as np
import math

class PurePursuitAlgo:
    def __init__(self, path, vehicle, lookahead_distance):
        self.lookahead_distance = lookahead_distance
        #self.lookahead_distance_varient = lookahead_distance * (vehicle.v0 * 0.1)
        self.path = path
        self.vehicle = vehicle

    def find_closest_point(self):
        # Find the closest point on the path to the current position
        distances = [np.hypot(self.vehicle.pos[0] - p[0], self.vehicle.pos[1] - p[1]) for p in self.path.PathPositionsList]
        min_distance_index = np.argmin(distances)
        return self.path.PathPositionsList[min_distance_index]
    
    def find_lookahead_point(self, closest_point):
        # Find the point on the path that is lookahead_distance away from the closest_point
        for i in range(len(self.path.PathPositionsList)):
            if np.hypot((self.path.PathPositionsList[i][0] - closest_point[0]).any(), (self.path.PathPositionsList[i][1] - closest_point[1]).any()) >= self.lookahead_distance:
                return self.path.PathPositionsList[i]
        return self.path.PathPositionsList[-1]

    def calculate_lookahead_point(self, path, vehicle):
        # Assuming path is a list of tuples (X, Y) in global coordinates
        closest_point = self.find_closest_point()
        lookahead_point = self.find_lookahead_point(closest_point)
        return lookahead_point
    
    def calculate_turn_radius(self ,path, vehicle):
        # Calculate the turn radius given the current position and lookahead point
        lookahead_point = self.calculate_lookahead_point(path, vehicle)
        dx = lookahead_point[0] - vehicle.pos[0]
        dy = lookahead_point[1] - vehicle.pos[1]
        distance = np.hypot(dx, dy)
        if dy == 0:  # Avoid division by zero
            return float('inf')  # Infinite radius implies straight line
        radius = (distance ** 2) / (2 * abs(dy))
        return radius

    def calculate_steering_angle(self):
        # Calculate the steering angle given the turn radius and wheelbase
        turn_radius = self.calculate_turn_radius(self.path, self.vehicle)
        if turn_radius == float('inf'):
            return 0  # Straight line
        return (np.arctan(self.vehicle.WB / turn_radius)) * 180 / math.pi

    



