import pygame
import math
import sys
from circleshape import CircleShape
from shot import Shot
from logger import log_event
from functions import SqDistPointSegment

from constants import PLAYER_SHOT_SPEED, PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_HIT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.hit_cooldown_timer = 0
        self.life = 3
        self.a = 0
        self.b = 0
        self.c = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        self.a = a
        self.b = b
        self.c = c
        return [a, b, c]
    
    def collision_detection(self, other):
        # for line between points (x1, y1) and (x2, y2)
        triangle = self.triangle()
        point_a = triangle[0]
        point_b = triangle[1]
        point_c = triangle[2]
        dist_from_asteroid_sqr = []
        dist_from_asteroid_sqr.append(SqDistPointSegment(point_a, point_b, other.position))
        dist_from_asteroid_sqr.append(SqDistPointSegment(point_b, point_c, other.position))
        dist_from_asteroid_sqr.append(SqDistPointSegment(point_a, point_c, other.position))
        for each in dist_from_asteroid_sqr:
            if math.sqrt(each) < other.radius:
                return True
            else:
                return False


    # This shows the player as grey when hit
    def draw(self, screen):
        
        if self.hit_cooldown_timer > 0:
            pygame.draw.polygon(screen, (128, 128, 128), self.triangle(), LINE_WIDTH)
            
        else:
            pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
            
              
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            pass
        else:
            shot = Shot(self.position.x, self.position.y)
            shot_vector = pygame.Vector2(0,1)
            rotated_shot_vector = shot_vector.rotate(self.rotation)
            rotated_shot_vector_speed = rotated_shot_vector * PLAYER_SHOT_SPEED
            shot.velocity = rotated_shot_vector_speed
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

    def remove_life(self):
        if self.hit_cooldown_timer > 0:
            pass
        else:
            if self.life > 1:
                self.life -= 1
                log_event("player_hit")
                self.hit_cooldown_timer = PLAYER_HIT_COOLDOWN
            else:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

    # creates screen with life to blit onto game screen
    def create_life(self):
        font = pygame.font.SysFont("Arial", 18, bold=True, italic=False)
        text_surface = pygame.font.Font.render(font, f"Lives remaining: {self.life}", True, (255, 255, 255))
        return text_surface

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= dt
        self.hit_cooldown_timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
