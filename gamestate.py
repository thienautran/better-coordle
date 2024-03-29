class Game:
    def __init__(self, guess_length, max_guesses):
        # self.answer = answer
        self.max_guesses = max_guesses
        self.guess_length = guess_length
        
        # board is initialised as all None for columns and max_guesses rows
        self.board = [None for row in range(self.max_guesses)]
        self.finished = False
        self.current_guess = 0

    def __validate_guess(self, guess):
        if self.current_guess + 1 > self.max_guesses:
            return False
        if not guess.isalpha():
            return False
        
        return True # when valid

    def add_guess(self, data):     
        if not self.__validate_guess(data["word"]):
            raise ValueError("Invalid guess")


        # create a guess object with data payload
        guess = Guess(data["word"], data["user"], data["timestamp"])

        # populate the board
        self.board[self.current_guess] = guess
        self.current_guess += 1 # move pointer


class Guess:
    def __init__(self, word, user, timestamp):
        self.word = word
        self.user = user
        self.timestamp = timestamp
        self.points = 0

class Word:
    def __init__(self, ):
        pass