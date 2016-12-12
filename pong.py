import pygame
import sys
from pygame.locals import *

FPS = 200
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
LINE_THICKNESS = 10
PADDLE_SIZE = 50
PADDLE_OFFSET = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_arena():
    DISPLAYSURF.fill((0,0,0))
    #Draw outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOW_WIDTH,WINDOW_HEIGHT)), LINE_THICKNESS*2)
    #Draw centre line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOW_WIDTH/2),0),((WINDOW_WIDTH/2),WINDOW_HEIGHT), int(LINE_THICKNESS/4))


#Draws the paddle
def draw_paddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOW_HEIGHT - LINE_THICKNESS:
        paddle.bottom = WINDOW_HEIGHT - LINE_THICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINE_THICKNESS:
        paddle.top = LINE_THICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)


# draws the ball
def draw_ball(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)


def main():
    pygame.init()
    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Pong')

    ball_x = WINDOW_WIDTH/2 - LINE_THICKNESS/2
    ball_y = WINDOW_HEIGHT/2 - LINE_THICKNESS/2
    playerOnePosition = (WINDOW_HEIGHT - PADDLE_SIZE)/2
    playerTwoPosition = (WINDOW_HEIGHT - PADDLE_SIZE)/2

    paddle_1 = pygame.Rect(PADDLE_OFFSET, playerOnePosition, LINE_THICKNESS, PADDLE_SIZE)
    paddle_2 = pygame.Rect(WINDOW_WIDTH - PADDLE_OFFSET - LINE_THICKNESS, playerTwoPosition, LINE_THICKNESS, PADDLE_SIZE)
    ball = pygame.Rect(ball_x, ball_y, LINE_THICKNESS, LINE_THICKNESS)

    draw_arena()
    draw_paddle(paddle_1)
    draw_paddle(paddle_2)
    draw_ball(ball)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        draw_arena()
        draw_paddle(paddle_1)
        draw_paddle(paddle_2)
        draw_ball(ball)

if __name__=='__main__':
    main()



