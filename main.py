import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

#load token from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# set up intents
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def test(ctx):
    await ctx.send(f'Fuck you! {round(bot.latency * 1000)}ms')

bot.run(TOKEN)