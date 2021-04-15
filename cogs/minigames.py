import discord
from discord.ext import commands
import random

flip = ['heads', 'tails']

class minigames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='coin flip', aliases=['coin', 'cf', 'coinflip'])
    async def coin_flip(self, ctx):
        await ctx.send(f'The coin landed on ***{random.choice(flip)}*** !')

def setup(bot):
    bot.add_cog(minigames(bot))