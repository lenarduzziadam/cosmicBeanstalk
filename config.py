#Sizes
SCREEN_WIDTH = 1000;
SCREEN_HEIGHT = 500;
TILESIZE = 32;

#Framerates
FPS = 60;

#Colors
MPURPLE = (100, 20, 135);
BLACK = (0, 0, 0);
GREEN = (0, 255, 0);
RED = (255, 0, 0);
WHITE = (255, 255, 255)
BLUE = (25, 25, 200)
OFFBLACK = (23, 23, 23)
OFFWHITE = (254, 254, 254)


#LAYER Classifications
PLAYER_LAYER = 4;
ENEMY_LAYER = 3;
BLOCK_LAYER = 2;
GROUND_LAYER = 1;

#SPEED Classifications
PLAYER_SPEED = 2;
ENEMY_SPEED = 1;

#Enviorment
home_map = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B.........................E..............E....B',
    'B....E................................EEEE....B',
    'B.................................E...........B',
    'B...........BBB...............................B',
    'B.............................................B',
    'B..........................................E..B',
    'B.....................P.......................B',
    'B..............................BBB............B',
    'B..........E...........................E......B',
    'B...................BBB.......................B',
    'B.............................................B',
    'B....B...............E....E..........B....E...B',
    'B............................................EB',
    'B.............................................B',
    'B.........................BBBBBB..............B',
    'B........BBBBBBB..............................B',
    'B.....................E.......................B',
    'B..................................E..........B',
    'B......................EE..........B..........B',
    'B.............................................B',
    'B.............E...............................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]

world_map = [
    '                                                                  ',
    '                                                                  ',
    '                t  t                                              ',
    '        X     XXXXXXXXXs                   XX   X                 ',
    ' tXXXt     XX         XX                XXXX tt XX                ',
    ' XX XX                                      XXXXX                 ',
    '          Xt    t           t  t   X                            G ',
    '        XXXXXX  XXXXs    XXXXXXXXXXX  XX              tt t     XXX',
    ' P   XX  X XX X  X XXXt     X XX  XX  XXX  XXXXXXXXs  XXXXXX      ',
    'XXXXXXX  X  X X  X  XXXXXXXXX XX  XX  XXX  XX XX XXXXXXX  X       ',
]

tile_size = 50
WIDTH, HEIGHT = 1000, len(world_map) * tile_size