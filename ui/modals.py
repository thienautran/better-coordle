import discord

class WordGuess(discord.ui.Modal):
    def __init__(self, game_controller, title="Guess a word"):
        self.game_controller = game_controller

        super().__init__(title=title)
        self.word = self.add_item(discord.ui.TextInput(label="Enter the word", placeholder="Enter a word: "))
    
    async def on_submit(self, interaction):
        word = self.word.children[0].value # first child is first element in the list which is the word
        await self.game_controller.ui_handler(interaction, modal=True, data=word)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"Error: {error}")