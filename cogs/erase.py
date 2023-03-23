import discord
from discord.ext import commands
import time
import asyncio
from randomuser import RandomUser
import random

class eraseCog(commands.Cog, name="erase command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name="erase", description="Does something...")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def erase(self, ctx,*, text):
		chars_list = list(text.lower())
		message = await ctx.respond(text.lower(), mention_author=False)
		for i in range(1,15):
			await asyncio.sleep(1)
			f = random.choices(chars_list, k=len(text.lower()))
			ff = str(f).replace('[','')
			ff = str(ff).replace("'",'')
			ff = str(ff).replace("]", '')
			ff = str(ff).replace(",", '')
			ff = str(ff).replace(" ", '')
			await message.edit(content=ff)


def setup(bot:commands.Bot):
	bot.add_cog(eraseCog(bot))