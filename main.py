import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('GigaBot is ready.')


token = os.environ.get('DISCORDBOT_TOKEN')


if __name__ == '__main__':
    client.run(token)