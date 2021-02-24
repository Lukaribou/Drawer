from typing import Tuple

import pygame

from Drawable import Drawable


class Text(Drawable):
    def __init__(self, pos: Tuple[int, int], text: str, size=30, color='black', font='Comic Sans MS'):
        super().__init__(pos)
        self.text = text
        self.font = pygame.font.SysFont(font, size)
        self.size = size
        self.color = pygame.Color(color) if isinstance(color, str) else color

    def get_text(self):
        return self.text

    def set_text(self, new_text: str):
        self.text = new_text

    def draw(self, screen):
        text = self.font.render(self.text, False, self.color)
        screen.blit(text, self.pos)
