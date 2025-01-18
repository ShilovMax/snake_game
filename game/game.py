from .base import BaseGame
from dataclasses import dataclass
from drawing_objects import Apple, Snake, Grid
import pygame as pg


@dataclass
class Game(BaseGame):
    apple: Apple
    snake: Snake
    grid: Grid

    def _draw(self) -> None:
        self.screen.fill(self.background_color)
        self.apple.draw(surface=self.screen)
        self.snake.draw(surface=self.screen)
        self.grid.draw(surface=self.screen)
        pg.display.flip()
