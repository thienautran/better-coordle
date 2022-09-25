import discord

class WordGuess(discord.ui.Modal, title="Word guess"):
    word = discord.ui.TextInput(label="Enter the word", placeholder="Enter a word: ")

    async def on_submit(self, interaction):
        await interaction.response.send_message(f"Your word was `{self.word.value}` uwu")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
