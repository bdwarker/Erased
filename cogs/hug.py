import discord
from discord.ext import commands
import time
import os
from PIL import Image, ImageFont, ImageDraw , ImageFilter
img = Image.open("Cogs/image/hug.jpg")
class HugCog(commands.Cog, name="hug command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name="hug", description="Hug a mentioned user.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def hug(self, ctx, member:discord.Member):
			im1 = Image.open("cogs/image/hug.jpg")
			await ctx.author.avatar.url.save(f'{ctx.author.id}avh.jpg')
			await member.avatar.url.save(f'{member.id}avh.jpg')
			im2 = Image.open(f'{ctx.author.id}avh.jpg')
			im3 = Image.open(f'{member.id}avh.jpg')
			newsize = (100, 100)
			im2 = im2.resize(newsize)
			ns2 = (100, 100)
			im3 = im3.resize(ns2)
			im1.paste(im3, (200, 100))
			im1.paste(im2, (300, 30))
			im1.save(f'{ctx.author.id}{member.id}.jpg', quality=95)
			await ctx.respond(file=discord.File(f'{ctx.author.id}{member.id}.jpg'), mention_author=False)
			os.remove(f'{ctx.author.id}{member.id}.jpg')
			os.remove(f'{ctx.author.id}avh.jpg')
			os.remove(f'{member.id}avh.jpg')

def setup(bot:commands.Bot):
	bot.add_cog(HugCog(bot))