import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        admin_check = ctx.author.guild_permissions.administrator
        return admin_check

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

    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'{extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'{extension}')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('Nice Test\N{OK HAND SIGN}')

    @clear.error
    @test.error
    @kick.error
    @ban.error
    @unban.error
    @load.error
    @unload.error
    async def error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send(f'It looks like you do not have the permission.')


def setup(bot):
    bot.add_cog(Admin(bot))