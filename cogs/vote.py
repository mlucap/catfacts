import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def vote(self, ctx):
        """Vote for the bot on top.gg"""
        await ctx.send("This will return a link once the bot is approved on top.gg")
        

def setup(client):
    client.add_cog(Vote(client))
