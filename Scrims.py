# Discord Gamecodes bot by indskys#2484
# Python version 3.6
# Please note there are better ways to display gamecodes

import discord
from discord.utils import get
import asyncio

# Type your discord token here
TOKEN = 'XXXXXXXXXXXXXX'
client = discord.Client()

# If you want to save the gamecodes use this list
gamecodes = []

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('+game'):
        sortedCodes = {}
        msg = message.content.split(" ")
        playerCode = msg[1]
        if len(playerCode) == 4:
            sender = '{0.author.mention}'.format(message) 
            sender = sender.replace('!', '')
            contentMessage = ""

            if any(sender in s for s in gamecodes):
                for i in range(len(gamecodes)):
                    if sender in gamecodes[i]:
                        await client.send_message(message.channel, '{0.author.mention}'.format(message) + " You have already sent a gamecode, your code has now been updated!")
                        gamecodes[i] = (sender + ' ' + msg[1] + ' \n')
            else:
                gamecodes.append(sender + ' ' + msg[1] + ' \n')
                    
            for i in range(len(gamecodes)):
                splitCode = gamecodes[i].split(" ")
                if splitCode[1] in sortedCodes:
                        sortedCodes[splitCode[1]] += "\n" + splitCode[0]
                if splitCode[1] not in sortedCodes:
                        sortedCodes[splitCode[1]] = '**__' + splitCode[1] + '__** \n' + splitCode[0]
                            
            for i in sortedCodes:
                sortedLengthTemp = str((len(sortedCodes[i])-9)/22).split(".")
                sortedLength = "(**" + sortedLengthTemp[0] + "**) "
                sortedCodes[i] = str(sortedLength) + sortedCodes[i]
                contentMessage += sortedCodes[i] + "\n"
            
            contentMessage += "\n Type +game <4 digit code>"
            await client.delete_message(message)
			#Edit the line below to change the colour of the embed message
            em = discord.Embed(title='__Game Codes:__', description= contentMessage, colour=0xFFFF00)
			#I have this set to my bots name "FortniteOCE"
            em.set_author(name='FortniteOCE', icon_url=client.user.avatar_url)
			#Change this to what you want in your embeded messages footer (You can change the author if you like.)
            em.set_footer(text='FortniteOCE.com • indskys#2484')
            await client.send_message(message.channel, embed=em)
        else:
            await client.send_message(message.channel, '{0.author.mention}'.format(message) + " Please enter a gamecode that is 4 digit's. ")

    if message.content.startswith('+reset'):
		#change "scrim host" to what role you want to allow to do the command +reset
        if "scrim host" in [y.name.lower() for y in message.author.roles]:
            del gamecodes[:]
            await client.send_message(message.channel, '{0.author.mention}'.format(message) + " The gamecodes have been reset. ")

@client.event
async def on_ready():
    print('------')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
