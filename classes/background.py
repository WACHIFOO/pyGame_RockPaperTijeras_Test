import pygame


class Background:
    def __init__(self):
        self.background = pygame.image.load("sprites/background/background.png")

    def blit(self, screen):
        screen.blit(self.background, self.background.get_rect())
