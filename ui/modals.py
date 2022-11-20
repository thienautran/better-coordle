import discord

class WordGuess(discord.ui.Modal):
    def __init__(self, game_controller, title="Guess a word"):
        self.game_controller = game_controller

        super().__init__(title=title)
        self.text_input = self.add_item(discord.ui.TextInput(label="Enter a word", placeholder=f"Enter a {self.game_controller.guess_length} letter word: ", max_length=self.game_controller.guess_length, min_length=self.game_controller.guess_length))
    
    async def on_submit(self, interaction):
        word = self.text_input.children[0].value # first child is first element in the list which is the word

        user = interaction.user.name
        timestamp = interaction.created_at
        input_data = {"word": word, "user": user, "timestamp": timestamp}
        logging_msg = f"Interaction at {input_data['timestamp']} from user {input_data['user']}"
        print(logging_msg)

        await self.game_controller.ui_handler(interaction, modal=True, data=input_data)



    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"Error: {error}")