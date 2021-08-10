import os
import os

import discord
from discord.ext import commands
import storage123 as s

default_prefix = '$'
async def determine_prefix(bot, message):
    guild = message.guild
    #Only allow custom prefixs in guild
    if guild:
        return s.Handle(str(guild.id), "check", "prefix")
    else:
        return default_prefix

bot = commands.Bot(command_prefix=determine_prefix)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        if s.Handle(str(guild.id), "check", "creditAddMsg") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "creditAddMsg", "Attention citizen! ")
        if s.Handle(str(guild.id), "check", "creditRemoveMsg") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "creditRemoveMsg", "Attention citizen! ")
        if s.Handle(str(guild.id), "check", "creditAddMsg2") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "creditAddMsg2", " social points have been added to your account!")
        if s.Handle(str(guild.id), "check", "creditRemoveMsg2") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "creditRemoveMsg2", " social points have been deducted from your account!")
        if s.Handle(str(guild.id), "check", "prefix") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "prefix", "$")
        if s.Handle(str(guild.id), "check", "threshold1") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold1", 400)
        if s.Handle(str(guild.id), "check", "threshold2") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold2", 600)
        if s.Handle(str(guild.id), "check", "threshold3") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold3", 1200)
        if s.Handle(str(guild.id), "check", "threshold4") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold4", 1500)
        if s.Handle(str(guild.id), "check", "threshold1role") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold1role", "None")
        if s.Handle(str(guild.id), "check", "threshold12role") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold12role", "None")
        if s.Handle(str(guild.id), "check", "threshold23role") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold23role", "None")
        if s.Handle(str(guild.id), "check", "threshold34role") == "User doesnt exist in database":
            s.Handle(str(guild.id), "add", "threshold34role", "None")
        if s.Handle(str(guild.id), "check", "threshold4role") == "User doesnt exist in database":
             s.Handle(str(guild.id), "add", "threshold4role", "None")
        for member in guild.members:
            if s.Handle('.'.join((str(guild.id), str(member.id))), "check", "credit") == "User doesnt exist in database":
                s.Handle('.'.join((str(guild.id), str(member.id))), "add", "credit", 1000)

@bot.command(name="check")
async def check(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
    id = '.'.join((str(ctx.guild.id), str(member.id)))
    outl = s.Handle(id, "check", "credit")

    await ctx.send(outl)

@bot.command(name="add")
@commands.has_permissions(administrator=True)
async def add(ctx, member: discord.Member=None, amount: int=0):
    if member is None:
        await ctx.send("You're supposed to provide a user!")
        return
    id = '.'.join((str(ctx.guild.id), str(member.id)))
    s.Handle(id, "add", "credit", s.Handle(id, "check", "credit") + amount)
    outl = (s.Handle(str(ctx.guild.id), "check", "creditAddMsg") + str(amount) + s.Handle(str(ctx.guild.id), "check", "creditAddMsg2") + member.mention) if amount > 0 else (s.Handle(str(ctx.guild.id), "check", "creditRemoveMsg") + str(-amount) + s.Handle(str(ctx.guild.id), "check", "creditRemoveMsg2") + member.mention)

    await ctx.send(outl)

@bot.command(name="setprefix")
@commands.has_permissions(administrator=True)
async def setPrefix(ctx, prefix=None):
    if prefix == None:
        await ctx.send("You're supposed to provide a prefix!")
        return
    s.Handle(str(ctx.guild.id), "add", "prefix", prefix)
    
    await ctx.send("Prefix successfully changed to " + prefix)

@bot.command(name="setvariable")
@commands.has_permissions(administrator=True)
async def setVar(ctx, var=None, val=None):
    if var == None:
        await ctx.send("You're supposed to provide a variable!")
        return
    if val == None:
        await ctx.send("You're supposed to provide a value!")
        return
    s.Handle(str(ctx.guild.id), "add", var, val)

    await ctx.send("Variable \"" + var + "\" successfully changed to: " + val)

@bot.event
async def on_message(message):
    if s.Handle('.'.join((str(message.guild.id), str(message.author.id))), "check", "credit") <= s.Handle(str(message.guild.id), "check", "threshold1"):
        if s.Handle(str(message.guild.id), "check", "threshold1role") != "None":
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold1role")))) if (s.Handle(str(message.guild.id), "check", "threshold1role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold12role")))) if (s.Handle(str(message.guild.id), "check", "threshold12role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold23role")))) if (s.Handle(str(message.guild.id), "check", "threshold23role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold34role")))) if (s.Handle(str(message.guild.id), "check", "threshold34role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold4role")))) if (s.Handle(str(message.guild.id), "check", "threshold4role") != "None") else h()
            await message.author.add_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold1role"))))
    if s.Handle(str(message.guild.id), "check", "threshold1") < s.Handle('.'.join((str(message.guild.id), str(message.author.id))), "check", "credit") <= s.Handle(str(message.guild.id), "check", "threshold2"):
        if s.Handle(str(message.guild.id), "check", "threshold12role") != "None":
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold1role")))) if (s.Handle(str(message.guild.id), "check", "threshold1role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold12role")))) if (s.Handle(str(message.guild.id), "check", "threshold12role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold23role")))) if (s.Handle(str(message.guild.id), "check", "threshold23role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold34role")))) if (s.Handle(str(message.guild.id), "check", "threshold34role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold4role")))) if (s.Handle(str(message.guild.id), "check", "threshold4role") != "None") else h()
            await message.author.add_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold12role"))))
    if s.Handle(str(message.guild.id), "check", "threshold2") < s.Handle('.'.join((str(message.guild.id), str(message.author.id))), "check", "credit") <= s.Handle(str(message.guild.id), "check", "threshold3"):
        if s.Handle(str(message.guild.id), "check", "threshold23role") != "None":
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold1role")))) if (s.Handle(str(message.guild.id), "check", "threshold1role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold12role")))) if (s.Handle(str(message.guild.id), "check", "threshold12role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold23role")))) if (s.Handle(str(message.guild.id), "check", "threshold23role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold34role")))) if (s.Handle(str(message.guild.id), "check", "threshold34role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold4role")))) if (s.Handle(str(message.guild.id), "check", "threshold4role") != "None") else h()
            await message.author.add_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold23role"))))
    if s.Handle(str(message.guild.id), "check", "threshold3") < s.Handle('.'.join((str(message.guild.id), str(message.author.id))), "check", "credit") <= s.Handle(str(message.guild.id), "check", "threshold4"):
        if s.Handle(str(message.guild.id), "check", "threshold34role") != "None":
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold1role")))) if (s.Handle(str(message.guild.id), "check", "threshold1role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold12role")))) if (s.Handle(str(message.guild.id), "check", "threshold12role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold23role")))) if (s.Handle(str(message.guild.id), "check", "threshold23role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold34role")))) if (s.Handle(str(message.guild.id), "check", "threshold34role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold4role")))) if (s.Handle(str(message.guild.id), "check", "threshold4role") != "None") else h()
            await message.author.add_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold34role"))))
    if s.Handle(str(message.guild.id), "check", "threshold4") < s.Handle('.'.join((str(message.guild.id), str(message.author.id))), "check", "credit"):
        if s.Handle(str(message.guild.id), "check", "threshold4role") != "None":
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold1role")))) if (s.Handle(str(message.guild.id), "check", "threshold1role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold12role")))) if (s.Handle(str(message.guild.id), "check", "threshold12role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold23role")))) if (s.Handle(str(message.guild.id), "check", "threshold23role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold34role")))) if (s.Handle(str(message.guild.id), "check", "threshold34role") != "None") else h()
            await message.author.remove_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold4role")))) if (s.Handle(str(message.guild.id), "check", "threshold4role") != "None") else h()
            await message.author.add_roles(discord.utils.get(message.guild.roles, id = str(s.Handle(str(message.guild.id), "check", "threshold4role"))))

    await bot.process_commands(message)

async def h():
    return




# @bot.event
# async def on_error(event, *args, **kwargs): # supposed to save errors but compiler error
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise 


bot.run(os.environ['token12345'])