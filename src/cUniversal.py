from sys import exit
import pygame

class Program:

    screen = 0 

    def __init__(self):

        self.windowResolutionHW = (1400, 1000)

    def init_screen(self):

        self.screen = pygame.display.set_mode(self.windowResolutionHW, pygame.SCALED, 0, 0, 1)

programData = Program()

def game_exit():

    pygame.quit()
    exit()
