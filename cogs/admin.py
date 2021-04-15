import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}. Reason: {reason}')

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}. Reason: {reason}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_tag = member.split('#')

        for entry in banned_users:
            user = entry.user

            if (user.name, user.tag) == (member_name, member_tag):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.tag}')

    @commands.command(aliases=['cls'])
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)

def setup(bot):
    bot.add_cog(Admin(bot))