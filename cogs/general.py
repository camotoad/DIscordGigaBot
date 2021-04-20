import discord
from discord.ext import commands
from discord import Member


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='profile picture', aliases=['pfp'])
    async def retrieve_profile_pic(self, ctx, *, member: Member = None):
        if not member:
            member = ctx.author
        pfp = member.avatar_url
        embed = discord.Embed(
            title=member.display_name,
            description='Profile picture'
        )
        embed.set_image(url=pfp)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(general(bot))