import discord

class GameBoard:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        
        # save the board dimentions from game
        self.board_x = self.game_controller.game.guess_length
        self.board_y = self.game_controller.game.max_guesses
        
        # create the embed
        self.embed = discord.Embed(title="Better Coordle")
        
        # initial state is a board_x * board_y 2d array of blank letters
        # needs to be converted to string for embed
        board_initial_state = "\n".join(["⬜" * self.board_x for row in range(self.board_y)])
        
        # populates the embed with initial state
        self.embed.add_field(name="Guesses", value=board_initial_state)

    def update_embed(self, board):
        self.embed.remove_field(0)
        new_ui_board = "\n".join([guess if guess != None else "⬜" * self.board_x for guess in board])
        self.embed.add_field(name="Guesses", value=new_ui_board)