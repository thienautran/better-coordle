import discord

class WordGuess(discord.ui.Modal):
    def __init__(self, game_controller, title="Guess a word"):
        self.game_controller = game_controller

        super().__init__(title=title)
        self.text_input = self.add_item(discord.ui.TextInput(label="Enter a word", placeholder=f"Enter a {self.game_controller.guess_length} letter word: ", max_length=self.game_controller.guess_length, min_length=self.game_controller.guess_length))
    
    async def on_submit(self, interaction):
        word = self.text_input.children[0].value # first child is first element in the list which is the word
        if word.isalpha():
            user = interaction.user.name
            timestamp = interaction.created_at
            print(f"Interaction at {timestamp}")
            input_data = {"word": word, "user": user, "timestamp": timestamp}
            await self.game_controller.ui_handler(interaction, modal=True, data=input_data)
        else:
            invalid_input_msg = f"{word} is an invalid guess\nGuesses can only contain letters"
            await interaction.response.send_message(invalid_input_msg, ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"Error: {error}")