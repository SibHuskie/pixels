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
bot_prefix= ["px!", "Px!"]
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='439658556656975872')
footer_text = "Pixels™"
limit = 100000000000000000
default_invite = 'https://discord.gg/Xj6beq7'
banner = 'https://cdn.discordapp.com/attachments/484761617016291328/527361105006297108/Photoshop_ccpixel.png'

owner_roles = []
manager_roles = []
admin_roles = []
mod_roles = []
helper_roles = []
partner_manager_roles = []
partner_roles = []
muted_roles = []
member_roles = []
self_roles = []
logs = []
joins_leaves = []
started = [1]

owner_roles_chnl = '516605295816867871'
manager_roles_chnl = '516606147558506507'
admin_roles_chnl = '516605310203592704'
mod_roles_chnl = '516605319665680405'
helper_roles_chnl = '516605337248464906'
partner_manager_roles_chnl = '516606847323734064'
partner_roles_chnl = '516606872896405520'
muted_roles_chnl = '516607156813037608'
member_roles_chnl = '516607267127164942'
self_roles_chnl = '516611549427793930'
logs_chnl = '516614512657563658'
log_chnl = '516594957432389632'
joins_leaves_chnl = '516616002012839936'

loading_e = "<a:loading:484705261609811979>"
error_e = ":x:"
joined_e = "<:joined:516609910318956552>"
left_e = "<:left:516609910318956553>"
serverinfo_e = ":crown: "
userinfo_e = ":bust_in_silhouette: "
avatar_e = ":frame_photo: "
suggestion_e = "<:suggestion:516609910088138772>"
upvote_e = "<:upvote:516609910235201536>"
downvote_e = "<:downvote:516609910214230016>"
lookup_e = ":mag: "
partner_e = "<:partner:516609910390390815>"
log_e = "<:log:516609910415425536>"
roleme_e = "<:roleme:516609911006691338>"
pinggood_e = "<:pinggood:516609909819965441>"
pingok_e = "<:pingok:516609909832417296>"
pingbad_e = "<:pingbad:516609910168092682>"
reload_e = "<:reload:516609910235070472>"
worked_e = "<:worked:516609910310699042>"
roles_e = "<:roles:516614182045614080>"
        
# }userinfo [user]
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.User = None):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        a = []
        for i in muted_roles:
            if i in ctx.message.server.roles:
                a.append(i)
                break
        if user == None:
            author = ctx.message.author
        else:
            author = user
        embed.set_thumbnail(url=author.avatar_url)
        m = "{} **__USER INFORMATION:__**".format(userinfo_e)
        m += "\n"
        m += "\n**NAME:** `{}`".format(author)
        m += "\n**ID:** `{}`".format(author.id)
        m += "\n**CREATED AT:** `{}`".format(author.created_at)
        m += "\n**JOINED AT:** `{}`".format(author.joined_at)
        m += "\n**STATUS:** `{}`".format(author.status)
        m += "\n**IS BOT:** `{}`".format(author.bot)
        m += "\n**GAME:** `{}`".format(author.game)
        m += "\n**NICKNAME:** `{}`".format(author.nick)
        m += "\n**TOP ROLE:** `{}`".format(author.top_role)
        m += "\n**VOICE CHANNEL:** `{}`".format(author.voice_channel)
        if len(a) != 0:
            if a[0] in author.roles:
                m += "\n**MUTED:** `True`"
            else:
                m += "\n**MUTED:** `False`"
        embed.description = m
        await client.say(embed=embed)
        
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
        
# }avatar [user]
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member = None):
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if user == None:
            author = ctx.message.author
        else:
            author = user
        embed = discord.Embed(colour=0x000)
        embed.set_footer(text=footer_text)
        embed.description = "{} Here is **{}**'s avatar:".format(avatar_e, author.name)
        embed.set_image(url=author.avatar_url)
        await client.say(embed=embed)
        
# }lookup <id>
@client.command(pass_context=True)
async def lookup(ctx, ID = None):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if ID == None:
            embed.description = "{} Please give a user ID you want to look up.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                user = await client.get_user_info(ID)
                embed.set_thumbnail(url=user.avatar_url)
                m = "{} **__USER INFORMATION:__**".format(lookup_e)
                m += "\n"
                m += "\n**NAME:** `{}`".format(user)
                m += "\n**ID:** `{}`".format(user.id)
                m += "\n**CREATED AT:** `{}`".format(user.created_at)
                m += "\n**IS BOT:** `{}`".format(user.bot)
                embed.description = m
                await client.say(embed=embed)
            except:
                embed.description = "{} User with that ID has not been found.".format(error_e)
                await client.say(embed=embed)
##################################
client.run(os.environ['BOT_TOKEN'])
