import pygame
pygame.init()

# характеристики
pygame.display.set_caption('Calculator')
window_height = 550
window_width = 700
window = pygame.display.set_mode((window_height, window_width))
color = (75, 0, 130)
window.fill(color)
pygame.display.flip()

# bg = pygame.image.load("calc.jpg")



# код
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False