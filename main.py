import discord
from discord.ext import commands
import random

from dotenv import load_dotenv
import os

# load the variables and token
load_dotenv()
token = os.getenv("TOKEN")

# This example requires the 'members' and 'message_content' privileged intents to function.


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
#intents.members = True
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        await message.channel.send(message.content[1:])

client.run(token)