import curses
from game import Game

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    game = Game(stdscr)
    game.start_game()

if __name__ == "__main__":
    curses.wrapper(main)
