import pygame as pg
from dataclasses import dataclass
import sys

pg.init()


@dataclass
class BaseGame:
    caption: str
    screen_size: tuple[int, int]
    background_color: tuple[int, int, int]
    fps: int

    def __post_init__(self) -> None:
        pg.display.set_caption(title=self.caption)
        self.screen = pg.display.set_mode(size=self.screen_size)

        self.is_win: bool = False
        self.is_game_over: bool = False

    def play(self) -> None:
        self._draw()
        while not self.is_win and not self.is_game_over:
            self._handle_events()
            self._update()
            pg.time.Clock().tick(self.fps)

    def _draw(self) -> None:
        self.screen.fill(self.background_color)
        pg.display.flip()

    def _handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def _update(self) -> None:
        pass


CAPTION = "SNAKE"
WIDTH = 400
HEIGHT = 400

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

FPS = 60

CELL_SIZE = 80


@dataclass
class DrawingObject:
    x: int
    y: int
    color: tuple[int, int, int]

    def draw(self, surface: pg.Surface) -> None:
        pg.draw.rect(
            surface,
            self.color,
            (
                self.x * CELL_SIZE,
                self.y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            ),
        )


class Apple(DrawingObject):
    pass


class Snake(DrawingObject):
    pass


class Grid(DrawingObject):
    def draw(self, surface: pg.Surface) -> None:
        self.draw_vertical_lines(surface=surface)
        self.draw_horizontal_lines(surface=surface)

    def draw_vertical_lines(self, surface: pg.Surface) -> None:
        for i in range(1, self.x):
            pg.draw.line(
                surface,
                self.color,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, self.y * CELL_SIZE),
            )

    def draw_horizontal_lines(self, surface: pg.Surface) -> None:
        for i in range(1, self.y):
            pg.draw.line(
                surface,
                self.color,
                (0, i * CELL_SIZE),
                (self.x * CELL_SIZE, i * CELL_SIZE),
            )


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


apple = Apple(x=4, y=4, color=RED)
snake = Snake(x=0, y=0, color=GREEN)
grid = Grid(x=5, y=5, color=GRAY)
game = Game(
    caption=CAPTION,
    screen_size=(WIDTH, HEIGHT),
    background_color=WHITE,
    fps=FPS,
    apple=apple,
    snake=snake,
    grid=grid,
)
game.play()
