import pygame
pygame.init()

# Constants
WINDOW_HEIGHT = 550
WINDOW_WIDTH = 700
color = (75, 0, 130)


# Window logic
window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Calculator')
window.fill(color)
pygame.display.flip()

# bg = pygame.image.load("calc.jpg")



# Event-loop
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
