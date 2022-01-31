import nextcord
import random
from data.db.db import *
import asyncio

async def Begging(interaction):
    try:
        begornot = random.randint(1,2)
        embed = nextcord.Embed(title="You are begging for some gold...")
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(random.randint(5,7))
        if begornot == 1:
            gold_given = random.randint(5,15)
            execute("SELECT gold FROM PlayerEconomy WHERE UserID = ?",interaction.user.id)
            player_gold = int(cur.fetchall()[0][0])
            player_gold+=gold_given
            execute("UPDATE PlayerEconomy SET Gold = ? WHERE UserID = ?", player_gold, interaction.user.id)
            embed = nextcord.Embed(title="You begged the townsfolk for some money",description=f"A kind folk gave you `{gold_given}` Gold!")
            await interaction.edit_original_message(embed=embed)
        else:
            embed = nextcord.Embed(title="You got nothing!", description="No one was kind enough to give you any gold :(")
            await interaction.edit_original_message(embed=embed)
        commit()
    except Exception as e:
        print(e)

async def Robbing(interaction):
    try:
        robsuccess = random.randint(1,5)
        embed = nextcord.Embed(title="You are trying to rob someone for gold...")
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(random.randint(5,10))
        if robsuccess == 1:
            gold_given = random.randint(20,30)
            execute("SELECT gold FROM PlayerEconomy WHERE UserID = ?",interaction.user.id)
            player_gold = int(cur.fetchall()[0][0])
            player_gold+=gold_given
            execute("UPDATE PlayerEconomy SET Gold = ? WHERE UserID = ?", player_gold, interaction.user.id)
            embed = nextcord.Embed(title=f"You managed to be very sneaky and robbed a poor townsfolk for `{gold_given}` Gold!")
            await interaction.edit_original_message(embed=embed)
        else:
            embed = nextcord.Embed(title="You got caught!", description="Maybe try another profession which actually yeilds profit?")
            await interaction.edit_original_message(embed=embed)
        commit()
    except Exception as e:
        print(e)

async def Fishing(interaction):
    try:
        fishsuccess = random.randint(1,10)
        embed = nextcord.Embed(title="You throw your line and patiently wait for a fish...")
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(random.randint(5,7))
        if fishsuccess == 1:
            gold_given = random.randint(30,50)
            execute("SELECT gold FROM PlayerEconomy WHERE UserID = ?",interaction.user.id)
            player_gold = int(cur.fetchall()[0][0])
            player_gold+=gold_given
            execute("UPDATE PlayerEconomy SET Gold = ? WHERE UserID = ?", player_gold, interaction.user.id)
            embed = nextcord.Embed(title=f"You managed to reel in a fish and sold it for `{gold_given}` Gold!")
            await interaction.edit_original_message(embed=embed)
        else:
            fail_list = ["You got nothing... Better luck next time!","You almost had it! But the fish was too strong...","Looks like the fish was very strong, your reel broke!"]
            embed = nextcord.Embed(title=random.choice(fail_list), description="Maybe you should try doing something else.")
            await interaction.edit_original_message(embed=embed)
        commit()
    except Exception as e:
        print(e)

async def CheckBalance(interaction):
    try:
        execute("SELECT Gold FROM PlayerEconomy WHERE UserID = ?", interaction.user.id)
        reply = cur.fetchall()
        gold = int(reply[0][0])
    
        # the embed
        embed = nextcord.Embed(title=f"**{interaction.user.display_name}'s Balance**", description=f" **Wallet:** {gold} Gold")
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        print(e)