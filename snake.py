class Snake:
    def __init__(self, stdscr):
        self.body = [(10, 10), (10, 9), (10, 8)]
        self.direction = 'RIGHT'
        self.stdscr = stdscr

    def move(self):
        # Logic for moving the snake based on the current direction
        pass

    def change_direction(self, new_direction):
        self.direction = new_direction

    def grow(self):
        # Logic for growing the snake's body
        pass
