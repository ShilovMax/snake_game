import pygame as pg
from drawing_objects import Apple, Snake, Grid
from game import Game
import config as cf

pg.init()


apple = Apple(x=4, y=4, color=cf.RED)
snake = Snake(x=0, y=0, color=cf.GREEN)
grid = Grid(x=5, y=5, color=cf.GRAY)
game = Game(
    caption=cf.CAPTION,
    screen_size=(cf.WIDTH, cf.HEIGHT),
    background_color=cf.WHITE,
    fps=cf.FPS,
    apple=apple,
    snake=snake,
    grid=grid,
)
game.play()
