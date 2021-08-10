import os

import discord
from discord.ext import tasks, commands
import json

default_prefix = '$'
async def determine_prefix(bot, message):
    guild = message.guild
    #Only allow custom prefixs in guild
    if guild:
        return bot.prefix
    else:
        return default_prefix

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=determine_prefix, intents=discord.Intents.all())

bot.creditAddMsg = "Attention citizen! "
bot.creditRemoveMsg = "Attention citizen! "
bot.creditAddMsg2 = " social points have been added to your account! Chairman Ingen is satisfied with your behavior! Glory to Ingenistan!\n\nhttps://cdn.discordapp.com/attachments/800812999656341545/874410096145342504/video0-31.mp4 "
bot.creditRemoveMsg2 = " social points have been deducted from your account! Chairman Ingen is NOT satisfied with your behavior! Glory to Ingenistan!\n\nhttps://cdn.discordapp.com/attachments/800812999656341545/874410096145342504/video0-31.mp4 "
bot.prefix = "$"
bot.threshold1 = 400
bot.threshold2 = 600
bot.threshold3 = 1200
bot.threshold4 = 1500
bot.threshold1role = 874454569889964032
bot.threshold12role = 874454522217508944
bot.threshold23role = 874454491624263701
bot.threshold34role = 874454451539308624
bot.threshold4role = 874454309943799828

memberCredits = json.load(open('varStorage.json'))

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="check")
async def check(ctx, member: discord.Member=None):
  if member is None:
      member = ctx.message.author
  try:
    await ctx.send(memberCredits[member.id])
    json.dump(memberCredits, open('varStorage.json', 'w'))
  except KeyError:
    memberCredits[member.id] = 1000
    json.dump(memberCredits, open('varStorage.json', 'w'))
  print("h")
  return


@bot.command(name="add")
@commands.has_permissions(administrator=True)
async def add(ctx, member: discord.Member=None, amount: int=0):
  if member is None:
      await ctx.send("You're supposed to provide a user!")
      return
  try:
    memberCredits[member.id] += amount
    outl = (bot.creditAddMsg + str(amount) + bot.creditAddMsg2 + member.mention) if amount > 0 else (bot.creditRemoveMsg + str(amount) + bot.creditRemoveMsg2 + member.mention)
    
    json.dump(memberCredits, open('varStorage.json', 'w'))

    await ctx.send(outl)
    return
  except KeyError:
    memberCredits[member.id] = 1000
    memberCredits[member.id] += amount
    outl = (bot.creditAddMsg + str(amount) + bot.creditAddMsg2 + member.mention) if amount >= 0 else (bot.creditRemoveMsg + str(amount) + bot.creditRemoveMsg2 + member.mention)
    
    json.dump(memberCredits, open('varStorage.json', 'w'))

    await ctx.send(outl)
    return

@bot.command(name="setprefix")
@commands.has_permissions(administrator=True)
async def setPrefix(ctx, prefix=None):
    if prefix == None:
        await ctx.send("You're supposed to provide a prefix!")
        return
    bot.prefix = prefix
    
    await ctx.send("Prefix successfully changed to " + bot.prefix)
    return

# @bot.command(name="setvariable")
# @commands.has_permissions(administrator=True)
# async def setVar(ctx, var=None, val=None):
#     if var == None:
#         await ctx.send("You're supposed to provide a variable!")
#         return
#     if val == None:
#         await ctx.send("You're supposed to provide a value!")
#         return
#     s.Handle(str(ctx.guild.id), "add", var, val)

#     await ctx.send("Variable \"" + var + "\" successfully changed to: " + val)

@tasks.loop(seconds=0.5)
async def update_roles():
  try:
    for guild in bot.guilds:
      for member in guild.members:
        if memberCredits[member.id] <= bot.threshold1:
          if bot.threshold1role != "None":
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold1role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold12role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold23role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold34role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold4role))
            await member.add_roles(discord.utils.get(guild.roles, id = bot.threshold1role))
        if bot.threshold1 < memberCredits[member.id] <= bot.threshold2:
          if bot.threshold12role != "None":
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold1role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold12role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold23role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold34role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold4role))
            await member.add_roles(discord.utils.get(guild.roles, id = bot.threshold12role))
        if bot.threshold2 < memberCredits[member.id] <= bot.threshold3:
          if bot.threshold23role != "None":
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold1role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold12role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold23role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold34role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold4role))
            await member.add_roles(discord.utils.get(guild.roles, id = bot.threshold23role))
        if bot.threshold3 < memberCredits[member.id] <= bot.threshold4:
          if bot.threshold34role != "None":
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold1role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold12role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold23role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold34role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold4role))
            await member.add_roles(discord.utils.get(guild.roles, id = bot.threshold34role))
        if bot.threshold4 < memberCredits[member.id]:
          if bot.threshold4role != "None":
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold1role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold12role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold23role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold34role))
            await member.remove_roles(discord.utils.get(guild.roles, id = bot.threshold4role))
            await member.add_roles(discord.utils.get(guild.roles, id = bot.threshold4role))

      
      json.dump(memberCredits, open('varStorage.json', 'w'))
  except KeyError:
    memberCredits[member.id] = 1000
    json.dump(memberCredits, open('varStorage.json', 'w'))
  except AttributeError:
    return

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