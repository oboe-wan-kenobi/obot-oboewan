import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os

token = os.environ.get('token')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='&', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
@commands.has_role('Administrators')
async def msga(ctx, msg, channelName, credit=False):
    channel = discord.utils.get(ctx.guild.channels, name=channelName)
    if credit:
        msgcop = ctx.author.mention + " says: " + msg
        await channel.send(msgcop)
    else:
        await channel.send(msg)

@bot.command()
@commands.has_role('Owner')
async def msgo(ctx, msg, channelName, credit=False):
    channel = discord.utils.get(ctx.guild.channels, name=channelName)
    if credit:
        msgcop = ctx.author.mention + " says: " + msg
        await channel.send(msgcop)
    else:
        await channel.send(msg)

@bot.command()
async def msg(ctx, msg, channelName):
    channel = discord.utils.get(ctx.guild.channels, name=channelName)
    msgcop = ctx.author.mention + ": " + msg
    await channel.send(msgcop)
    await ctx.message.delete()

@bot.command()
@commands.has_role("Administrators")
async def dm(ctx, user: discord.User, msg):
    #user = bot.get_user(id)
    await user.send(msg)

async def idCheck(id, crx):
    if id.isdecimal():
        return True
    else:
        await crx.send("Failure, id is not valid.")
        return False

@bot.command()
@commands.bot_has_permissions(manage_roles=True)
async def mute(ctx, opt, member: discord.Member, seconds = 0):
    muteRole = discord.utils.get(ctx.guild.roles, name="muted")
    if opt == 'mute':
        await member.add_roles(muteRole)
        await ctx.send('User has been muted.')
    elif opt == 'unmute':
        await member.remove_roles(muteRole)
        await ctx.send('User has been unmuted.')
    else:
        await ctx.send('Failure, you did not select to either mute or unmute.\nCorrect command syntax is `&mute <"mute" or "unmute"> <user id or mention>`.')
    if seconds != 0:
        await asyncio.sleep(seconds)
        await member.remove_roles(muteRole)
        await ctx.send('User has been unmuted.')

bot.run(token)