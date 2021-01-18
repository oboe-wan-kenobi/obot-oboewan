import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os





async def setEnv(envName, val):
    os.environ[envName] = str(val)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='&', intents=intents)




@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    loadscores(1)
    loadscores(2)

@bot.command()
@commands.has_role("delete")
async def deletemessage(ctx, channelName, messageID):
    channel = discord.utils.get(ctx.guild.channels, name=channelName)
    msg = await channel.fetch_message(messageID)
    await msg.delete()
    await ctx.send("Message was deleted.")

def loadscores(house):
    if house == 1:
        try:
            #open files
            ozzyfile = open ('ozzy.txt', 'r')
            print("success reading files")

            #debug show file contents
            ozzy = ozzyfile.read()
            print(str(ozzy))
            ozzyfile.close()
            return ozzy
        except Exception as e:
            print("error reading" + str(e))
            
    elif house == 2:
        try:
            #open files
            mystfile = open ('myst.txt', 'r')
            print("success reading files")

            #debug show file contents
            myst = mystfile.read()
            print(str(myst))
            mystfile.close()
            return myst
        except Exception as e:
            print("error reading" + str(e))

@bot.command()
@commands.has_role('Administrators')
async def setscores(ctx, house, val=0):
    if house == '1':
        ozzyfile = open ('ozzy.txt', 'w+')
        ozzyfile.write(str(val))
        ozzyfile.close()
        send = 'Set Ozzymandia to ' + str(val)
        await ctx.send(send)
        print("help")
    elif house == '2':
        mystfile = open ('myst.txt', 'w+')
        mystfile.write(str(val))
        mystfile.close()
        send = 'Set Myst to ' + str(val)
        await ctx.send(send)

@bot.command()
@commands.has_role('Administrators')
async def addscores(ctx, house, pts=1):
    if house == '1':
        before = loadscores(1)
        ozzyfile = open ('ozzy.txt', 'w+')
        after = int(before) + int(pts)
        ozzyfile.write(str(after))
        ozzyfile.close()
        send = 'Set Ozzymandia to ' + str(after)
        await ctx.send(send)
        print("help")
    elif house == '2':
        before = loadscores(2)
        mystfile = open ('myst.txt', 'w+')
        after = int(before) + int(pts)
        mystfile.write(str(after))
        mystfile.close()
        send = 'Set Myst to ' + str(after)
        await ctx.send(send)
        print("help")

@bot.command()
async def showscores(ctx):
    ozzy = loadscores(1)
    myst = loadscores(2)
    await ctx.send("Ozzymandia: " + str(ozzy))
    await ctx.send("Myst: " + str(myst))

@bot.command()
async def test(ctx):
    loadscores()
    
   
#@bot.event
#async def on_message(message):
#    if str(message).startswith("&"):
#        print("Command recieved.")



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
@commands.has_role('Moderator')
async def msgm(ctx, msg, channelName, credit=False):
    channel = discord.utils.get(ctx.guild.channels, name=channelName)
    if credit:
        msgcop = ctx.author.mention + " says: " + msg
        await channel.send(msgcop)
    else:
        await channel.send(msg)

@bot.command()
@commands.has_role('Owner')
async def msgo(ctx, msg, channelName, credit=False, delete=False):
    channel = discord.utils.get(ctx.guild.channels, name=channelName)
    if credit:
        msgcop = ctx.author.mention + " says: " + msg
        await channel.send(msgcop)
    else:
        await channel.send(msg)
    if delete:
        await ctx.message.delete()

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
@commands.has_role("mute")
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

@bot.command()
@commands.has_role("Moderator")
async def mutem(ctx, opt, member: discord.Member, seconds = 0):
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

@bot.event
async def on_message(message):
    nonos = ["nigg", "nig ", "nig.", "fag", "whore", "dike", "dix", "ooptestlol", "dyke", "slut", "foreskin", "tard", "kyke", "slur", "cunt"]
    standalones = ["nig", "nigg", "nig ", "nig.", "fag", "whore", "dike", "dix", "ooptestlol", "dyke", "slut", "foreskin", "tard", "kyke", "slur", "cunt"]
    symbols = [" ", "*", "-", "=", "!", "@", "#", "$", "%", "^", "&", "*" "(", ")", ".", ",", "`", "~", "/", "\\", "+", "=", "-", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    censors = ["sex", "hentai", "censortest", "vag", "pussy", "penis", "naked", "nude", "boob", "breast", "horny", "dick", "smexy", "knife", "blood", "blade", "kill", "abuse", "slaughter", "death", "dead", "suic", "kms", "kys", "bleach", "orgasm", "burn", "stab"]


    for nono in nonos:
        
        for symbol in symbols:
            s = (symbol.join(nono))

            if s in str(message.content).lower():
                await message.channel.send("Words like that are not allowed here, " + str(message.author.mention))
                await message.delete() 
            
        if nono in str(message.content).lower():
            await message.channel.send("Words like that are not allowed here, " + str(message.author.mention))
            await message.delete() 
        
        #for symbol in symbols:

            #for s in str(message.content).lower():
             #   no = 
              #  await message.channel.send("Words like that are not allowed here, " + str(message.author.mention))
               # await message.delete() 
        
    for standalone in standalones:

        if str(message.content).lower() == standalone:
            await message.channel.send("Words like that are not allowed here, " + str(message.author.mention))
            await message.delete() 
    
    if not "||" in str(message.content):
        if not "a!censor" in str(message.content):
            for censor in censors:
                if censor in str(message.content):
                    censored = message.author.mention + ": ||" + str(message.content) + "||"
                    await message.channel.send(censored)
                    await message.delete()

    await bot.process_commands(message)

bot.run('Nzk3NjUyOTAzNDU5NDIyMjM4.X_pmJw.CN-oKN_Sgw8hM0SUBtyEPB4kSRw')