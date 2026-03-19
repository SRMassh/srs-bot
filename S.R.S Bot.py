import os
from dotenv import load_dotenv

load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN') 

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True  
intents.message_content = True 


bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logado como {bot.user}')

#cmd

@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def reset(ctx):
    count = 0

    for member in ctx.guild.members:
        try:
            if member.nick is not None:
                await member.edit(nick=None)
                count += 1
        except discord.Forbidden:
            continue
        except discord.HTTPException:
            continue
            
    await ctx.send(f"✅ Resetados {count} apelidos com sucesso!")


bot.run(TOKEN)