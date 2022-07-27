import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from webserver import keep_alive
import os

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
#----------
client = commands.Bot(command_prefix='!')
#-------------
comand = ('')

#--------------

#hello
@client.command()
async def hello(ctx):
    await ctx.send(
        f'{ctx.message.author.mention}: jello'
    )
#-----

@client.command()
async def helpi(ctx):
    await ctx.send(hel)
#-----------

@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_id=870695644438859779)
    embed = discord.Embed(
        title=f"Welcome {member.name}",
        description=f"Thanks for joining {member.guild.name}!")  # F-Strings!
    embed.set_thumbnail(
        url=member.avatar_url
    )  # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
