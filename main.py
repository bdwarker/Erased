import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file
# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]

	owner_id = data["owner_id"]
class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
intents.members = True
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	message = ""
	for guild in bot.guilds:
		message += f"{guild.name}\n"
	print(message)
	print(f"We have logged in as {bot.user}")
	print(discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name =f"/help"))


# @bot.event
# async def on_message(message):
# 	bot_Ping = f"<@!{bot.user.id}>"
# 	if message.author.bot:
# 		return
# 	elif f"{bot_Ping}" in message.content.lower():
# 		msg = message.content
# 		clear_Ping = msg.replace(f"{bot_Ping}", '')
# 		import requests
# 		url = "https://random-stuff-api.p.rapidapi.com/ai"
# 		querystring = {"msg":f"{clear_Ping}","bot_name":"Erased","bot_gender":"bot","bot_master":"Unerasable#3892"}
# 		headers = {
# 				'authorization': "aShRHeuJXtaW",
# 				'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
# 				'x-rapidapi-key': "890e94f353msh6e856d5b37337c2p10e6fajsn8d839c08439f"
# 				}
# 		response = requests.request("GET", url, headers=headers, params=querystring)

# 		await message.reply(response["AIResponse"].text)
# 	await bot.process_commands(message)
bot.run(os.getenv('TOKEN'))