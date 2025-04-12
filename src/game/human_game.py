from dataclasses import dataclass
from .game import Game
import pygame as pg
from action import Action


@dataclass
class HumanGame(Game):
    def _check_events(self, event: pg.event.Event) -> None:
        super()._check_events(event=event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.action = Action.left
            elif event.key == pg.K_RIGHT:
                self.action = Action.right
            elif event.key == pg.K_UP:
                self.action = Action.up
            elif event.key == pg.K_DOWN:
                self.action = Action.down
