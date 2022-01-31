from data.db.db import *

async def GivePlayerGold(interaction,arg1,arg2,owner_id):
    if interaction.user.id==owner_id:
        execute(f"SELECT Gold FROM PlayerEconomy WHERE UserID = ?",arg1)
        reply = cur.fetchall()
        Gold = reply[0][0]   
        Gold = int(Gold) + int(arg2)
        execute("UPDATE PlayerEconomy SET Gold = ? WHERE UserID = ?", Gold, arg1)
        commit()
        await interaction.response.send_message(f"Successfully given `{arg2}` Gold to <@{arg1}>")
    else:
        await interaction.response.send_message("No I dont think i will.")

async def TakePlayerGold(interaction,arg1,arg2,owner_id):
    if interaction.user.id==owner_id:
        execute(f"SELECT Gold FROM PlayerEconomy WHERE UserID = ?",arg1)
        reply = cur.fetchall()
        Gold = reply[0][0]   
        Gold = int(Gold) - int(arg2)
        execute("UPDATE PlayerEconomy SET Gold = ? WHERE UserID = ?", Gold, arg1)
        commit()
        await interaction.response.send_message(f"Successfully taken `{arg2}` Gold from <@{arg1}>")
    else:
        await interaction.response.send_message("No I dont think i will.")