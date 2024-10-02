import pygame
from config import *
import math
import random

class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()
    
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

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
        
        #handling external sprite images
        
        # Create a surface for the player and fill it with a color or sprite image
        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        
        # Define the player's rectangular area for movement and collisions
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
   
    def update(self):
        #calls movement
        self.movement() 
        
        #adds change in x and y
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
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

    
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            
            if hits:
                #handles leftward collisons
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                
                #handles rightward collisions
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            
            if hits:
                #handles leftward collisons
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                
                #handles rightward collisions
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom 
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = BLOCK_LAYER;
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
#Class to define ground sprites
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y