# import the game class
from game import Game
from rich.console import Console

def main():
    game = Game()
    game.reset()
    console = Console()
    captured = 0
    game.count_captured(game.getBoard(), 0, 0, game.getBoard()[0][0])

    # input loop
    while True:
        game.print_board_emoji(game.getBoard())

        if captured > 0:
            console.print("captured", captured, style="bold green")
            console.print("Score", game.calculate_score_gain(captured), style="bold green")
            captured = 0

        console.print("""
        0 = Red
        1 = Green
        2 = Blue
        3 = Purple
        4 = Brown
        5 = Yellow
        """)

        # get input
        x = int(input("Change: "))
        game.flood_fill(game.getBoard(), 0, 0, game.getBoard()[0][0], x)
        captured = game.count_captured(game.getBoard(), 0, 0, x)


if __name__ == '__main__':
    main()