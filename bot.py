import discord
from discord.ext import commands
import firebase

TOKEN = "InputYourTokenHere"

client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def hello(ctx):
	await ctx.channel.send("Heyaa!")

client.load_extension('cogs.music')

client.run(TOKEN)
