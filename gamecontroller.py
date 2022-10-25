import asyncio
from gamestate import Game
from ui.embeds import GameBoard
from ui.buttons import GuessButton
from ui.modals import WordGuess

class GameController:
    def __init__(self, guess_length, max_guesses):
        self.guess_length = guess_length
        self.max_guesses = max_guesses
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
        # update the backend gamestate
        try:
            self.game.add_guess(data)
        except ValueError:
            await interaction.response.send_message("The game is over, try again in the next round")
            return

        # no errors were raised so continue

        # edit the ui embed in memory 
        self.ui_embed.update_embed(self.game.board)

        # send the payload game data to ui
        await interaction.response.edit_message(embed=self.return_embed())

    async def ui_handler(self, interaction, button=False, embed=False, modal=False, data=None):
        if button:
            # do button things
            await self.send_ui_modal(interaction)
        elif modal:
            # do modal things
            await self.update_gamestate(interaction, data)
        return