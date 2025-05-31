from food import Food
import random

class Game:
    def __init__(self, root, canvas, snake):
        self.root = root
        self.canvas = canvas
        self.snake = snake

        self.canvas_width = 400
        self.canvas_height = 400
        self.snake_segment_size = self.canvas_height // 20

        self.small_food_size = self.snake_segment_size / 2
        self.large_food_size = self.snake_segment_size

        self.SMALL_FOOD = None
        self.LARGE_FOOD = None

        self.current_direction = "Up"
        self.opposites = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

    def on_key_press(self, event):
        key = event.keysym
        if key in self.opposites and key != self.opposites[self.current_direction]:
            self.current_direction = key

    def get_canvas_size(self):
        return [self.canvas_width, self.canvas_height]

    def update_canvas_size(self, width, height):
        self.canvas_width = width
        self.canvas_height = height
        self.snake.update_canvas_size(width, height)

    def get_random_coords(self):
        grid_x = random.randint(0, (self.canvas_width // self.snake_segment_size) - 1)
        grid_y = random.randint(0, (self.canvas_height // self.snake_segment_size) - 1)
        x = grid_x * self.snake_segment_size
        y = grid_y * self.snake_segment_size
        return [x, y]

    def place_small_food(self):
        margin = (self.snake_segment_size - self.small_food_size) / 2
        x, y = self.get_random_coords()
        self.SMALL_FOOD = Food(
            self.canvas,
            self.small_food_size,
            x + margin,
            y + margin,
            'blue'
        )

    def place_large_food(self):
        x, y = self.get_random_coords()
        self.LARGE_FOOD = Food(self.canvas, self.large_food_size, x, y, 'red')
        self.root.after(5000, self.LARGE_FOOD.remove)
        self.root.after(10000, self.place_large_food)
