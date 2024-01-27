import curses
from snake import Snake
from food import Food
from scoreboard import Scoreboard

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.snake = Snake(self.stdscr)
        self.food = Food(self.stdscr)
        self.scoreboard = Scoreboard(self.stdscr)
        self.game_over = False

    def start_game(self):
        while not self.game_over:
            self.game_loop()

    def game_loop(self):
        self.stdscr.clear()
        self.snake.move()
        self.food.display()
        self.scoreboard.display_score()
        self.stdscr.refresh()
        curses.napms(200)  # Game speed

    def end_game(self):
        self.game_over = True
