import discord, os, time, asyncio, re
from discord.ext import commands

import alert


BOT_PREFIX = os.environ['prefix']
TOKEN = os.environ['token']

bot = commands.Bot(command_prefix=BOT_PREFIX)

alerts = []

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

@bot.command(name="setalert")
async def set_alert(ctx, name="", hours=0, mins=0, secs=0):
    #await ctx.message.channel.send("alerted")
    #pattern = re.compile(r'')
    #match = pattern.finditer(time)
    if(name == ""):
        await ctx.message.channel.send("Must input a name for the alert")
        return

    if(hours == 0 and mins == 0 and secs == 0):
        await ctx.message.channel.send("Must input hours, minutes, and seconds")
        return
    
    secs = (hours * 60 * 60) + (mins * 60) + secs

    new_alert = alert.Alert(ctx.message.guild, name, secs)
    alerts.append(new_alert)
    print(new_alert, alerts)
    print("{} hours, {} mins, {} secs".format(hours, mins, secs))
    await ctx.message.channel.send(":white_check_mark: Alert {} successfully registered.".format(name))




bot.run(TOKEN)
