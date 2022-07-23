import discord
from discord.ext import commands
from webserver import keep_alive
import os

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!')


#hello
@client.command()
async def hello(ctx):
    await ctx.send(f'{ctx.message.author.mention}: привет')


'''
@
async def on_member_join(member):
    channel = get(member.guild.channels, id=870695644438859779)
    await channel.send(f'{member} welcome')
'''
'''
@client.event
async def on_member_join(member):
    channel = client.get_channel(870695644438859779)
    embed = discord.Embed(title="Welcome!",
                          description=f"{member.mention} Just Joined")
    await channel.send(embed=embed)
'''

keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
