from typing import Tuple

import pygame
import math

from Drawable import Drawable


class Point(Drawable):
    def __init__(self, pos: Tuple[int, int], radius=10, color='black', on_selected_color='green'):
        super().__init__(pos)
        self.color = color
        self.radius = radius
        self.on_selected_color = on_selected_color

    def draw(self, screen):
        pygame.draw.circle(screen, self.on_selected_color if self.selected else self.color, self.pos, self.radius)

    def is_clicked(self, c_pos: Tuple[int, int]):
        return math.sqrt((c_pos[0] - self.pos[0]) ** 2 + (c_pos[1] - self.pos[1]) ** 2) < self.radius
