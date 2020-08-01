import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['money', 'donate'])
    async def support(self, ctx):
        """Ways to support my project!"""
        embed = discord.Embed(title='Support Me!', description='If you\'d like to support the project, please just the github repository `>github` to find proper methods! If you are looking to make a financial donation you can do so by emailing me, again on the github repository.', colour=discord.Color.orange())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Support(client))