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
        
        #sets change in x to placeholder 0
        self.x_change = 0
        self.y_change = 0
        
        # Create a surface for the player and fill it with a color
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(MPURPLE) # Fill with a mixed purple color
        
        # Define the player's rectangular area for movement and collisions
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
   
    def update(self):
        #calls movement
        self.movement() 
        
        #adds change in x and y
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        #resets x change and y change to 0
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        #Key press related movments
        keys = pygame.key.get_pressed()
        
        #Handles right and left
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
       
       #Handles up and down
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'