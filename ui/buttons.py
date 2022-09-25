import discord
import ui.modals as modals

class GuessButton(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Make guess', style=discord.ButtonStyle.green)
    async def make_guess(self, interaction, button):
            await interaction.response.send_modal(modals.WordGuess())
            # await interaction.response.send_message("clicked")
