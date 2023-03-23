import discord
from discord.ext import commands
import time


class InviteCog(commands.Cog, name="invite command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name="invite", description="Sends a link for the bot invite.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def invite(self, ctx):
            await ctx.respond("Invite me! https://dsc.gg/erased", mention_author=False)

def setup(bot:commands.Bot):
	bot.add_cog(InviteCog(bot))