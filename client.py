import discord
import os, os.path # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()
cogs_list = [
    'ping'
]
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN')) # run the bot with the token