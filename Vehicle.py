import numpy as np

class Vehicle:
    def __init__(self, x0, y0, psi0, v):
        self.position = np.array([x0, y0])
        self.psi = psi0
        self.v = v
        self.delta = 0  # Road wheel angle