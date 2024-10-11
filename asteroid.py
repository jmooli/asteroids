from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (240, 240, 240)

    def draw(self, screen):
        pygame.draw.circle(screen, color = self.color, center = self.position, radius = self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # split the asteroid into two smaller asteroids
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20, 50)
            velocity_a = self.velocity.rotate(random_angle) * 1.2
            velocity_b = self.velocity.rotate(-random_angle) * 1.2

            asteroid_a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_a.velocity = velocity_a
            asteroid_b.velocity = velocity_b
            
        pass
