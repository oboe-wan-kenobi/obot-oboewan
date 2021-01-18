import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
import os.path
from os import path

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    loadscores(1)
    loadscores(2)



bot.run('Nzk3NjUyOTAzNDU5NDIyMjM4.X_pmJw.CN-oKN_Sgw8hM0SUBtyEPB4kSRw')