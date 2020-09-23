import discord
import time
import os
import sys
import json
import datetime
import asyncio
from discord.ext import commands
sys.dont_write_bytecode = True


def get_prefix(message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Bot has logged in at {datetime.datetime.now().time()}\nLatency is {round(client.latency * 1000)}ms')
    while True:
        await client.change_presence(activity=discord.Game(name=f'200+ Random Cat Facts!'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f'Running in {len(client.guilds)} servers!'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f'Mention me if you need help!'))
        await asyncio.sleep(20)


@client.event
async def on_message(message):
    with open('prefixes.json', 'r') as f:
        data = json.load(f)
    if str(message.guild.id) in data:
        prefix = data[str(message.guild.id)]
    else:
        prefix = 'cf>'

    for x in message.mentions:
        if(x==client.user):
            msg = await message.channel.send(f'My prefix is `{prefix}`')

    await client.process_commands(message)    


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'cf>'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token = os.getenv('BOT_TOKEN')
client.run(token)
