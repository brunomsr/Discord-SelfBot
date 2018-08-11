import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
   print(client.user.name)
   print(client.user.id)
   print('Bot Online')

@client.event
async def on_message(message):
   if message.content.startswith('!test'):
       await client.send_message(message.channel, 'Bot testado!')

#client.run('token')
#client.run('email','senha')