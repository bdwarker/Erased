import discord
from discord.ext import commands
import time
import os
from PIL import Image, ImageFont, ImageDraw , ImageFilter
img = Image.open("cogs/image/ntg.jpg")
class KissCog(commands.Cog, name="kiss command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name="kiss", description="Hmmmm...")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def kiss(self, ctx, member:discord.Member):
			im1 = Image.open("cogs/image/ntg.jpg")
			await ctx.author.avatar.url.save(f'{ctx.author.id}avk.jpg')
			await member.avatar.url.save(f'{member.id}avk.jpg')
			im2 = Image.open(f'{ctx.author.id}avk.jpg')
			im3 = Image.open(f'{member.id}avk.jpg')
			newsize = (100, 100)
			im2 = im2.resize(newsize)
			ns2 = (100, 100)
			im3 = im3.resize(ns2)
			im1.paste(im2, (350, 100))
			im1.paste(im3, (50, 150))
			im1.save(f'{ctx.author.id}{member.id}.jpg', quality=95)
			await ctx.respond(file=discord.File(f'{ctx.author.id}{member.id}.jpg'), mention_author=False)
			os.remove(f'{ctx.author.id}{member.id}.jpg')
			os.remove(f'{ctx.author.id}avk.jpg')
			os.remove(f'{member.id}avk.jpg')

def setup(bot:commands.Bot):
	bot.add_cog(KissCog(bot))