from dataclasses import dataclass
import numpy as np

from star_system import StarSystem
from utils import pol2cart


@dataclass
class GlobularCluster:
    star_system = []

    def generate_stars(self, radius, num_stars):
        mu, sigma = 0.0, 10.0 # offset, standard deviation
        distance_mod = 10.0
        rng = np.random.default_rng()

        for idx in range(num_stars):
            rho = abs(rng.normal(mu, sigma) * radius) / distance_mod # radius
            theta = rng.uniform(0, 2 * np.pi)
            phi = rng.uniform(0, 2 * np.pi)
            security = rho / radius

            x, y, z = pol2cart(rho, theta, phi)

            star = StarSystem(f"Star Sector #{idx}", x, y, z, 60000, security)
            self.star_system.append(star)
