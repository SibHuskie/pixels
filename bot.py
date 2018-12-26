print("Starting Cube. . .")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

''''''

Client = discord.Client()
bot_prefix = ["px!", "Px!"]
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "Pixels"
limit = 1000000000000
version = "1.0"
splitter = "**~~`====================`~~**"




@client.async_event
async def on_member_join(userName: discord.User):
    m2 = "Welcome to **P i x e l s ™**, <@{}>! We hope you enjoy your stay and have fun.".format(userName.id)
    m2 += "\nAll information is in the <#426683264682557440> channel, but feel free to ask the staff about anything you want to know."
    m2 += "\https://giphy.com/gifs/1fmwoUOwMh5koSdpVD"
    m = "\n**Welcome to P i x e l s™, <@{}>! :sparkles:".format(userName.id)
    m += "\nRemember to read all the <#527430670255915008>."
    m += "\nAlso don't forget to get roles and colors in the <#527430670255915008> and the <#527430670255915008> channels :wink: \nEnjoy your stay :sparkling_heart:**"
    m += "\http://imgur.com/a/r6RyJm8"
    await client.send_message(client.get_channel("447634076866969610"), "{}".format(m))
    server = client.get_server('447634076866969610')
    try:
        await client.send_message(userName, "{}".format(m2))
    except:
        print("")

@client.async_event
async def on_member_remove(userName: discord.User):
    leaves = ["Cya `{}` :wave:".format(userName)]
    await client.send_message(client.get_channel("447634076866969610"), "{}".format(random.choice(leaves)))
    print("Leave")
    

#######################
client.run(os.environ['BOT_TOKEN'])
