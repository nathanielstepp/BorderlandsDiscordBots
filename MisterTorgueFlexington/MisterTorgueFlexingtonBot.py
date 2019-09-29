# FILE INFORMATION:
#
# Filename:   MisterTorgueFlexingtonBot.py
# Project:    Mister Torgue Flexington Discord Bot
# Created By: Mark Goodrich (mark.d.goodrich@gmail.com)
#             Nathaniel Stepp (stepp.nathaniel@gmail.com)
# Created On: 2019/09/27
#
# Descritption: Main Python script used to operate the Mister Torgue Flexington Discord Bot.
#               Script pulls from two seperate files to randomly select a quote (stored in: 
#               MisterTorgueFlexingtonQuotes.py) given one of catch phrases (stored in: 
#               MisterTorgueFlexingtonCatchPhrases.py) is mentioned in any text channel of a
#               Discord server text chat.

import os
import random
import discord
from dotenv import load_dotenv
from MisterTorgueFlexingtonCatchPhrases import catchPhrases
from MisterTorgueFlexingtonQuotes import torgueQuotes

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    game = discord.Game("Air Guitar")
    await client.change_presence(status = discord.Status.online, activity = game);

@client.event
async def on_message(message):
    if message.author == client.user:
        return
	
    if any(x in message.content for x in catchPhrases):
        response = random.choice(torgueQuotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(token)
