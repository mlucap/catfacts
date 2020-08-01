import discord
import math
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Error(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title='Command on cooldown', description='Command is on cooldown, please wait {}s'.format(math.ceil(error.retry_after)), colour=discord.Color.red())
            await ctx.send(embed=embed)
            return
def setup(client):
    client.add_cog(Error(client))