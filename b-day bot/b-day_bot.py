# bot.py
import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import random
import sqlite3
from date_checker import Check_date

db = sqlite3.connect("Birthdays.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Dates(
user_id integer PRIMARY KEY,
date text NOT NULL);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Servers(
id integer PRIMARY KEY,
server_id integer NOT NULL,
user_id integer NOT NULL,
FOREIGN KEY (user_id)
REFERENCES Dates (user_id));""")
db.close()

load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents(messages = True, guilds = True)
intents.members = True
client = commands.Bot(command_prefix = ">", intents = intents)

def id_creator():
    db = sqlite3.connect("Birthdays.db")
    cursor = db.cursor()
    
    cursor.execute("SELECT Servers.id FROM Servers")
    count = 1
    prev = 0
    for x in cursor.fetchall():
        current = x[0]
        if current - prev != 1:
            count = prev + 1
            break
        count += 1
        prev = current
    db.commit()
    print(count)
    db.close()
    return count

def check_setup(date):
    check = Check_date(date)
    print(check.check_format())
    print(check.check_day())
    print(check.check_month())
    print(check.check_year())
    print(check.check_valid())
    valid = check.check_valid()
    return valid

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def add(ctx, date = None):
    db = sqlite3.connect("Birthdays.db")
    cursor = db.cursor()
    
    valid = check_setup(date)
    if valid == False:
        await ctx.send("Please enter a date in the format: £add [dd/mm/yyyy]")
    
    user_id = ctx.author.id
    server_id = ctx.message.guild.id
    aid = id_creator() 
    a_in_db = True
    
    cursor.execute("""SELECT Servers.server_id, Servers.user_id
                    FROM Servers WHERE Servers.server_id = ? AND
                    Servers.user_id = ?""", [server_id, user_id])
    db.commit()
    if len(cursor.fetchall()) == 0 and valid == True:
        a_in_db = False
        cursor.execute("""INSERT INTO Servers(id, server_id, user_id)
                        VALUES(?, ?, ?)""",(aid, server_id, user_id))
        db.commit()
        cursor.execute("""SELECT * FROM Dates WHERE Dates.user_id = ?""",
                       [user_id])
        if len(cursor.fetchall()) == 0:
            cursor.execute("""INSERT INTO Dates(user_id, date)
                            VALUES(?, ?)""",(user_id, date))
            db.commit()
            await ctx.send("Birthday added to database.")
        else:
            await ctx.send("Birthday added to this server.")
            
    if a_in_db == True and valid == True:
        db.commit()
        await ctx.send("Birthday already in database.")
    db.close()
    
@client.command()
async def update(ctx, date = None):
    db = sqlite3.connect("Birthdays.db")
    cursor = db.cursor()
    
    valid = check_setup(date)
    if valid == False:
        await ctx.send("Please enter a date in the format: £update [dd/mm/yyyy]")

    in_db = False
    user_id = ctx.author.id

    cursor.execute("""UPDATE Dates SET date = ? WHERE Dates.user_id = ?""",
                   [date, user_id])
    await ctx.send("Updated :)")
    db.commit()
    db.close()

@client.command()
async def display(ctx):
    db = sqlite3.connect("Birthdays.db")
    cursor = db.cursor()

    server_id = ctx.message.guild.id

    cursor.execute("""SELECT Servers.user_id, Dates.date FROM Servers JOIN Dates ON Servers.user_id = Dates.user_id
                    WHERE Servers.server_id = ?""",
                   [server_id])
    results = cursor.fetchall()
    db.commit()
    for result in results:
        user_id = result[0]
        date = result[1]
        for member in client.get_all_members():
            if user_id == member.id:
                name = member.name
                if member.nick != None:
                    name = member.nick
                output = str(name) + ": " + str(date)
                await ctx.send(output)
    db.close()
client.run(TOKEN)
