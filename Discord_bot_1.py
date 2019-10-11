#
# Example of simple discord chatbot based on discord.py library
# For article (Russian language): http://tetraquark.ru/archives/377
#

import discord
import asyncio
import requests
from discord.ext import commands

TOKEN = 'token'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
	await ctx.channel.purge(limit=amount + 1)
	await ctx.send(f"Сообщений удалено: {amount}")

client.run(TOKEN)
