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
        return min_distance_index, self.path.PathPositionsList[min_distance_index]
    
    def find_lookahead_point(self, closest_point, closest_point_index):
        # Find the point on the path that is lookahead_distance away from the closest_point
        for i in range(closest_point_index, len(self.path.PathPositionsList)):
            dist = np.hypot((self.path.PathPositionsList[i][0] - self.vehicle.pos[0]), (self.path.PathPositionsList[i][1] - self.vehicle.pos[1]))
            if dist >= self.lookahead_distance:
                return self.path.PathPositionsList[i]
        return self.path.PathPositionsList[-1]

    def calculate_lookahead_point(self):
        # Assuming path is a list of tuples (X, Y) in global coordinates
        closest_point_index, closest_point = self.find_closest_point()
        lookahead_point = self.find_lookahead_point(closest_point, closest_point_index)
        return lookahead_point
    
    def calculate_turn_radius(self ,path, vehicle):
        # Calculate the turn radius given the current position and lookahead point
        lookahead_point = self.calculate_lookahead_point()
        lookahead_point_ego = vehicle.global_to_ego(lookahead_point[0], lookahead_point[1])
        dx = lookahead_point_ego[0]
        dy = lookahead_point_ego[1]
        distance = np.hypot(dx, dy)
        if dy == 0:  # Avoid division by zero
            return float('inf')  # Infinite radius implies straight line
        radius = (distance ** 2) / (2 * dy)
        return radius

    def calculate_steering_angle(self):
        # Calculate the steering angle given the turn radius and wheelbase
        turn_radius = self.calculate_turn_radius(self.path, self.vehicle)
        if turn_radius == float('inf'):
            return 0  # Straight line
        steering_angle = (np.arctan(self.vehicle.WB / turn_radius)) 
        return steering_angle

    



