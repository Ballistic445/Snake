import pygame

pygame.init()

true = True
false = False

WindowWidth = 720
WindowHeight = 256
screen = pygame.display.set_mode((WindowWidth, WindowHeight))
clock = pygame.time.Clock()

Running = true

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = false

    screen.fill("black")
    pygame.display.flip()

    clock.tick(60)
