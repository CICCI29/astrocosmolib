import numpy as np
from scipy.integrate import quad
from .funzionedihubble import HubbleFunction

class Distances:
    def __init__(self, hubble_function):
        self.hubble_function = hubble_function
    
    def comoving_distance(self, z):
        # Function to calculate comoving distance for a single z value
        def single_comoving_distance(z_single):
            def integrand(z_prime):
                return 1.0 / self.hubble_function(z_prime)
            
            distance, _ = quad(integrand, 0, z_single)
            c = 299792.458  # Speed of light in km/s
            return c * distance
        
        # Check if z is a single value or an array
        if np.isscalar(z):
            return single_comoving_distance(z)
        else:
            return [single_comoving_distance(z_i) for z_i in z]
    
    def luminosity_distance(self, z):
        return (1 + z) * self.comoving_distance(z)
    def angular_diameter_distance(self, z):
        omega_k = self.hubble_function.omega_k
        c = 299792.458  # Velocità della luce in km/s
        H0 = self.hubble_function.H0

        comoving_dist = np.array(self.comoving_distance(z))  # Assicurati che sia un array NumPy

        if omega_k == 0:
            return comoving_dist / (1 + z)
        elif omega_k > 0:
            return (c / H0) * (1 / np.sqrt(omega_k)) * np.sinh(np.sqrt(omega_k) * (H0 / c) * comoving_dist)
        elif omega_k < 0:
            return (c / H0) * (1 / np.sqrt(np.abs(omega_k))) * np.sin(np.sqrt(np.abs(omega_k)) * (H0 / c) * comoving_dist)