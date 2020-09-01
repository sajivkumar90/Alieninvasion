import sys
import pygame

class AlienInvasion:
    """ Overall class to manage games assets and behaviour"""
    def __init__(self):
        pygame.init()
        

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
