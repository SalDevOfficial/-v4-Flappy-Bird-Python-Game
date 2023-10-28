import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("</>")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("Green")
    pygame.draw.rect(screen, "Blue", (70,50,200,140))

    pygame.display.update()
    clock.tick(60)