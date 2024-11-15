from game import RPS
from player import Player, RandomPlayer, HumanPlayer

def simulate(player1, player2):
    game = RPS(player1, player2)
    game.play_game()

if __name__ == '__main__':
    player1 = HumanPlayer()
    player2 = HumanPlayer()
    simulate(player1, player2)