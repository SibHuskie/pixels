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
error_img = ':x: '
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

owner_roles_chnl = '527373834618273803'
manager_roles_chnl = '527373849495339008'
admin_roles_chnl = '527373859335176202'
mod_roles_chnl = '527373873394483200'
helper_roles_chnl = '516605337248464906'
partner_manager_roles_chnl = '516606847323734064'
partner_roles_chnl = '516606872896405520'
muted_roles_chnl = '516607156813037608'
member_roles_chnl = '516607267127164942'
self_roles_chnl = '516611549427793930'
logs_chnl = '516614512657563658'
log_chnl = '516594957432389632'
joins_leaves_chnl = '516616002012839936'


# staff
@client.command(pass_context=True)
async def staff(ctx):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        embed.description = "{} Loading staff list... {}".format(roles_e, loading_e)
        k = await client.say(embed=embed)
        
        try:
            roles = {"owners" : owner_roles,
                     "managers" : manager_roles,
                     "admins" : admin_roles,
                     "mods" : mod_roles,
                     "helpers" : helper_roles,
                     "pms" : partner_manager_roles}
            owners = ""
            managers = ""
            admins = ""
            mods = ""
            helpers = ""
            pms = ""
            roles_l = {"owners" : owners,
                       "managers" : managers,
                       "admins" : admins,
                       "mods" : mods,
                       "helpers" : helpers,
                       "pms" : pms}
            for i in roles:
                for u in roles[i]:
                    if u in ctx.message.server.roles:
                        for o in ctx.message.server.members:
                            if u in o.roles:
                                roles_l[i] += "\n`{}`".format(o.name)
                        embed.add_field(name="{}".format(u.name), value=roles_l[i], inline=True)
            embed.description = "{} **__STAFF LIST:__**".format(roles_e)
            await client.edit_message(k, embed=embed)
        except:
            embed.description = "{} There was an error while loading the staff list. Please try again.".format(error_e)
            await client.edit_message(k, embed=embed)
        
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
        
##################################
client.run(os.environ['BOT_TOKEN'])
