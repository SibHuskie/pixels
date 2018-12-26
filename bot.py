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
started = "2"




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
    
# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        embed.description = "{} Loading information...".format(loading_e)
        h = await client.say(embed=embed)
        m = "**ID:** `{}`".format(ctx.message.server.id)
        m += "\n**OWNER:** `{}`".format(ctx.message.server.owner)
        m += "\n**MEMBERS:** `{}`".format(len(ctx.message.server.members))
        m += "\n**REGION:** `{}`".format(ctx.message.server.region)
        m += "\n**CREATED AT:** `{}`".format(ctx.message.server.created_at)
        embed.description = "{} **__SERVER INFORMATION:__**\n\n{}".format(servers_e, m)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        ts = ""
        if ctx.message.server.id in currency_t:
            ts += "\n{}`Currency Rewards`{}".format(coins_e, off_e)
        else:
            ts += "\n{}`Currency Rewards`{}".format(coins_e, on_e)
        if ctx.message.server.id in responses_t:
            ts += "\n{}`Auto-Responses`{}".format(messages_e, off_e)
        else:
            ts += "\n{}`Auto-Responses`{}".format(messages_e, on_e)
        embed.add_field(name="{} TOGGLES:".format(bannedusers_e), value=ts, inline=True)
        ing = ""
        for i in ctx.message.server.channels:
            if i.id in ignored:
                ing += "  <#{}>".format(i.id)
        if ing != "":
            embed.add_field(name="{} IGNORED CHANNELS:".format(ignored_e), value=ing, inline=True)
        await client.edit_message(h, embed=embed)
#######################
client.run(os.environ['BOT_TOKEN'])
