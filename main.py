import discord
import random
import os
from discord.ext import commands
from dotenv import load_dotenv

# we might have to remove this and replace this with a database soon
GACHA_POOL = {
    "1Star": ["Basic Jethro", "Basic Jesh", "Basic David"],
    "2Star": ["Chris Gym Pic", "Blurry Eman Pic"],
    "3Star": ["Jesh Gym Pic", "Joseph Tiktok"],
    "4Star": ["Laboratory Jesh", "Alpha Joseph"]
}

RARITIES = ["1Star", "2Star", "3Star", "4Star"]
WEIGHTS = [0.7, 0.2, 0.08, 0.02]

#load token from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# set up intents
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

#this just shows in the console
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

#test command
@bot.command()
async def test(ctx):
    await ctx.send(f'Fuck you! {round(bot.latency * 1000)}ms')

#pull command
@bot.command()
async def pull(ctx):
    selected_rarity = random.choices(RARITIES, weights=WEIGHTS, k=1)[0]
    item = random.choice(GACHA_POOL[selected_rarity])
    
    await ctx.send(f'You pulled a {selected_rarity} item: {item} {round(bot.latency * 1000)}ms')
    

bot.run(TOKEN)