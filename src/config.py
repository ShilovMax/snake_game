from pathlib import Path
from torch.nn import Linear, ReLU, Softmax, MSELoss
from torch.optim import Adam

# SCORE
SCORE_FONT_SIZE = 36
SCORE_TEXT_RECT_SIZE = (80, 30)
SCORE_TEXT = "SCORE 0"
SCORE_COLOR = (100, 100, 200)
SCORE_SURFACE_SIZE = (400, SCORE_TEXT_RECT_SIZE[1])
SCORE_BACKGROUND_COLOR = (230, 230, 230)

# PLAYBOARD
PLAYBOARD_WIDTH = 400
PLAYBOARD_HEIGHT = 400
PLAYBOARD_SIZE = (PLAYBOARD_WIDTH, PLAYBOARD_HEIGHT)
PLAYBOARD_BACKGROUND_COLOR = (255, 255, 255)  # WHITE


# GAME
CAPTION = "SNAKE"
SCREEN_WIDTH = PLAYBOARD_WIDTH
SCREEN_HEIGHT = PLAYBOARD_HEIGHT + SCORE_TEXT_RECT_SIZE[1]
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = (0, 0, 0)  # BLACK
FPS = 60
CELL_SIZE = 80
N_WIDTH = PLAYBOARD_WIDTH // CELL_SIZE
N_HEIGHT = PLAYBOARD_HEIGHT // CELL_SIZE

# Q LEARNING
LEARNING_RATE = 0.1
GAMMA = 0.9
EPSILON = 0.3
MIN_EPSILON = 0.01
EPSILON_DECAY = 0.995
MATRIX_SIZE = (
    N_WIDTH * N_HEIGHT,
    N_WIDTH * N_HEIGHT,
    4,
)

# PATH
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
MATRIX_FILE = ""  # MODELS_DIR / "q_matrix.npy"
TORCH_FILE = ""
# TORCH_FILE = MODELS_DIR / "model_v2.pth"
# TORCH_FILE = MODELS_DIR / "model_v2_batch.pth"
# DRAWING OBJECTS
DEFAULT_APPLE_X = 0  # N_WIDTH - 1
DEFAULT_APPLE_Y = 0  # N_HEIGHT - 1
DEFAULT_APPLE_COLOR = (255, 0, 0)  # RED

DEFAULT_SNAKEITEM_X = N_WIDTH - 1  # 0
DEFAULT_SNAKEITEM_Y = N_WIDTH - 1  # 0
DEFAULT_SNAKEITEM_COLOR = (0, 255, 0)  # GREEN

DEFAULT_GRID_X = N_WIDTH
DEFAULT_GRID_Y = N_HEIGHT
DEFAULT_GRID_COLOR = (100, 100, 100)  # GRAY

# NEURAL NETWORK
NN_LAYERS = [
    {
        "name": "layer0",
        "func": Linear(4, 4),
    },
    {
        "name": "softmax0",
        "func": Softmax(),
    },
]

NN_LAYERS = [
    {
        "name": "layer0",
        "func": Linear(8, 8),
    },
    {
        "name": "relu0",
        "func": ReLU(),
    },
    {
        "name": "layer1",
        "func": Linear(8, 4),
    },
    {
        "name": "softmax0",
        "func": Softmax(),
    },
]

# DEEP Q LEARNING
OPTIMIZER = Adam
LOSS_FUNC = MSELoss()
