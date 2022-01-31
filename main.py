import nextcord
from nextcord import Interaction
import json

# importing command files
from commands.Economy import *
from commands.AdminCommands import *
from data.db.db import *

with open ("configuration.json", "r") as config:
    data = json.load(config)
    token = data["BOT_TOKEN"]
    owner_id = data["OWNER_ID"]
    guild_id = data["GUILD_ID"]

bot = nextcord.Client()

async def PlayerSignUpChecker(userid):
    try:
        execute("SELECT Gold FROM PlayerEconomy WHERE UserID = ?",userid)
        reply=cur.fetchall()
        reply=reply[0][0]
        if(reply==0 or reply>=0):
            return "yes"
    except:
        return "no"

async def SignUpPlayer(userid):
    execute("INSERT INTO PlayerEconomy (UserID, Gold) VALUES (?, ?)", userid, 0)
    commit()

#### READY UP AND BOT EVENTS ####

@bot.event  
async def on_ready():
    build()
    print("-----------------------------------------")
    print(f"{bot.user} has connected to discord!")
    print(f"Guild ID - {guild_id}")
    print("-----------------------------------------")
    await bot.change_presence(status=nextcord.Status.online)
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name='https://github.com/WonkyPigs/Discord-Ticket-Bot'))

#### COMMANDS ####
    
@bot.slash_command(name="help", guild_ids=[guild_id], description="Need some help?")
async def help(interaction: Interaction):
    await interaction.response.send_message(f"Available commands - ```/balance\n/rob\n/beg\n/fish\n/takegold **ADMIN COMMAND**\n/givegold **ADMIN COMMAND**```")

@bot.slash_command(name="balance", guild_ids=[guild_id], description="Check your balance")
async def balance(interaction: Interaction):
    if await PlayerSignUpChecker(interaction.user.id) == "no":
        await SignUpPlayer(interaction.user.id)
    await CheckBalance(interaction)

@bot.slash_command(name="beg", guild_ids=[guild_id], description="Beg the townsfolk for gold")
async def beg(interaction: Interaction):
    if await PlayerSignUpChecker(interaction.user.id) == "no":
        await SignUpPlayer(interaction.user.id)
    await Begging(interaction)

@bot.slash_command(name="rob", guild_ids=[guild_id], description="Rob the innocent townsfolk for gold")
async def rob(interaction: Interaction):
    if await PlayerSignUpChecker(interaction.user.id) == "no":
        await SignUpPlayer(interaction.user.id)
    await Robbing(interaction)

@bot.slash_command(name="fish", guild_ids=[guild_id], description="Do some fishing and chill!")
async def fish(interaction: Interaction):
    if await PlayerSignUpChecker(interaction.user.id) == "no":
        await SignUpPlayer(interaction.user.id)
    await Fishing(interaction)

@bot.slash_command(name="givegold", guild_ids=[guild_id], description="Give a specific amount of gold to a user, owner only")
async def givegold(interaction: Interaction, user: nextcord.Member, amount: int):
    user = int(user.id)
    if await PlayerSignUpChecker(user) == "no":
        await SignUpPlayer(user)
    await GivePlayerGold(interaction,user,amount, owner_id)

@bot.slash_command(name="takegold", guild_ids=[guild_id], description="Take a specific amount of gold from a user, owner only")
async def takegold(interaction: Interaction, user: nextcord.Member, amount: int):
    user = int(user.id)
    if await PlayerSignUpChecker(user) == "no":
        await SignUpPlayer(user)
    await TakePlayerGold(interaction,user,amount, owner_id)

#### MAKE THE BOT COME TO LIFE ####
bot.run(token)