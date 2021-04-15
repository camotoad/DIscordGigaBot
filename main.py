import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import os

bot = commands.Bot(command_prefix='!')
token = os.environ.get('DISCORD_BOT_TOKEN')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Going a lot.'))
    print('GigaBot is ready.')

def load_cogs():
    for file_name in os.listdir('./cogs'):
        if file_name.endswith('.py'):
            bot.load_extension(f'cogs.{file_name[:-3]}')

@bot.command(name='reload', hidden=True)
@has_permissions(administrator=True)
async def reload_cogs(ctx):
    try:
        for file_name in os.listdir('./cogs'):
            if file_name.endswith('.py'):
                bot.unload_extension(f'cogs.{file_name[:-3]}')
        load_cogs()
        await ctx.send('\N{OK HAND SIGN}')
    except:
        await ctx.send('Something went wrong.')

@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Required Argument.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('No such command is found.')
    elif isinstance(error, CheckFailure):
        await ctx.send("You don't have the permission to do that!")
    else:
        await ctx.send('Something went wrong.')

if __name__ == '__main__':
    load_cogs()
    bot.run(token)