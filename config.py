import pygame


class Config():
    # Set up the colours
    BLACK     = (0,0,0)
    WHITE     = (255,255,255)

    window_width = 400
    window_height = 300

    display_surf = pygame.display.set_mode((window_width,window_height))

    fps_clock = pygame.time.Clock()
    fps = 40 # Number of frames per second