import discord
import ui.modals as modals

class GuessButton(discord.ui.View):
    def __init__(self, game_controller):
        self.game_controller = game_controller
        super().__init__()

    @discord.ui.button(label='Make guess', style=discord.ButtonStyle.green)
    async def make_guess(self, interaction, button):
        await self.game_controller.ui_handler(interaction, button=True)