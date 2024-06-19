import numpy as np

# Zeekr 001 dynamic parameters, according to an online search by chatGPT:

WheelBase = 2.999 # [m]
Mass = 2345 # [kg]
l_f = 1.5 # [m]
l_r = 1.5 # [m]
C_f = 190000 # [N/rad]
C_r = 190000 # [N/rad]

class Vehicle:
    def __init__(self, x0, y0, psi0, v0, L):
        self.x = x0  # Position x
        self.y = y0  # Position y
        self.psi = psi0  # Heading angle
        self.v = v0  # Speed
        self.delta = 0  # Steering angle
        self.L = L  # Wheelbase
    
    def update(self, delta_t):
        """Update the vehicle's state based on the kinematic bicycle model."""
        self.x += self.v * np.cos(self.psi) * delta_t
        self.y += self.v * np.sin(self.psi) * delta_t
        self.psi += (self.v / self.L) * np.tan(self.delta) * delta_t

    def set_steering_angle(self, delta):
        """Set the steering angle (in radians)."""
        self.delta = delta

    def set_speed(self, speed):
        """Set the vehicle speed."""
        self.v = speed

    def global_to_ego(self, X_global, Y_global):
        """Transform global coordinates to ego coordinates."""
        dx = X_global - self.x
        dy = Y_global - self.y
        x_ego = np.cos(self.psi) * dx + np.sin(self.psi) * dy
        y_ego = -np.sin(self.psi) * dx + np.cos(self.psi) * dy
        return x_ego, y_ego

    def ego_to_global(self, x_ego, y_ego):
        """Transform ego coordinates to global coordinates."""
        X_global = self.x + np.cos(self.psi) * x_ego - np.sin(self.psi) * y_ego
        Y_global = self.y + np.sin(self.psi) * x_ego + np.cos(self.psi) * y_ego
        return X_global, Y_global