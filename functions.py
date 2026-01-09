import pygame
import math

# for this game, C is the center of the circle
def SqDistPointSegment(point_a, point_b, point_c):
    vector_ab = pygame.math.Vector2(point_b[0] - point_a[0], point_b[1] - point_a[1])
    vector_ac = pygame.math.Vector2(point_c[0] - point_a[0], point_c[1] - point_a[1])
    vector_bc = pygame.math.Vector2(point_c[0] - point_b[0], point_c[1] - point_b[1])
   
    e = pygame.math.Vector2.dot(vector_ac, vector_ab)
    f = pygame.math.Vector2.dot(vector_ab, vector_ab)
    if e <= 0:
        return pygame.math.Vector2.dot(vector_ac, vector_ac)
    elif e >= f:
        return pygame.math.Vector2.dot(vector_bc, vector_bc)
    else:
        return pygame.math.Vector2.dot(vector_ac, vector_ac) - (e**2)/f


