# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_color = (0, 0, 0)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(bg_color)
        pygame.display.flip()

if __name__ == "__main__":
    main()