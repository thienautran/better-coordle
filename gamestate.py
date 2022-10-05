class Game:
    def __init__(self, guess_length, max_guesses):
        # self.answer = answer
        self.max_guesses = max_guesses
        self.guess_length = guess_length
        
        # board is initialised as all None for columns and max_guesses rows
        self.board = [None for row in range(self.max_guesses)]
        self.finished = False
        self.current_guess = 0

    def make_guess(self, guess):
        if self.current_guess + 1 > self.max_guesses:
         raise ValueError("Game is over")

        self.board[self.current_guess] = guess
        self.current_guess += 1




class Guess:
    def __init__(self, word, user, timestamp):
        self.word = word
        self.user = user
        self.timestamp = timestamp
        self.points = 0

class Word:
    def __init__(self, ):
        pass