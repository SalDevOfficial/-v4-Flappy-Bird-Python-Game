from random import randint, choice
import pygame


# add sfx and music


pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pygame Flappy Bird")
clock = pygame.time.Clock()

top_icon = pygame.image.load("flappybirdicon.png")
pygame.display.set_icon(top_icon)

# bg load

bg1 = pygame.image.load("fb_bg.png").convert()


# bird load

bird1 = pygame.image.load("bird_fly_1.png").convert_alpha()
bird2 = pygame.image.load("bird_fly_2.png").convert_alpha()
bird3 = pygame.image.load("bird_fly_3.png").convert_alpha()

# bird animation frames

bird_frames = [bird1, bird2, bird3]
bird_frame_index = 0

bird_surf = bird_frames[bird_frame_index]
bird_rect = bird_surf.get_rect(center=(100, 250))
gravity = -5

# pipes

green_pipe = pygame.image.load("green-pipe.png").convert_alpha()
yellow_pipe = pygame.image.load("yellow-pipe.png").convert_alpha()
blue_pipe = pygame.image.load("blue-pipe.png").convert_alpha()
red_pipe = pygame.image.load("red-pipe.png").convert_alpha()

pipes = [green_pipe, yellow_pipe, green_pipe, blue_pipe, green_pipe, red_pipe]

pipe_bottom_surf = choice(pipes)
pipe_top_surf = pygame.transform.flip(pipe_bottom_surf, False, True)

pipe_top_rect = pipe_top_surf.get_rect(midbottom=(500, 150))
pipe_bottom_rect = pipe_bottom_surf.get_rect(midtop=(500, 350))

# game over messages and font
main_font = pygame.font.Font("ChrustyRock-ORLA.ttf", 50)
small_font = pygame.font.Font("ChrustyRock-ORLA.ttf", 35)

game_over_msg = main_font.render("Game Over!", True, "red")
game_over_msg_rect = game_over_msg.get_rect(center=(400, 250))

restart_msg = main_font.render("Press Space to Restart", True, "red")
restart_msg_rect = restart_msg.get_rect(center=(400,400))

# scores and high score
score = 0
score_msg = small_font.render(f"Score: {score:}", True, "yellow")
score_msg_rect = score_msg.get_rect(topright=(800, 0))


# game over images

game_over_bird_surf = pygame.transform.scale2x(bird_surf)
game_over_bird_rect = game_over_bird_surf.get_rect(midbottom=(400, 230))

game_active = True

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gravity = -5
        else:
            # restart
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

                bird_rect.center = (100, 250)
                gravity = -5

                pipe_top_rect.bottomleft = (800, randint(50, 200))
                pipe_bottom_rect.topleft = (800, randint(300, 450))
                pipe_bottom_surf = choice(pipes)
                pipe_top_surf = pygame.transform.flip(pipe_bottom_surf, False, True)
                
                score = 0

    if game_active:
        # everything on screen
        screen.blit(bg1, (0, 0))
        screen.blit(bird_surf, bird_rect)
        screen.blit(pipe_bottom_surf, pipe_bottom_rect)
        screen.blit(pipe_top_surf, pipe_top_rect)
        screen.blit(score_msg, score_msg_rect)

        # bird animations

        bird_frame_index += 0.05
        if bird_frame_index >= 3:
            bird_frame_index = 0

        bird_surf = bird_frames[int(bird_frame_index)]

        # pipe movement
        pipe_top_rect.x -= 3
        pipe_bottom_rect.x -= 3
        if pipe_top_rect.right < 0:
            pipe_top_rect.bottomleft = (800, randint(50,200))
            pipe_bottom_rect.topleft = (800, randint(300,450))
            pipe_bottom_surf = choice(pipes)
            pipe_top_surf = pygame.transform.flip(pipe_bottom_surf, False, True)
            score = score + 1

        # score render
        score_msg = small_font.render(f"Score: {score:}", True, "yellow")

        # gravity
        bird_rect.y += gravity
        gravity += 0.2

        # game over
        if bird_rect.colliderect(pipe_top_rect) or bird_rect.colliderect(pipe_bottom_rect):
            game_active = False
        if bird_rect.bottom > 500 or bird_rect.top < 0:
            game_active = False
    else:
        screen.fill("lightgreen")
        screen.blit(game_over_msg, game_over_msg_rect)
        screen.blit(game_over_bird_surf, game_over_bird_rect)
        screen.blit(restart_msg, restart_msg_rect)

        # total score when game over

        end_score_msg = small_font.render(f"Your Score is: {score}", True, "black")
        end_score_msg_rect = end_score_msg.get_rect(center=(400, 320))
        screen.blit(end_score_msg, end_score_msg_rect)

    # frames per second
    pygame.display.update()
    clock.tick(60)