import discord
from discord.ext import commands
import random
import os

description = " Робот который может что делать"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
@bot.event
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
print('------')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def Glbot(ctx):
    await ctx.send(f'Я бот который выплняет команды')
@bot.command()
async def Glcomads(ctx):
    await ctx.send(f' Мои команды:?Globaltempkr ?Globaltempthen ?Globaltempresson и ?Globaltempimg !')
@bot.command()
async def Globaltempkr(ctx):
    await ctx.send(f'Глобальное потепление — долгосрочное повышение средней температуры климатической системы Земли, происходящее уже более века')
@bot.command()
async def Globaltempthen(ctx):
    await ctx.send(f' Основная причина глобального потепления — деятельность человека. Люди сжигают ископаемое топливо (уголь, нефть, газ), в результате чего в атмосферу выбрасываются газы — углекислый газ, метан, оксид азота, фторированные газы. Они ведут к возникновению парникового эффекта, потому что способны поглощать много солнечного тепла. ')

@bot.command()
async def Globaltempresson(ctx):
    await ctx.send(f' Последствия глобального потепления включают повышение уровня моря, региональные изменения осадков, более частые экстремальные погодные явления, такие как жара и расширение пустынь.')
@bot.command()
async def Globaltempimg(ctx):
  img_name = random.choice(os.listdir('images'))
  with open(f'images/{img_name}', 'rb') as f:
    picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
bot.run('')
