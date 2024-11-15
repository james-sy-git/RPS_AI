import numpy as np

class Player:
    
    def __init__(self):
        self.score = 0

    def play(self):
        pass
    
    def scoreself(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
    
class RandomPlayer(Player):
    
    def __init__(self):
        super().__init__()
    
    def play(self):
        return np.random.randint(0, 3)
    
class HumanPlayer(Player):
    
    def __init__(self):
        super().__init__()
    
    def play(self):
        human_input = input('rock, paper, or scissors? ')
        if human_input == 'rock':
            return 0
        elif human_input == 'paper':
            return 1
        elif human_input == 'scissors':
            return 2
        else:
            print('Invalid input. Please try again.')
            return self.play()