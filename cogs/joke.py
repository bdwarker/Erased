import dependencies.joke as joke
import discord
from discord.ext import commands
import time


class JokeCog(commands.Cog, name="joke command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name="joke", description="Tells a random joke.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def joke(self, ctx):
            jokes = joke.get_joke()
            await ctx.respond(jokes['joke'], mention_author=False)

def setup(bot:commands.Bot):
	bot.add_cog(JokeCog(bot))