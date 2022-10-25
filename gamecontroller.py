import asyncio
from gamestate import Game
from ui.embeds import GameBoard
from ui.buttons import GuessButton
from ui.modals import WordGuess

class GameController:
    def __init__(self, guess_length, max_guesses):
        self.game = Game(guess_length, max_guesses)
        
        # UI components
        self.ui_modal = WordGuess(self)
        self.ui_button = GuessButton(self)
        self.ui_embed = GameBoard(self)

    def return_embed(self):
        return self.ui_embed.embed

    async def send_ui_modal(self, interaction):
        await interaction.response.send_modal(self.ui_modal)

    async def update_gamestate(self, interaction, data):
        # await interaction.response.send_message(f"Word is: {guess}")
        guess = data[0]

        # update the backend gamestate
        try:
            self.game.make_guess(guess)
        except ValueError:
            await interaction.response.send_message("The game is over, try again in the next round")
            return

        # edit the ui embed in memory 
        self.ui_embed.update_embed(self.game.board)

        # edit the message and update the ui
        
        await interaction.message.edit(embed=self.return_embed())
        await interaction.response.send_message(f"{data[1]} has placed a guess!\nThe guessed word was: {guess}\nInteraction created at {data[2]}")
    
    async def ui_handler(self, interaction, button=False, embed=False, modal=False, data=None):
        if button:
            # do button things
            await self.send_ui_modal(interaction)
        elif modal:
            # do modal things
            await self.update_gamestate(interaction, data)
        elif embed:
            # do embed things
            pass