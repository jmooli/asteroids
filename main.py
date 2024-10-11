# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot, updatable, drawable)
    
    time = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroidfield = AsteroidField()
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_color = (0, 0, 0)
    

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(bg_color)

        for up in updatable:
            up.update(dt)
        for d in drawable:
            d.draw(screen)

        
        pygame.display.flip()
        dt = time.tick(60) / 1000

        for a in asteroid:
            if a.collides_with(player):
                print("Game Over!")
                return
            for s in shot:
                if a.collides_with(s):
                    a.split()
                    s.kill()
                    print("Asteroid destroyed!")

            
                


if __name__ == "__main__":
    main()