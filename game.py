import numpy as np

class RPS:

    def __init__(self, player1, player2):
        self.moves = {0, 1, 2}
        self.p1 = player1
        self.p2 = player2

    def play_game(self):
        p1_move = self.p1.play()
        p2_move = self.p2.play()
        print('Player 1 chose', str(self.decode(p1_move)))
        print('Player 2 chose', str(self.decode(p2_move)))
        print('The result is: ')
        if p1_move == p2_move:
            print('Tie!')
        elif (p1_move - p2_move) == 1 or (p1_move - p2_move) == -2:
            print('Player 1 wins!')
            self.p1.scoreself()
        else:
            print('Player 2 wins!')
            self.p2.scoreself()

    def decode(self, move):
        if move == 0:
            return 'rock'
        elif move == 1:
            return 'paper'
        elif move == 2:
            return 'scissors'
        else:
            return 'Invalid move'
        
    def test(self):
      pass