import logging
import aiohttp
import discord
from discord.ext import commands


class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    logging.getLogger('asyncio').setLevel(logging.CRITICAL)

    @commands.command(aliases=['cf', 'cat'])
    async def catfact(self, ctx: commands.Context) -> None:
        """Gets a random cat fact."""

        await ctx.trigger_typing()
        async with aiohttp.ClientSession().get("https://catfact.ninja/fact") as response:
        
            fact = (await response.json())["fact"]
            length = (await response.json())["length"]
            embed = discord.Embed(title=f'Random cat fact number: **{length}**', description=f'{fact}', colour=0x400080)
            # await ctx.send(f'Random cat fact number {length}:\n{fact}')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Cat(client))