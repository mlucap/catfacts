import discord
from discord.ext import commands


class Bug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bug(self, ctx):
        """Report bugs directly to the owner!"""
        user = self.client.get_user(218795930294419456)
        embed = discord.Embed(title='Bug report!', description='Your bug report, along with your discord name, discriminator, and id were sent to the bot owner. He will look into your report and hopefully fix the issue soon!', colour=discord.Color.green())
        if user is not None:
            await user.send(f'{ctx.message.content} | User: {ctx.message.author} ID: {ctx.message.author.id}')
            await ctx.send(embed=embed)
        else:
            await ctx.send('Unable to send request.')


def setup(client):
    client.add_cog(Bug(client))