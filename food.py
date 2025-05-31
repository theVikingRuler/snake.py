class Food:
    def __init__(self, canvas, size, x, y, color):
        self.canvas = canvas
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.id = self._create_food()

    def _create_food(self):
        return self.canvas.create_oval(
            self.x, self.y,
            self.x + self.size, self.y + self.size,
            fill=self.color
        )

    def get_id(self):
        return self.id

    def get_coords(self):
        return self.canvas.coords(self.id) if self.id else None

    def remove(self):
        if self.canvas and self.id:
            self.canvas.delete(self.id)
            self.id = None
