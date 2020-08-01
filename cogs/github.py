import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Github(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['git', 'support', 'issue'])
    async def github(self, ctx):
        """Official github page"""
        embed = discord.Embed(title='Github', description='The official catfacts github page. https://github.com/mlucap/catfacts', url='https://github.com/mlucap/catfacts', colour=discord.Color.blue())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Github(client))