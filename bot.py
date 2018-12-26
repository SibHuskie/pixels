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

loading_e = "<a:loading:484705261609811979>"
error_e = "<:error:516609910356574212>"
joined_e = "<:joined:516609910318956552>"
left_e = "<:left:516609910318956553>"
serverinfo_e = ":mag:"
userinfo_e = "<:userinfo:516609910465757184>"
avatar_e = "<:avatar:516609910008578049>"
suggestion_e = "<:suggestion:516609910088138772>"
upvote_e = "<:upvote:516609910235201536>"
downvote_e = "<:downvote:516609910214230016>"
lookup_e = "<:lookup:516609910553837578>"
partner_e = "<:partner:516609910390390815>"
log_e = "<:log:516609910415425536>"
roleme_e = "<:roleme:516609911006691338>"
pinggood_e = "<:pinggood:516609909819965441>"
pingok_e = "<:pingok:516609909832417296>"
pingbad_e = "<:pingbad:516609910168092682>"
reload_e = "<:reload:516609910235070472>"
worked_e = "<:worked:516609910310699042>"
roles_e = "<:roles:516614182045614080>"


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
    else:
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        m = "{} **__SERVER INFORMATION:__**".format(serverinfo_e)
        m += "\n"
        m += "\n**MEMBERS:** `{}`".format(len(ctx.message.server.members))
        m += "\n**CHANNELS:** `{}`".format(len(ctx.message.server.channels))
        m += "\n**EMOJIS:** `{}`".format(len(ctx.message.server.emojis))
        m += "\n**ID:** `{}`".format(ctx.message.server.id)
        m += "\n**REGION:** `{}`".format(ctx.message.server.region)
        m += "\n**ROLES:** `{}`".format(len(ctx.message.server.roles))
        m += "\n**CREATED BY:** `{}`".format(ctx.message.server.owner)
        m += "\n**CREATED AT:** `{}`".format(ctx.message.server.created_at)
        embed.description = m
        await client.say(embed=embed)
#######################
client.run(os.environ['BOT_TOKEN'])
