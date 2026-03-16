from abc import ABC, abstractmethod
import pygame

from cod.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, ENTITY_SIZE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        if name in ENTITY_SIZE:
            self.surf = pygame.transform.scale(self.surf, ENTITY_SIZE[name])

        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass
