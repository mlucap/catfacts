import discord
import json
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors, has_permissions

class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        """Change the servers prefix. Note: Only server admins can use this command."""
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to `{prefix}`')

def setup(client):
    client.add_cog(Prefix(client))