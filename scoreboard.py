class Scoreboard:
    def __init__(self, stdscr):
        self.score = 0
        self.high_score = 0  # This could be loaded from a file
        self.stdscr = stdscr

    def update_score(self, points):
        self.score += points

    def display_score(self):
        # Logic for displaying the current score and high score
        pass
