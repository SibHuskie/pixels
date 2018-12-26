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
logs_chnl = '527385743224733706'
log_chnl = '527385743224733706'
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
                
# }say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if args == None:
            embed.description = "{} Please give a message that you want me to say.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 2000:
            embed.description = "{} The message cannot be longer than 2000 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            await client.say("`{}`".format(args))
            await client.delete_message(ctx.message)
                
############### FOR PARTNERS ############

# }p <user>
@client.command(pass_context=True)
async def p(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        partner = []
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles, partner_manager_roles]
        for i in partner_roles:
            if i in ctx.message.server.roles:
                partner.append(i)
                break
        if len(partner) != 0:
            a = []
            for i in roles:
                for u in i:
                    if u in ctx.message.server.roles and u in ctx.message.author.roles:
                        if user == None:
                            embed.description = "{} No user was mentioned.".format(error_e)
                            await client.say(embed=embed)
                        elif user.bot:
                            embed.description = "{} Bots can't be partners.".format(error_e)
                            await client.say(embed=embed)
                        elif partner[0] in user.roles:
                            await client.remove_roles(user, partner[0])
                            embed.description = "{} **{}** removed the partner role from **{}**.".format(partner_e, author.name, user.name)
                            await client.say(embed=embed)
                            m = splitter
                            m += "\n{} **__Removed Partner Role__** {}".format(log_e, partner_e)
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            for o in logs:
                                b = o.split(' | ')
                                if b[0] == ctx.message.server.id:
                                    c = client.get_channel(b[1])
                                    await client.send_message(c, m)
                        else:
                            await client.add_roles(user, partner[0])
                            embed.description = "{} **{}** gave the partner role to **{}**.".format(partner_e, author.name, user.name)
                            await client.say(embed=embed)
                            m = splitter
                            m += "\n{} **__Added Partner Role__** {}".format(log_e, partner_e)
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            for o in logs:
                                b = o.split(' | ')
                                if b[0] == ctx.message.server.id:
                                    c = client.get_channel(b[1])
                                    await client.send_message(c, m)
                        a.append("+1")
                        break
                if len(a) != 0:
                    break
            if len(a) == 0:
                embed.description = "{} This command can only be used by partner managers and staff.".format(error_e)
                await client.say(embed=embed)
        else:
            embed.description = "{} No partner role found in the database.".format(error_e)
            await client.say(embed=embed)

########################## STAFF ########################
# }setrole <option> <role name>
@client.command(pass_context=True)
async def setrole(ctx, option = None, *, args = None):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        a = []
        for i in owner_roles:
            if i in ctx.message.server.roles and i in ctx.message.author.roles:
                options = ["owner", "manager", "admin", "mod", "helper", "muted"]
                if option == None or args == None:
                    embed.description = "{} Not all arguments were given.\nOptions: `owner`, `manager`, `admin`, `mod`, `helper`, `muted`.\nTo remove a role from the database write the role's name like this: `<role name> | none`.".format(error_e)
                    await client.say(embed=embed)
                elif option.lower() not in options:
                    embed.description = "{} Invalid option.\nOptions: `owner`, `manager`, `admin`, `mod`, `helper`, `muted`.\nTo remove a role from the database write the role's name like this: `<role name> | none`.".format(error_e)
                    await client.say(embed=embed)
                else:
                    t = {"owner" : owner_roles_chnl,
                         "manger" : manager_roles_chnl,
                         "admin" : admin_roles_chnl,
                         "mod" : mod_roles_chnl,
                         "helper" : helper_roles_chnl,
                         "muted" : muted_roles_chnl}
                    k = {"owner" : owner_roles,
                         "manger" : manager_roles,
                         "admin" : admin_roles,
                         "mod" : mod_roles,
                         "helper" : helper_roles,
                         "muted" : muted_roles}
                    embed.description = "{} Editing roles database... {}".format(roles_e, loading_e)
                    h = await client.say(embed=embed)
                    p = []
                    r = []
                    for u in ctx.message.server.roles:
                        if ' | ' in args:
                            y = args.split(' | ')
                            args = y[0]
                            r.append(y[1])
                        if args.lower() in str(u.name.lower()):
                            p.append("+1")
                            if " | none" in r:
                                async for o in client.logs_from(client.get_channel(t[option]), limit=limit):
                                    b = o.content.split(' | ')
                                    if b[0] == ctx.message.server.id and b[1] == u.id:
                                        await client.delete_message(o)
                                        k[option].remove(u)
                                        break
                                embed.description = "{} **{}** removed `{}` from the `{}` roles database.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Removed role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Role type:` {}".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                                break
                            elif option.lower() != "member":
                                async for o in client.logs_from(client.get_channel(t[option]), limit=limit):
                                    b = o.content.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        k[option].remove(discord.utils.get(ctx.message.server.roles, id=b[1]))
                                        await client.delete_message(o)
                                        break
                                await client.send_message(client.get_channel(t[option]), "{} | {}".format(ctx.message.server.id, u.id))
                                k[option].append(u)
                                embed.description = "{} **{}** set the `{}` role as `{}`.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Set role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Set as:` {}".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                                break
                            else:
                                await client.send_message(client.get_channel(t[option]), "{} | {}".format(ctx.message.server.id, u.id))
                                k[option].append(u)
                                embed.description = "{} **{}** set the `{}` role as `{}`/`auto role`.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Set role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Set as:` {}/auto role".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                                break
                    if len(p) == 0:
                        embed.description = "{} Role not found.".format(error_e)
                        await client.edit_message(h, embed=embed)
                a.append("+1")
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)

##################################
client.run(os.environ['BOT_TOKEN'])
