class Food:
    def __init__(self, stdscr):
        self.position = (5, 5)  # Initial food position
        self.stdscr = stdscr

    def display(self):
        self.stdscr.addstr(self.position[0], self.position[1], '*')

    def relocate(self):
        # Logic for relocating the food
        pass
