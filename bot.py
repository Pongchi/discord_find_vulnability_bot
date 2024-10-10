import os # default module
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv() # load all the variables from the env file

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="제목",color=discord.Color.gold())
    embed.add_field(name="하위요소1",value="값1",inline=True)
    embed.add_field(name="하위요소2",value="값2",inline=True)
    embed.add_field(name="하위요소3",value="값3",inline=False)
    embed.set_thumbnail(url=ctx.author.avatar)
    embed.set_footer(text="글아래")
    await ctx.send(embed=embed)

bot.run(os.getenv('TOKEN'))