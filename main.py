import os
import discord
import ui.embeds as embeds
import ui.buttons as buttons
import ui.modals as modals
from dotenv import load_dotenv
from discord.ext import commands

# load the variables and token
load_dotenv()
token = os.getenv("TOKEN")


class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or("!"), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

client = Client()


@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def guess(ctx):
    view = buttons.GuessButton()
    await ctx.send(view=view)

@client.command()
async def board(ctx):
    e = embeds.GameBoard(6)
    e = e.create_embed()
    v = buttons.GuessButton()
    await ctx.send(embed=e, view=v)


client.run(token)