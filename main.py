from typing import List

import pygame

from Drawable import Drawable
from Point import Point
from Text import Text


class Game:
    def __init__(self):
        import os

        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (pygame.display.Info().current_w / 5, 100)
        self.screen = pygame.display.set_mode(
            (int(pygame.display.Info().current_w // 1.5), int(pygame.display.Info().current_h // 1.5)))
        pygame.display.set_caption("Drawer")
        self.screen.fill('white')

        self.mode = Text((10, 2), 'point')
        self.objects: List[Drawable] = []

        self.__listen_events()

    def __listen_events(self):
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_p:
                    self.mode.set_text('point')
                elif ev.key == pygame.K_s:
                    self.mode.set_text('select')
                elif ev.key == pygame.K_d:
                    self.mode.set_text('delete')
            elif ev.type == pygame.MOUSEBUTTONUP:
                if self.mode.get_text() == 'point':
                    self.objects.append(Point(pygame.mouse.get_pos()))
                else:
                    for item in self.objects:
                        if item.is_clicked(pygame.mouse.get_pos()):
                            if self.mode.get_text() == 'select':
                                item.on_clicked()
                            elif self.mode.get_text() == 'delete':
                                self.objects.remove(item)

            # draw all again
            self.screen.fill('white')
            for item in self.objects:
                item.draw(self.screen)
            self.mode.draw(self.screen)
            pygame.display.update()
        self.quit()

    @staticmethod
    def quit():
        pygame.quit()


if __name__ == '__main__':
    game = Game()
