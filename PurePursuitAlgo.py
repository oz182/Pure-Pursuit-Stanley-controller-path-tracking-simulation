import numpy as np

class PurePursuitAlgo:
    def __init__(self, lookahead_distance):
        self.lookahead_distance = lookahead_distance

    def find_closest_point(self, path, vehicle):
        # Find the closest point on the path to the current position
        distances = [np.hypot(vehicle.pos[0] - p[0], vehicle.pos[1] - p[1]) for p in path.PathPositionsList]
        min_distance_index = np.argmin(distances)
        return path[min_distance_index]
    
    def find_lookahead_point(self, path, closest_point, vehicle):
        # Find the point on the path that is lookahead_distance away from the closest_point
        for i in range(len(path)):
            if np.hypot(path[i][0] - vehicle.pos[0], path[i][1] - vehicle.pos[1]) >= self.lookahead_distance:
                return path[i]
        return path[-1]

    def calculate_lookahead_point(self, path, vehicle):
        # Assuming path is a list of tuples (X, Y) in global coordinates
        closest_point = self.find_closest_point(path, vehicle)
        lookahead_point = self.find_lookahead_point(path, closest_point, vehicle)
        return lookahead_point
    



