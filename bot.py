import discord, os, time, asyncio
from discord.ext import commands


BOT_PREFIX = '>'
TOKEN = os.environ['token']

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print('discord version:')
    print(discord.__version__)
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    servers = list(bot.guilds)
    print('Connected on '+ str(len(servers)) + ' servers:')
    print('\n'.join('>'+ server.name for server in servers))
    print('------')

@bot.command(name="alert")
async def alert(ctx):
    await ctx.message.channel.send("alerted")


bot.run(TOKEN)
