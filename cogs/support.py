import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['money', 'donate'])
    async def support(self, ctx):
        """Ways to support my project!"""
        embed = discord.Embed(title='Command coming soon', description='I really appreciate the fact you are wanting to support my financially! Unfortunetely I do not have any practical ways of accepting payments of any kind so hold tight and the best way to support this project will be adding your ideas to the `>github` page or upvoting the bot on top.gg', colour=discord.Color.red())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Support(client))