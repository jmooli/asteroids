from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, 5)
        self.radius = SHOT_RADIUS
        self.color = (240, 240, 240)

    def draw(self, screen):
        pygame.draw.circle(screen, color = self.color, center = self.position, radius = self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
