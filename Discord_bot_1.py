#
# Example of simple discord chatbot based on discord.py library
# For article (Russian language): http://tetraquark.ru/archives/377

import discord
import asyncio
import requests
from discord.ext import commands

TOKEN = 'NjMxOTMwNzAzNTU0MTUwNDE4.XZ-Bjg.RmT9v7iKBgfrEl5HAiF6uwsPvnE'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
		
@client.command(pass_context=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f"Сообщения удалены {amount}")

client.run(TOKEN)