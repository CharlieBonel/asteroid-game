import pygame
from constants import PLAYER_HIT_COOLDOWN

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        r_self = self.radius
        r_other = other.radius
        min_dist = r_other + r_self
        if pygame.math.Vector2.distance_to(self.position, other.position) < min_dist:
            return True
        else:
            return False