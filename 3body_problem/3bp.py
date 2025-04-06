# 3 body problem simulator

import pygame as pg

# Constants
G =  6.67430e-11

class Mass:
    def __init__(self, x, y, m, vx=0, vy=0):
        self.x = x
        self.y = y
        self.m = m
        self.vx = vx
        self.vy = vy
        self.trail = []

    def force(self, m):
        dx = m.x - self.x
        dy = m.y - self.y
        r = (dx**2 + dy**2)**0.5
        f = G * self.m * m.m / r**2
        fx = f * dx / r
        fy = f * dy / r
        return fx, fy
    
    def update(self, m1, m2, dt):
        fx1, fy1 = self.force(m1)
        fx2, fy2 = self.force(m2)
        self.vx += (fx1 + fx2) / self.m * dt
        self.vy += (fy1 + fy2) / self.m * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.trail.append((self.x, self.y))
        if len(self.trail) > 2000:  # Limit trail length
            self.trail.pop(0)
        return fx1 + fx2, fy1 + fy2

# Main
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('3 Body Problem')
clock = pg.time.Clock()

m1 = Mass(200, 300, 1e12, 0, 0.2)
m2 = Mass(450, 400, 1e12, 0, -0.2)
m3 = Mass(600, 100, 1e12, 0.2, 0)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    fx1, fy1 = m1.update(m2, m3, 1)
    fx2, fy2 = m2.update(m3, m1, 1)
    fx3, fy3 = m3.update(m1, m2, 1)

    screen.fill((0, 0, 0))
    
    for mass, color in [(m1, (255, 0, 0)), (m2, (0, 255, 0)), (m3, (0, 0, 255))]:
        if len(mass.trail) > 1:
            pg.draw.lines(screen, color, False, [(int(x), int(y)) for x, y in mass.trail], 2)
        pg.draw.circle(screen, color, (int(mass.x), int(mass.y)), 5)
    
    # Draw force vectors
    scale_factor = 0.1
    pg.draw.line(screen, (255, 255, 255), (int(m1.x), int(m1.y)), (int(m1.x + fx1 * scale_factor), int(m1.y + fy1 * scale_factor)), 1)
    pg.draw.line(screen, (255, 255, 255), (int(m2.x), int(m2.y)), (int(m2.x + fx2 * scale_factor), int(m2.y + fy2 * scale_factor)), 1)
    pg.draw.line(screen, (255, 255, 255), (int(m3.x), int(m3.y)), (int(m3.x + fx3 * scale_factor), int(m3.y + fy3 * scale_factor)), 1)
    
    pg.display.flip()
    clock.tick(60)

pg.quit()
