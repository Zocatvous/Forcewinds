import discord
import os
from dotenv import load_dotenv
DISCORD_TOKEN = 'elQPyzibhfODB5NoB4N5hxlTMuRxKGy-'
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_ready():
	print('{}'.format(clinet.user))


client.run(TOKEN)