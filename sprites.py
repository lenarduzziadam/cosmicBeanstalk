import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game; # Reference to the main game class
        self._layer = PLAYER_LAYER # Set player layer (used for drawing order)
        self.groups = self.game.all_sprites
        
        # Add player to the all_sprites group directly
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        # Set player position and size based on tile size
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        # Create a surface for the player and fill it with a color
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(MPURPLE) # Fill with a mixed purple color
        
        # Define the player's rectangular area for movement and collisions
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
   
    def update(self):
        pass