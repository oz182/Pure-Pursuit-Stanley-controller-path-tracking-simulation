import numpy as np

WheelBase = 2.999 # [m] WheelBase of zeekr 001 

class vehicle:
    def __init__(self, x0, y0, psi, v):
        self.x = x0  # Position x
        self.y = y0  # Position y
        self.psi = psi  # Heading angle
        self.v = v  # Speed
        self.delta = 0  # Steering angle
        
        self.WB = WheelBase
        self.SteerAngleLim = 0.785 # [rad] asked in the assignment 45 deg steer angle limit

        self.pos = (self.x, self.y)
        self.traj_x = []
        self.traj_y = []
    
    def update(self, delta_t):
        # Update the vehicle's state based on the kinematic bicycle model.
        self.x += self.v * np.cos(self.psi) * delta_t
        self.y += self.v * np.sin(self.psi) * delta_t
        self.psi += (self.v / self.WB) * np.tan(self.delta) * delta_t

        self.pos = (self.x, self.y)
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)

    def set_steering_angle(self, delta):
        # Set the steering angle (in radians). The steering angle goes  
        if delta < -self.SteerAngleLim:
            self.delta = -self.SteerAngleLim
        elif delta > self.SteerAngleLim:
            self.delta = self.SteerAngleLim
        else:
            self.delta = delta
            

    def set_speed(self, speed):
        # Set the vehicle speed.
        self.v = speed

    def global_to_ego(self, X_global, Y_global):
        # Transform global coordinates to ego coordinates.
        dx = X_global - self.x
        dy = Y_global - self.y
        x_ego = np.cos(-self.psi) * dx - np.sin(-self.psi) * dy
        y_ego = np.sin(-self.psi) * dx + np.cos(-self.psi) * dy
        return x_ego, y_ego

    def ego_to_global(self, x_ego, y_ego):
        # Transform ego coordinates to global coordinates.
        X_global = self.x + np.cos(self.psi) * x_ego - np.sin(self.psi) * y_ego
        Y_global = self.y + np.sin(self.psi) * x_ego + np.cos(self.psi) * y_ego
        return X_global, Y_global