from dataclasses import asdict, dataclass, field

from utils.state import PlusShapedVisionState, PlusShapedVisionLessOrGreateStateState

from .base_deep_q_learning_game import BaseDeepQLearningGame


@dataclass
class LongSnakeDeepQLearningGame(BaseDeepQLearningGame):
    state: type[PlusShapedVisionLessOrGreateStateState] = field(
        init=False, default=PlusShapedVisionLessOrGreateStateState
    )

    def _get_state(self) -> PlusShapedVisionLessOrGreateStateState:
        return PlusShapedVisionLessOrGreateStateState(
            **asdict(super()._get_state()),
            **asdict(
                self._get_barriers_info(),
            ),
        )

    def _get_barriers_info(self) -> PlusShapedVisionState:
        state = PlusShapedVisionState()

        directions = {
            (0, 1): "is_barrier_on_bottom",
            (0, -1): "is_barrier_on_top",
            (1, 0): "is_barrier_on_right",
            (-1, 0): "is_barrier_on_left",
        }

        for x, y in self.snake.body_visible_coords:
            dx = x - self.snake_head.x
            dy = y - self.snake_head.y
            if (dx, dy) in directions:
                setattr(state, directions[(dx, dy)], True)

        if self.snake_head.x == 0:
            state.is_barrier_on_left = True
        elif self.snake_head.x == self.playboard.width:
            state.is_barrier_on_right = True

        if self.snake_head.y == 0:
            state.is_barrier_on_top = True
        elif self.snake_head.y == self.playboard.height:
            state.is_barrier_on_bottom = True

        return state

    def _set_playboard_from_state(self, state: PlusShapedVisionLessOrGreateStateState):
        print(5555555, str(state), int(str(state), 2))
        snake_x, snake_y, apple_x, apple_y = (
            super()._get_snake_head_and_apple_from_state(state=state)
        )
        self.snake.body = self.snake.body[:1]
        match sum(list(state)[4:]):
            case 0:
                self.snake.head.coords = (snake_x, snake_y)
            case 1:
                self.snake.head.coords = (snake_x, snake_y)
                if state.is_barrier_on_left:
                    self.snake.add_item(x=snake_x - 1)
                elif state.is_barrier_on_right:
                    self.snake.add_item(x=snake_x + 1)
                elif state.is_barrier_on_top:
                    self.snake.add_item(y=snake_y - 1)
                elif state.is_barrier_on_bottom:
                    self.snake.add_item(y=snake_y + 1)

            case 2:
                if state.is_barrier_on_left:
                    if state.is_barrier_on_right:
                        if snake_x > 1:
                            snake_x += 1
                            self.snake.head.coords = (snake_x, snake_y)
                            self.snake.add_item(x=snake_x - 1)
                        else:
                            snake_x -= 1
                            self.snake.head.coords = (snake_x, snake_y)
                            self.snake.add_item(x=snake_x + 1)
                    elif state.is_barrier_on_top:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x - 1)
                        self.snake.add_item(x=snake_x - 1, y=snake_y - 1)
                        self.snake.add_item(x=snake_x, y=snake_y - 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y - 1)
                    elif state.is_barrier_on_bottom:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x - 1)
                        self.snake.add_item(x=snake_x - 1, y=snake_y + 1)
                        self.snake.add_item(x=snake_x, y=snake_y + 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y + 1)

                elif state.is_barrier_on_right:
                    if state.is_barrier_on_top:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x + 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y - 1)
                        self.snake.add_item(x=snake_x, y=snake_y - 1)
                        self.snake.add_item(x=snake_x - 1, y=snake_y - 1)
                    elif state.is_barrier_on_bottom:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x + 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y + 1)
                        self.snake.add_item(x=snake_x, y=snake_y + 1)
                        self.snake.add_item(x=snake_x - 1, y=snake_y + 1)

                elif state.is_barrier_on_top:
                    if state.is_barrier_on_bottom:
                        if snake_y > 1:
                            snake_y += 1
                            self.snake.head.coords = (snake_x, snake_y)
                            self.snake.add_item(y=snake_y - 1)
                        else:
                            snake_y -= 1
                            self.snake.head.coords = (snake_x, snake_y)
                            self.snake.add_item(y=snake_y + 1)

            case 3:
                if state.is_barrier_on_left:
                    if state.is_barrier_on_right and state.is_barrier_on_top:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x - 1, y=snake_y)
                        self.snake.add_item(x=snake_x - 1, y=snake_y - 1)
                        self.snake.add_item(x=snake_x, y=snake_y - 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y - 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y)
                        self.snake.add_item(x=snake_x + 1, y=snake_y + 1)

                    elif state.is_barrier_on_right and state.is_barrier_on_bottom:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x - 1, y=snake_y)
                        self.snake.add_item(x=snake_x - 1, y=snake_y + 1)
                        self.snake.add_item(x=snake_x, y=snake_y + 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y + 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y)
                        self.snake.add_item(x=snake_x + 1, y=snake_y - 1)

                    elif state.is_barrier_on_top and state.is_barrier_on_bottom:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x, y=snake_y - 1)
                        self.snake.add_item(x=snake_x - 1, y=snake_y - 1)
                        self.snake.add_item(x=snake_x - 1, y=snake_y)
                        self.snake.add_item(x=snake_x - 1, y=snake_y + 1)
                        self.snake.add_item(x=snake_x, y=snake_y + 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y + 1)

                elif state.is_barrier_on_right:
                    if state.is_barrier_on_top and state.is_barrier_on_bottom:
                        self.snake.head.coords = (snake_x, snake_y)
                        self.snake.add_item(x=snake_x, y=snake_y - 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y - 1)
                        self.snake.add_item(x=snake_x + 1, y=snake_y)
                        self.snake.add_item(x=snake_x + 1, y=snake_y + 1)
                        self.snake.add_item(x=snake_x, y=snake_y + 1)
                        self.snake.add_item(x=snake_x - 1, y=snake_y + 1)
        print(self.snake.coords)
        print()
        self.apple.coords = (apple_x, apple_y)
