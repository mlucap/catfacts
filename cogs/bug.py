import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Bug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bug(self, ctx):
        """Report bugs directly to the owner!"""
        embed = discord.Embed(title='Command coming soon', description='This command is currently being developed. Sorry for any issues that may be present. For a better result, check out the bots github https://github.com/mlucap/catfacts/', colour=discord.Color.red())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Bug(client))