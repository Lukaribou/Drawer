from typing import Tuple

import pygame

from Drawable import Drawable


class Point(Drawable):
    def __init__(self, pos: Tuple[int, int], radius=10, color='black', on_selected_color='green'):
        super().__init__(pos)
        self.color = color
        self.radius = radius
        self.on_selected_color = on_selected_color

    def draw(self, screen):
        pygame.draw.circle(screen, self.on_selected_color if self.selected else self.color, self.pos, self.radius)

    def is_clicked(self, click_coords: Tuple[int, int]):
        return click_coords[0] ** 2 + click_coords[1] ** 2 - self.radius ** 2 <= 0

    def on_clicked(self):
        self.selected = True
        print('clicked')
