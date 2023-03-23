from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner
import time


class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		if isinstance(error, commands.CommandOnCooldown):
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				await ctx.respond('This command has a cooldown, for '+str(day)+ " day(s)", mention_author=False)
			elif hour > 0:
				await ctx.respond('This command has a cooldown, for '+str(hour)+ " hour(s)", mention_author=False)
			elif minute > 0:
				await ctx.respond('This command has a cooldown, for '+ str(minute)+" minute(s)", mention_author=False)
			else:
				await ctx.respond(f'This command has a cooldown, for {error.retry_after:.2f} second(s)', mention_author=False)
		elif isinstance(error, CommandNotFound):
			return
		elif isinstance(error, MissingPermissions):
			await ctx.respond(error)
		elif isinstance(error, CheckFailure):
			await ctx.respond(error)
		elif isinstance(error, NotOwner):
			await ctx.respond(error)
		else:
			print(error) 

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))
