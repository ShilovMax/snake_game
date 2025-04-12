from .rectangle import Rectangle


class Snake(Rectangle):
    def move_left(self) -> None:
        self.x -= 1

    def move_right(self) -> None:
        self.x += 1

    def move_up(self) -> None:
        self.y -= 1

    def move_down(self) -> None:
        self.y += 1
