import pygame

#C
COLOR_ORANGE = (255, 100, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (50, 255, 50)
COLOR_CYAN = (0, 128, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_PINK = (255, 20, 147)
COLOR_RED = (255, 50, 50)
COLOR_ORANGE_BRIGHT = (255, 69, 0)
COLOR_PINK_2 = (255, 20, 147)

#E
ENTITY_SIZE = {
    'Player1': (80, 80),
    'Player2': (80, 80),
}
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Player1': 3,
    'Player2': 3,
    'Player1Shot': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shot': 5,
    'Enemy2Shot': 2
}

EVENT_ENEMY = pygame.USEREVENT +1

ENTITY_HEALTH ={
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 50,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shot': 20,
    'Enemy2Shot': 15
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0
}

EVENT_TIMEOUT = pygame.USEREVENT + 2

#M
MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT',
)



#T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 40000

#P
PLAYER_KEY_UP ={
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w }

PLAYER_KEY_DOWN ={
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}
PLAYER_KEY_LEFT ={
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}
PLAYER_KEY_RIGHT ={
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}
PLAYER_KEY_SHOOT ={
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_LCTRL
}
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#S
SPAWN_TIME = 4000

SCORE_POS = {
    'Title': (WIN_WIDTH / 2 - 150, 50),
    'EnterName': (100, 150),
    'Label': (100, 200),
    'Name': (100, 250),
    0: (100, 250),
    1: (100, 280),
    2: (100, 310),
    3: (100, 340),
    4: (100, 370),
    5: (100, 400),
    6: (100, 430),
    7: (100, 460),
    8: (100, 490),
    9: (100, 520),
}