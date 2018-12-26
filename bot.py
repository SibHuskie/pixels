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
error_e = "<:error:516609910356574212>"
joined_e = "<:joined:516609910318956552>"
left_e = "<:left:516609910318956553>"
serverinfo_e = "<:serverinfo:516609910088400922>"
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

# START UP SYSTEM
started = []
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(owner_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        owner_roles.append(role)
    print("[START UP] Loaded owner roles.")
    async for i in client.logs_from(client.get_channel(manager_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        manager_roles.append(role)
    print("[START UP] Loaded manager roles.")
    async for i in client.logs_from(client.get_channel(admin_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        admin_roles.append(role)
    print("[START UP] Loaded administrator roles.")
    async for i in client.logs_from(client.get_channel(mod_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        mod_roles.append(role)
    print("[START UP] Loaded moderator roles.")
    async for i in client.logs_from(client.get_channel(helper_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        helper_roles.append(role)
    print("[START UP] Loaded helper roles.")
    async for i in client.logs_from(client.get_channel(partner_manager_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        partner_manager_roles.append(role)
    print("[START UP] Loaded partner manager roles.")
    async for i in client.logs_from(client.get_channel(partner_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        partner_roles.append(role)
    print("[START UP] Loaded partner roles.")
    async for i in client.logs_from(client.get_channel(member_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        member_roles.append(role)
    print("[START UP] Loaded member roles.")
    async for i in client.logs_from(client.get_channel(self_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        self_roles.append(role)
    print("[START UP] Loaded self roles.")
    async for i in client.logs_from(client.get_channel(muted_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        muted_roles.append(role)
    print("[START UP] Loaded muted roles.")
    async for i in client.logs_from(client.get_channel(logs_chnl), limit=limit):
        logs.append(i.content)
    print("[START UP] Loaded logs channels.")
    async for i in client.logs_from(client.get_channel(joins_leaves_chnl), limit=limit):
        joins_leaves.append(i.content)
    print("[START UP] Loaded join-leave channels.")
    started.append("+1")
    print("[START UP] Finished.")
    await client.change_presence(game=discord.Game(name="px!help | px!invite"))
    m = splitter
    m += "\n{} **__Bot Restart__** {} `-` Version: {}".format(log_e, reload_e, version)
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel(log_chnl))
    t2 = time.perf_counter()
    m += "\n{} Ping: `{}ms`".format(pingok_e, round((t2-t1)*1000))
    await client.send_message(client.get_channel(log_chnl), m)

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
