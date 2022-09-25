import discord

class GameBoard:
    def __init__(self, size=5):
        self.size = size
        self.board = [["⬜" for i in range(self.size)] for j in range(self.size)]
    
    def create_embed(self):
        board = "```" + "\n".join([" ".join(i) for i in self.board]) + "```"
        embed = discord.Embed(title="better Coordle")

        embed.add_field(name="Coordle board", value=board)
        return embed