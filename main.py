import pygame;

pygame.init();

SCREEN_WIDTH = 800;
SCREEN_HEIGHT = 600;

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((200, 150, 30, 30))

run = True
while run:
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (100, 20, 135), player)
    
    key = pygame.key.get_pressed();
    
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
        
    elif key[pygame.K_w] == True: 
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;
        
        if event.type == pygame.KEYDOWN:
            print("Key pressed baby")
        if event.type == pygame.KEYUP:
            print("Why did you stop?")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clickity Clackity")
        if event.type == pygame.MOUSEBUTTONUP:
            print("Atleast buy something will YA! GEEZ!")
        
        
    pygame.display.update();

pygame.quit()