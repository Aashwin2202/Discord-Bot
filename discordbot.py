import os
from dotenv import load_dotenv
import random

import discord
intents = discord.Intents.default()
intents.members = True

from discord.ext import commands
bot = commands.Bot(command_prefix='!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    welcome_messages = [(f'Aao {member.name}. Kya haal chaal?'),(f'{member.name}, aapki hi deri thi bs!'),(f'Swagat h aapka, {member.name}')]
    await member.create_dm()
    await member.dm_channel.send(random.choice(welcome_messages))

client.run(TOKEN)