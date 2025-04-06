# Solar system simulator

import pygame as pg
import math

# Constants
G = 6.67430e-11  # Gravitational constant
AU = 1.496e11  # Astronomical unit in meters
SCALE = 250 / AU  # Scale for visualization
TIMESTEP = 3600 * 24  # One day in seconds

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

class Planet:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, screen):
        x = self.x * SCALE + screen.get_width() / 2
        y = self.y * SCALE + screen.get_height() / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * SCALE + screen.get_width() / 2
                y = y * SCALE + screen.get_height() / 2
                updated_points.append((x, y))

            pg.draw.lines(screen, self.color, False, updated_points, 2)

        pg.draw.circle(screen, self.color, (int(x), int(y)), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * TIMESTEP
        self.y_vel += total_fy / self.mass * TIMESTEP

        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP
        self.orbit.append((self.x, self.y))

def main():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    pg.display.set_caption("Solar System Simulator")
    clock = pg.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000  # m/s

    mars = Planet(-1.524 * AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000  # m/s

    planets = [sun, earth, mars]

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for planet in planets:
            planet.update_position(planets)
            planet.draw(screen)

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()