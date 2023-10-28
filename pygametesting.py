import pygame

pygame.init()   # for starting pygame

screen = pygame.display.set_mode((600, 400))    # save display size, open window
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()     # pygame makes a clock for fps

top_icon = pygame.image.load("dev_icon.png")     # load top icon image to project
pygame.display.set_icon(top_icon)       # set top icon

bird_sprites = pygame.image.load("bird_old.png")


green_y = 200       # variable of green rect's y coordinate
magenta_x = 150     # variable of magenta rect's x coordinate
magenta_y = 150      # variable of magenta rect's y coordinate
bird_x = 80
bird_y = 90

while True:                             # for program to close when clicked X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # quits the program
            pygame.quit()
            exit()                      # closes the program

    screen.fill("white")    # updates background
    pygame.draw.rect(screen, "green", (200, green_y, 50, 100))
    pygame.draw.rect(screen, "magenta", (magenta_x, magenta_y, 40, 60))
    # pygame.draw.rect(display, "color", (x, y, width, length))

    screen.blit(bird_sprites, (bird_x, bird_y))

    green_y -= 4    # variable for green rect's y -= number (makes it move up)

    keys = pygame.key.get_pressed()     # list of all keys pressed
    if keys[pygame.K_LEFT]:
        bird_x -= 2
    if keys[pygame.K_RIGHT]:
        bird_x += 2
    if keys[pygame.K_UP]:
        bird_y -= 2
    if keys[pygame.K_DOWN]:
        bird_y += 2


    pygame.display.update()     # updates program's frames
    clock.tick(60)      # setting framerate