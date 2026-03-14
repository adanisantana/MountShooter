import sys
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from cod.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPANW_TIME, COLOR_GREEN, TIMEOUT_STEP, \
    EVENT_TIMEOUT, TIMEOUT_LEVEL
from cod.Enemy import Enemy
from cod.Entity import Entity
from cod.EntityFactory import EntityFactory
from cod.EntityMediator import EntityMediator
from cod.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list:list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPANW_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        #pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        #pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            self.window.fill((0, 0, 0))
            clock.tick(60)
            for ent in self.entity_list[:]:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == 'Player1':
                        self.level_text(14, f'Player1 - HEALTH:{ent.health} | Score: {ent.score}',COLOR_GREEN,(10, 25))
                    if ent.name == 'Player2':
                        self.level_text(14, f'Player2 - HEALTH:{ent.health} | Score: {ent.score}',COLOR_GREEN,(10, 45))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return True


            self.level_text(14, f'{self.name}- Timeout{self.timeout / 1000 :.1f}s', COLOR_WHITE,(10,5))
            self.level_text(14, f'fps:{clock.get_fps() :.0f}',COLOR_WHITE,(10, WIN_HEIGHT -35))
            self.level_text(14,f'{len(self.entity_list)}',COLOR_WHITE,(10, WIN_HEIGHT -20))
            pygame.display.flip()

            #Collision
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self,text_size:int, text:str, text_color:tuple,text_pos:tuple):
        text_font:Font= pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf:Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect:Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)

        pass