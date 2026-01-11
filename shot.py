import pygame
import math
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def shot_collision(self, other):
        self_radius = self.radius
        other_radius = other.radius
        min_dist = self_radius + other_radius
        if pygame.math.Vector2.distance_to(self.position, other.position) <= min_dist:
            return True
        else:
            return False