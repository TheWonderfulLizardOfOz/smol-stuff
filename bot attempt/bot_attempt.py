# bot.py
import os
#import discord
#from discord.ext import tasks, commands
from discord.ext import commands
from dotenv import load_dotenv
import random
import time

load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")
saysomething_msg = ["I AM GOD", "This bot makes me feel very powerful",
                    "This is fun we are having fun", ":)", "Nah", "No",
                    "Nope", "Ok", "MEEP MORP I AM A ROBOT",
                    "If this works Garance will be very happy",
                    "I'm sorry I have nothing to say right now please come back now",
                    "I WILL NOT DO AS YOU COMMAND"]

client = commands.Bot(command_prefix = "%")
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.command()
async def saysomething(ctx):
    await ctx.send(saysomething_msg[random.randint(0, len(saysomething_msg) - 1)])
    
@client.command()
async def roll(ctx, arg1, arg2 = 0):
    try:
        if int(arg1) > int(arg2):
            num = str(random.randint(int(arg2), int(arg1)))
            await ctx.send(num)
        else:
            num = str(random.randint(int(arg1), int(arg2)))
            await ctx.send(num) 
    except ValueError:
        await ctx.send("Please only give me only numbers.")

@client.command()
async def hello(ctx):
    await ctx.send("Hello {}!".format(ctx.message.author.mention))

@client.command()
async def party(ctx, arg):
    try:
        if int(arg) <= 0:
            await ctx.send("Bruh")
        else:    
            for i in range(int(arg)):
                await ctx.send(":confetti_ball: IT'S PARTY TIME :confetti_ball:")
    except ValueError:
        await ctx.send("Integers!")

@client.command()
async def pain(ctx):
    while True:
        time.sleep(15)
        await ctx.send("15 seconds have passed")
client.run(TOKEN)
