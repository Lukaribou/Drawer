from typing import Tuple


class Drawable:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos
        self.selected = False

    def draw(self, screen):
        pass

    def is_clicked(self, click_coords: Tuple[int, int]):
        pass

    def on_clicked(self):
        self.selected = True
