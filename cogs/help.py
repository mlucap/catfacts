import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        """Shows this menu"""
        embed = discord.Embed(title="Help Menu", colour=discord.Color.green())
        embed.add_field(name="Catfact", value="Gives you a new, random catfact every command run!")
        embed.add_field(name="Changeprefix", value="Reserved for server admins only. Allows for admins to change the prefix for their server.")
        embed.add_field(name="Bug", value="Reports any bugs you may come across to the owner (Missue of this command may result in a blacklist from running commands.)")
        embed.add_field(name="Support", value="Provides you with different ways to support the project.")
        embed.add_field(name="Github", value="Provides you with the official github repository of this bot.")
        embed.add_field(name="Vote", value="DM's you the url to vote for the bot on top.gg. This is a great way to support the bot!")
        embed.add_field(name="Uptime", value="Shows how long the bot has been running since it's last restart.")
        embed.set_footer(text="The default prefix is 'cf>'. If you are ever unsure of the prefix, tagging the bot will tell you the current prefix")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))