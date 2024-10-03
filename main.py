import pygame;
from sprites import *;
from config import *;
import sys

class Game:
    def __init__(self):
        pygame.init();

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_name = pygame.display.set_caption('Cosmic Beanstalk')
        self.clock = pygame.time.Clock()

        self.running = True;
        self.font = pygame.font.Font('Times New Roman/times new roman italic.ttf', 30)
        
        self.character_spritesheet = SpriteSheet('img/character.png')
        self.terrain_spritesheet = SpriteSheet('img/terrain.png')
        self.enemy_spritesheet = SpriteSheet('img/enemy.png')
        self.intro_background = pygame.image.load('./img/introbackground.png')
        
    #method to create home_map
    def createMap(self):
        #Loop and nested for finding B and P (For adding barriers and Player to map)
        for i, row in enumerate(home_map):
            for j, column in enumerate(row):
                Ground(self, j, i)
                
                if column == "B": #creates a barrier
                    Block(self, j, i)
                
                if column == "E": #creates an enemy
                    Enemy(self, j, i)
                
                if column == "P": #spawns player sprite onto player
                    Player(self, j, i)

    def new(self):
        # Start of new game
        self.playing = True
        
        # Initialize sprite groups for handling various objects in the game
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates() #Used for walls/obstacles
        self.enemies = pygame.sprite.LayeredUpdates() #handles enemy sprites
        self.attacks = pygame.sprite.LayeredUpdates() #handles attack animations
        
        self.createMap()
       
       #self.player = Player(self, 1, 2); #initializes player at position (1,2)
        
    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
    def update(self):
        #updating game loops
        self.all_sprites.update()
        
        
    def draw(self): 
        #Draws everthing onto screen
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
        
    def main(self):
        #game loop
        while self.playing:
            self.events() ##handles events such as player inputs/Quiting
            self.update() #updates game objects
            self.draw() #draws objects to screen
        self.running = False
        
    def game_over(self):
        #TODO: handles what occurs when game is over(Placehodler for now).
        pass
    
    def intro_screen(self):
        intro = True
        
        title = self.font.render('The Cosmic Stalk', True, BLACK)
        title_rect = title.get_rect(x = 10, y = 10)
        
        play_button = Button(10, 50, 100, 50, MPURPLE, BLACK, 'Play', 30)
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            
            #gets position of mouse on screen
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            
            pygame.display.update()

# Create a game instance and starts intro screen, followed game loop
g = Game()
g.intro_screen()
g.new()

#keeps game running until player quits
while g.running:
    g.main()
    g.game_over()

#exits game, then system when game loop ends.    
pygame.quit()
sys.exit()