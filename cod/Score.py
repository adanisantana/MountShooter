import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, K_RETURN, KEYDOWN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from cod.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTION, COLOR_WHITE, COLOR_BLACK, COLOR_CYAN, COLOR_ORANGE, \
    COLOR_ORANGE_BRIGHT, COLOR_PINK, COLOR_PINK_2
from cod.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'Score', COLOR_ORANGE, SCORE_POS['Title'])

            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter your name (4 chars):'
            elif game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (4 chars):'
            else:  # MENU_OPTION[2]
                score = max(player_score[0], player_score[1])
                text = 'Enter Winner name (4 chars):'


            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])
            self.score_text(30, name, COLOR_YELLOW, SCORE_POS['Name'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'TOP 10 SCORE', COLOR_ORANGE, SCORE_POS['Title'])

            # Labels em Ciano para separar o cabeçalho dos dados
            self.score_text(20, 'NAME      SCORE           DATE', COLOR_PINK_2, SCORE_POS['Label'])

            for index, player_score in enumerate(list_score):
                id_, name, score, date = player_score
                # Dados em Branco com sombra para leitura perfeita
                self.score_text(20, f'{name:4s}      {score:05d}      {date}', COLOR_WHITE,
                                SCORE_POS[index])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)

        # --- EFEITO DE SOMBRA ---
        shadow_surf: Surface = text_font.render(text, True, COLOR_BLACK).convert_alpha()
        self.window.blit(shadow_surf, (text_pos[0] + 2, text_pos[1] + 2))

        # --- TEXTO PRINCIPAL ---
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    return current_datetime.strftime("%H:%M - %d/%m/%Y")