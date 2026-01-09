import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCORE_HEIGHT, SCORE_X_POS, LIFE_POS_X, LIFE_POS_Y
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    mesh = pygame.sprite.Group()
    Player.containers = (updatable, drawable, mesh)
    Asteroid.containers = (updatable, drawable, asteroids, mesh)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    # initialising asteroid field
    AsteroidField()
    # initialising score
    score = Score()
    # initialising game loop
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # add clock for delta time
    clock = pygame.time.Clock()
    dt = 0
    # instantiating player
    screen_x = SCREEN_WIDTH / 2
    screen_y = SCREEN_HEIGHT / 2
    player = Player(screen_x, screen_y)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # adding score to screen
        screen.blit(score.create_score(), (SCORE_X_POS, SCORE_HEIGHT))
        # adding live to screen
        screen.blit(player.create_life(), (LIFE_POS_X, LIFE_POS_Y))
        updatable.update(dt)
        # detecting colisions
        for asteroid in asteroids:
            if player.collision_detection(asteroid) == True:
                player.remove_life()
                # add function to set ship to grey
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()
                    score.add_score()
        for p in drawable:
            p.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

