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

##################################
client.run(os.environ['BOT_TOKEN'])
