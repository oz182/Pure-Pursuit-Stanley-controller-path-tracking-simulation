import numpy as np

class StanleyController:
    def __init__(self, path, vehicle, k=1.0, lookahead_distance=1.0):
        self.k = k
        self.lookahead_distance = lookahead_distance
        self.path = path
        self.vehicle = vehicle

    def find_closest_point(self):
        distances = [np.hypot(self.vehicle.pos[0] - p[0], self.vehicle.pos[1] - p[1]) for p in self.path.PathPositionsList]
        min_distance_index = np.argmin(distances)
        return min_distance_index, self.path.PathPositionsList[min_distance_index]

    def calculate_steering_angle(self):
        closest_point_index, closest_point = self.find_closest_point()
        lookahead_point = self.path.PathPositionsList[min(closest_point_index + 1, len(self.path.PathPositionsList) - 1)]

        # Transform to vehicle coordinates
        lookahead_point_ego = self.vehicle.global_to_ego(lookahead_point[0], lookahead_point[1])
        dx = lookahead_point_ego[0]
        dy = lookahead_point_ego[1]
        local_x = dx * np.cos(self.vehicle.psi) + dy * np.sin(self.vehicle.psi)
        local_y = dy * np.cos(self.vehicle.psi) - dx * np.sin(self.vehicle.psi)

        # Heading error
        path_heading = np.arctan2(lookahead_point[1] - closest_point[1], lookahead_point[0] - closest_point[0])
        heading_error = path_heading - self.vehicle.psi
        heading_error = np.arctan2(np.sin(heading_error), np.cos(heading_error))  # Normalize angle

        # Cross-track error
        crosstrack_error = local_y

        # Stanley control law
        control_steer = heading_error + np.arctan2(self.k * crosstrack_error, self.vehicle.v)

        return control_steer
