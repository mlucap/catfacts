import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Bug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bug(self, ctx, args):
        """Report bugs directly to the owner!"""
        coffii = await client.get_user_info('218795930294419456')
        embed = discord.Embed(title='Bug report!', description='Your bug report, along with your discord name, discriminator, and id were sent to the bot owner. He will look into your report and hopefully fix the issue soon!', colour=discord.Color.green())
        await ctx.send(embed=embed)
        await ctx.send_message(me, 'test')

def setup(client):
    client.add_cog(Bug(client))