import numpy as np

WheelBase = 2.999 # [m] WheelBase of zeekr 001 

class vehicle:
    # This class describe the vehicle and its properties.
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
        self.traj_psi = []

        self.SteeringServo = ServoDynamics()
    
    def update(self, delta_t):
        # Update the vehicle's state based on the kinematic bicycle model.
        self.x += self.v * np.cos(self.psi) * delta_t
        self.y += self.v * np.sin(self.psi) * delta_t
        self.psi += (self.v / self.WB) * np.tan(self.delta) * delta_t

        self.pos = (self.x, self.y)
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)
        self.traj_psi.append(self.psi)

    def set_steering_angle(self, delta):
        # Set the steering angle using the servo dynamics classs
        self.delta = self.SteeringServo.get_actual_steering_angle(delta_command=delta)
        return self.delta

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
    

    
class ServoDynamics:
    # This class expresses the control dynamics of the steering angle actuator.
    # I've set the dt to 0.4. smaller than that and the servo is not fast enogh to overcome the curve
        def __init__(self, delta_max=45.0, rate_limit=20.0, time_delay=0.2, omega_delta=1.0, zeta_delta=0.7, dt=0.4):
            self.delta_max = np.radians(delta_max)  # Convert to radians
            self.rate_limit = np.radians(rate_limit)  # Convert to radians per second
            self.time_delay = time_delay
            self.omega_delta = omega_delta # Bandwidth
            self.zeta_delta = zeta_delta   # Damping
            self.dt = dt

            # Initialize states for the second-order system
            self.delta = 0
            self.delta_dot = 0

            # Initialize buffer for time delay
            self.delay_buffer = [0] * int(time_delay / dt)

        def second_order_system(self, delta_command):
            # Discrete second-order system approximation
            delta_ddot = self.omega_delta**2 * (delta_command - self.delta) - 2 * self.zeta_delta * self.omega_delta * self.delta_dot
            self.delta_dot += delta_ddot * self.dt
            self.delta += self.delta_dot * self.dt

            return self.delta

        def rate_limiter(self, delta_command, delta_prev):
            max_change = self.rate_limit * self.dt
            change = delta_command - delta_prev
            if abs(change) > max_change:
                delta_command = delta_prev + np.sign(change) * max_change
            return delta_command

        def get_actual_steering_angle(self, delta_command):
            # Apply time delay
            self.delay_buffer.append(delta_command)
            delayed_command = self.delay_buffer.pop(0)

            # Apply rate limiter
            limited_command = self.rate_limiter(delayed_command, self.delta)

            # Update the second-order system
            actual_delta = self.second_order_system(limited_command)

            # Limit the road wheel angle
            actual_delta = np.clip(actual_delta, -self.delta_max, self.delta_max)

            return actual_delta