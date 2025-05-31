import tkinter as tk
import time
from snake import Snake
from game import Game

class SnakeGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas_size = 400
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="black")
        self.canvas.pack()
        self.running = False
        self.home_screen() 
        

    def home_screen(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            200, 180,
            text=self.root.title(),
            fill="white",
            font=("Helvetica", 16),
            anchor="center"
        )

        self.play_text = self.canvas.create_text(
            200, 220,
            text="Play",
            fill="white",
            font=("Helvetica", 16),
            anchor="center",
            tags="play"
        )

        self.canvas.tag_bind("play", "<Button-1>", self.start_game)


    def start_game(self, event=None):
        self.canvas.delete("all")
        self.snake = Snake(self.canvas, 200, 200)
        self.game = Game(self.root, self.canvas, self.snake)
        self.root.bind("<KeyPress>", self.game.on_key_press)
        self.running = True
        self.game.place_small_food()
        self.game.place_large_food()
        self.game_loop()


    def game_loop(self):
        if not self.running:
            return

        self.snake.move_snake(self.game.current_direction)
        
        self.handle_collisions()

        if self.snake.check_self_collision():
            self.end_game("You collided with yourself!")

        self.root.after(150, self.game_loop)

    def handle_collisions(self):
        overlapping = self.snake.get_overlapping_shapes()

        if self.game.SMALL_FOOD and self.game.SMALL_FOOD.get_id() in overlapping:
            self.snake.grow()
            self.canvas.delete(self.game.SMALL_FOOD.get_id())
            self.game.place_small_food()

        if self.game.LARGE_FOOD and self.game.LARGE_FOOD.get_id() in overlapping:
            self.snake.grow()
            self.snake.grow()  # Bonus growth
            self.canvas.delete(self.game.LARGE_FOOD.get_id())
            self.game.LARGE_FOOD = None  # Avoid multiple deletes

    def end_game(self, message):
        self.running = False
        self.canvas.create_text(
            self.canvas_size // 2,
            self.canvas_size // 2,
            text=message,
            fill="white",
            font=("Helvetica", 20, "bold")
        )

        self.root.after(2000, self.home_screen)

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeGameApp(root)
    root.mainloop()
