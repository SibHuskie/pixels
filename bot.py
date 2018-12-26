import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS
import urbandictionary as ud

Client = discord.Client()
bot_prefix= "Px!"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='439658556656975872')
footer_text = "Pixels™"
error_img = ':x: '
default_invite = 'https://discord.gg/Xj6beq7'
banner = 'https://cdn.discordapp.com/attachments/484761617016291328/527361105006297108/Photoshop_ccpixel.png'

# say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id='Moderator')
    legend = discord.utils.get(ctx.message.server.roles, name='<@299761993382887425>')
    msg = discord.Embed(colour=0x284e87, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if args == None:
            msg.add_field(name=error_img, value="Please give a message that you want the bot to say.")
            await client.say(embed=msg)
        else:
            if len(str(args)) > 2000:
                msg.add_field(name=error_img, value="The message cannot be longer than 2000 characters.")
                await client.say(embed=msg)
            else:
                await client.say("{}".format(args))
                await client.delete_message(ctx.message)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Admins!")
        await client.say(embed=msg)
        
##################################
client.run(os.environ['BOT_TOKEN'])
