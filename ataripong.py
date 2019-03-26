# Modules required for the game
import pygame, sys, time, random, os

# Initializing screen and values
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Atari Pong')
white = (255, 255, 255)
black = (0, 0, 0)
player1_score = 0
player2_score = 0
ball_x = 400
ball_y = 300
player1_x = 20
player2_x = 760
player1_y = 200
player2_y = ball_y
y_change1 = 0
ballSpeeds = [6, -6]
ball_x_speed = random.choice(ballSpeeds)
ball_y_speed = random.choice(ballSpeeds)
player1_score = 0
player2_score = 0
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 65)

# Game loop: will execute until pygame.QUIT == True
while True:
    player2_y = ball_y - 65
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                        y_change1 = -8
                if event.key == pygame.K_DOWN:
                        y_change1 = 8
        if event.type == pygame.KEYUP:
                y_change1 = 0
    if player1_y + 150 >= 600:
        player1_y = 450
    if player1_y <= 0:
        player1_y = 0
    if player2_y + 150 >= 600:
        player2_y = 450
    if player2_y <= 0:
        player2_y = 0
    if ball_x >= 800 or ball_x <= 0:
        ball_x_speed = -ball_x_speed
    if ball_y >= 600 or ball_y <= 0:
        ball_y_speed = -ball_y_speed
    if player1_x + 20 == ball_x and (ball_y > player1_y and ball_y < player1_y + 150):
        ball_x_speed = -ball_x_speed
    if player2_x == ball_x and (ball_y > player2_y and ball_y < player2_y + 150):
        ball_x_speed = -ball_x_speed
    if ball_x <= 0:
        player2_score += 1
        time.sleep(2)
        ball_x = 400
        ball_y = 300
        ball_x_speed = random.choice(ballSpeeds)
        ball_y_speed = random.choice(ballSpeeds)
        player1_y = 240
        player2_y = 240
    elif ball_x >= 800:
        player1_score += 1
        time.sleep(2)
        ball_x = 400
        ball_y = 300
        ball_x_speed = random.choice(ballSpeeds)
        ball_y_speed = random.choice(ballSpeeds)
        player1_y = 240
        player2_y = 240
    player1_y += y_change1
    ball_x += ball_x_speed
    ball_y += ball_y_speed
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, [player1_x, player1_y, 20, 150])
    pygame.draw.rect(gameDisplay, white, [player2_x, player2_y, 20, 150])
    pygame.draw.rect(gameDisplay, white, [ball_x, ball_y, 10, 10])
    label1 = myfont.render(str(player1_score), 1, (255,255,255))
    label2 = myfont.render(str(player2_score), 1, (255,255,255))
    gameDisplay.blit(label1, (100, 100))
    gameDisplay.blit(label2, (650, 100))
    pygame.display.update()
    clock.tick(60)
