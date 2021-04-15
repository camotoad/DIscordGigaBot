import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')
token = os.environ.get('DISCORD_BOT_TOKEN')

@bot.event
async def on_ready():
    print('GigaBot is ready.')

def load_cogs():
    for file_name in os.listdir('./cogs'):
        if file_name.endswith('.py'):
            bot.load_extension(f'cogs.{file_name[:-3]}')

@bot.command(aliases=['reload'])
async def _reload_cogs(ctx):
    if bot.is_owner(ctx.author):
        try:
            for file_name in os.listdir('./cogs'):
                if file_name.endswith('.py'):
                    bot.unload_extension(f'cogs.{file_name[:-3]}')
            load_cogs()
            await ctx.send('\N{OK HAND SIGN}')
        except:
            await ctx.send('Something went wrong.')
    else:
        await ctx.send('You are not authorized')

if __name__ == '__main__':
    load_cogs()
    bot.run(token)