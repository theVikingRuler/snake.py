class Snake:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 20
        self.canvas_width = 400
        self.canvas_height = 400
        self.body = []
        self.should_grow = False  # Delayed grow flag

        self.create_segment(x, y)

    def update_canvas_size(self, width, height):
        self.canvas_width = width
        self.canvas_height = height

    def create_segment(self, x, y):
        segment = self.canvas.create_rectangle(
            x, y, x + self.size, y + self.size,
            fill="green"
        )
        self.body.append(segment)

    def move_snake(self, direction):
        # Store current positions before move
        prev_coords = [self.canvas.coords(segment) for segment in self.body]

        # Move head
        if direction == "Left":
            self.x = (self.x - self.size) % self.canvas_width
        elif direction == "Right":
            self.x = (self.x + self.size) % self.canvas_width
        elif direction == "Up":
            self.y = (self.y - self.size) % self.canvas_height
        elif direction == "Down":
            self.y = (self.y + self.size) % self.canvas_height

        # Move head to new position
        self.canvas.coords(
            self.body[0],
            self.x, self.y,
            self.x + self.size, self.y + self.size
        )

        # Move body segments
        for i in range(1, len(self.body)):
            self.canvas.coords(self.body[i], *prev_coords[i - 1])

        # Add a new segment if requested
        if self.should_grow:
            new_segment = self.canvas.create_rectangle(*prev_coords[-1], fill="green")
            self.body.append(new_segment)
            self.should_grow = False

    def grow(self):
        """Request a new segment to be added after the next move."""
        self.should_grow = True

    def get_overlapping_shapes(self):
        return self.canvas.find_overlapping(
            self.x, self.y,
            self.x + self.size,
            self.y + self.size
        )

    def check_self_collision(self):
        head_coords = self.canvas.coords(self.body[0])
        for segment in self.body[1:]:
            if self.canvas.coords(segment) == head_coords:
                return True
        return False
