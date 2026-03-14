from cod.Const import ENTITY_SPEED, WIN_WIDTH
from cod.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position:tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
        if self.rect.left > WIN_WIDTH:
            self.health = 0