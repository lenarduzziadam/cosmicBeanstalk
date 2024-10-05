import pygame
from config import *
import math
import random

class Level:
    def __init__(self):
        
        #get display surface
        self.dis_surface = pygame.display.get_surface
        
        #new sprite groups setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
    
    def run(self):
        #updates and draws game
        pass
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
        self.facing = 'down'
        self.animation_loop = 1
        
        # Create a surface for the player and fill it with a color or sprite image
        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        
        # Define the player's rectangular area for movement and collisions
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        #Sets up animations for different movements
        self.down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        self.up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        self.left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]
    
    #update function in Player class
    def update(self):
        #calls movement
        self.movement() 
        
        #updates animations
        self.animate()
        self.collide_enemy()
        
        #adds change in x and y
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
        #resets x change and y change to 0
        self.x_change = 0
        self.y_change = 0
        
        self.animation_loop = 1
        self.collide_enemy()
    
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
    
    
    def animate(self):


        #ifs for assigning animations
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 3:
                    self.animation_loop = 1
    
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        
        if hits:
            self.kill()
            self.game.playing = False
    
    #Handles collisions for barriers/Blocks            
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.right = hits[0].rect.left
                elif self.x_change < 0:
                    self.rect.left = hits[0].rect.right
                self.x_change = 0

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.bottom = hits[0].rect.top
                elif self.y_change < 0:
                    self.rect.top = hits[0].rect.bottom
                self.y_change = 0
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
       
        #defines enemy sprite
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change = 0
        self.y_change = 0
        
        #defines enemy movment and animation loop
        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7, 40)
        
        #grabs image from sprite sheet
        self.image = self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.left_animations = [self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height)]
    #update function for Enemy class
    def update(self):
        
        self.movement()
        self.animate()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        # Save the old position to reset if collision occurs
        old_x = self.rect.x
        old_y = self.rect.y
        
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED;
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
                
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED;
            self.movement_loop +=1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'
    
         # Apply movement
        self.rect.x += self.x_change

        # Check for collisions with blocks
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            # If a collision happens, reverse direction and move the enemy back slightly
            if self.facing == 'left':
                self.rect.x = old_x  # Reset position to avoid overlap with the block
                self.facing = 'right'  # Reverse direction
                self.rect.x += ENEMY_SPEED  # Push back to prevent getting stuck
                
            elif self.facing == 'right':
                self.rect.x = old_x  # Reset position to avoid overlap with the block
                self.facing = 'left'  # Reverse direction
                self.rect.x -= ENEMY_SPEED  # Push back to prevent getting stuck
            
    def animate(self):
  
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height)
            
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height)
            
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        #Handles barrier sprite, and behavior
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
        

class Button:
    def __init__(self, x, y, width, height, foreg, backg, content, fontsize):
        self.font = pygame.font.Font('Times New Roman/times new roman.ttf', fontsize)
        self.content = content
        
        #cordinates and size definers for button
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        #sets foreground and background
        self.foreg = foreg
        self.backg = backg
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.backg)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.text = self.font.render(self.content, True, self.foreg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)
        
    def is_pressed(self, pos, pressed):
        
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
        

class Attack(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.animation_loop = 0
        
        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.right_animations = [self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height)]

        self.down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

        self.left_animations = [self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height)]

        self.up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]
        
    def update(self):
        self.animate()
        self.collide()
    
    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
    
    def animate(self):
        direction = self.game.player.facing
        

        if direction == 'up':
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        
        if direction == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
                
        if direction == 'right':
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
                
        if direction == 'left':
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
                

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Move the entity's position based on the camera
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Center the camera on the target (player)
        x = -target.rect.centerx + int(SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(SCREEN_HEIGHT / 2)

        # Limit scrolling to the map size
        x = min(0, x)  # Left boundary
        y = min(0, y)  # Top boundary
        x = max(-(self.width - SCREEN_WIDTH), x)  # Right boundary
        y = max(-(self.height - SCREEN_HEIGHT), y)  # Bottom boundary

        self.camera = pygame.Rect(x, y, self.width, self.height)
