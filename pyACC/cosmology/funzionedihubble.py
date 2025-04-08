import numpy as np
class HubbleFunction:
    def __init__(self, H0, omega_m, omega_l, omega_rad, omega_k):
        self.H0 = H0  # Hubble constant in km/s/Mpc
        self.omega_m = omega_m  # Density parameter for matter
        self.omega_l = omega_l  # Density parameter for dark energy
        self.omega_rad = omega_rad  # Density parameter for radiation 
        self.omega_k = omega_k  # Density parameter for curvature
    
    def __call__(self, z):
        return self.H0 * np.sqrt(
            self.omega_m * (1 + z)**3 + self.omega_l + self.omega_rad * (1 + z)**4
            + self.omega_k * (1 + z)**2 )