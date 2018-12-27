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

owner_roles_chnl = '527410451655426058'
manager_roles_chnl = '527410482844532736'
admin_roles_chnl = '527410517388820480'
mod_roles_chnl = '527410541191495680'
helper_roles_chnl = '527410570018816012'
partner_manager_roles_chnl = '516606847323734064'
partner_roles_chnl = '516606872896405520'
muted_roles_chnl = '516607156813037608'
member_roles_chnl = '516607267127164942'
self_roles_chnl = '516611549427793930'
logs_chnl = '516614512657563658'
log_chnl = '516594957432389632'
joins_leaves_chnl = '516616002012839936'


loading_e = ":arrows_counterclockwise: "
error_e = ":x:"
joined_e = "<:joined:516609910318956552>"
left_e = "<:left:516609910318956553>"
serverinfo_e = ":mag:"
userinfo_e = ":bust_in_silhouette: "
avatar_e = ":frame_photo:"
suggestion_e = "<:suggestion:516609910088138772>"
upvote_e = "<:upvote:516609910235201536>"
downvote_e = "<:downvote:516609910214230016>"
lookup_e = ":mag:"
partner_e = "<:partner:516609910390390815>"
log_e = "<:log:516609910415425536>"
roleme_e = "<:roleme:516609911006691338>"
pinggood_e = "<:pinggood:516609909819965441>"
pingok_e = "<:pingok:516609909832417296>"
pingbad_e = "<:pingbad:516609910168092682>"
reload_e = ":arrows_counterclockwise: "
worked_e = "<:worked:516609910310699042>"
roles_e = "<:roles:516614182045614080>"


@client.async_event
async def on_member_join(userName: discord.User):
    m2 = "Welcome to **P i x e l s ™**, <@{}>! We hope you enjoy your stay and have fun.".format(userName.id)
    m2 += "\nAll information is in the <#426683264682557440> channel, but feel free to ask the staff about anything you want to know."
    m2 += "\https://giphy.com/gifs/1fmwoUOwMh5koSdpVD"
    m = "\n**Welcome to P i x e l s™, <@{}>! :sparkles:".format(userName.id)
    m += "\nRemember to read all the <#447618217805086720>."
    m += "\nAlso don't forget to get roles and colors in the <#471257818482343957> and the <#471257883712028683> channels :wink: \nEnjoy your stay :sparkling_heart:**\nhttp://imgur.com/a/r6RyJm8"
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
    
# serverinfo
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
        
# userinfo [user]
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
        
# avatar [user]
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
        embed = discord.Embed(colour=0x000000)
        embed.set_footer(text=footer_text)
        embed.description = "{} Here is **{}**'s avatar:".format(avatar_e, author.name)
        embed.set_image(url=author.avatar_url)
        await client.say(embed=embed)
        
# lookup <id>
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
                
# say <text>
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
            
# cointoss
@client.command(pass_context=True)
async def cointoss(ctx):
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
    else:
        msgs = ["heads", "tails"]
        embed.description = "{} It's {}!".format(cointoss_e, random.choice(msgs))
        await client.say(embed=embed)
        
# suicide
@client.command(pass_context=True)
async def suicide(ctx):
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
    else:
        msgs = ["**{}** tried to commit suicide but failed! Better luck next time I guess.".format(ctx.message.author.name),
                "**{}** killed themselves after losing all their diamonds on their christian minecraft server.".format(ctx.message.author.name),
                "**{}** had no internet connection for more than 5 seconds so they commited suicide.".format(ctx.message.author.name),
                "**{}** felt weird in the middle of the night, but hentaihaven was down so they killed themselves.".format(ctx.message.author.name),
                "**{}** didn't really have a life, but they still managed to kill themselves.".format(ctx.message.author.name),
                "**{}** watched boku no pico, few seconds later they jumped off the 7th floor.".format(ctx.message.author.name),
                "**{}** saw Zero's face. They instantly commited suicide after that.".format(ctx.message.author.name),
                "All of **{}**'s memes were stolen. Not having any memes or dreams left, they decided to kill themselves.".format(ctx.message.author.name),
                "**{}** realized how shitty this server actually is. Leaving it wasn't enough so they commited suicide too.".format(ctx.message.author.name),
                "**{}** had anxiety for way too long. They couldn't live with it anymore so they took their own life away.".format(ctx.message.author.name),
                "**{}** was bipolar. That disorder was messing up their life too much so they commited suicide.".format(ctx.message.author.name),
                "**{}** suffered from depression for years. Not having any hope or motivation left, they commited suicide.".format(ctx.message.author.name),
                "**{}** was physically abused every day. They thought killing themselves would make things better.".format(ctx.message.author.name),
                "**{}** was sexually abused. That experience made them take their own life away.".format(ctx.message.author.name),
                "**{}** lived in war and chaos for a very long time. The day they had enough was the day they killed themselves.".format(ctx.message.author.name),
                "**{}** was bullied in school, outside, even at home. They couldn't take it anymore so they commited suicide.".format(ctx.message.author.name),
                "**{}** had a personality disorder that made them take their life away.".format(ctx.message.author.name),
                "**{}** had an eating disorder. They couldn't eat anything without thorwing up after that so they took their life away.".format(ctx.message.author.name),
                "**{}** was lonely all their life. Not having any friends or family, they killed themselves without anyone finding out.".format(ctx.message.author.name),
                "**{}** had a great relationship that started to fall apart. After their partner left them, they became depressed and decided to kill themselves, thinking no one would ever love them again.".format(ctx.message.author.name),
                "**{}** commited suicide. Too bad there's no one to leave a flower on their grave...".format(ctx.message.author.name),
                "**{}** killed themselves.".format(ctx.message.author.id)]
        embed.description = "{} {}".format(suicide_e, random.choice(msgs))
        await client.say(embed=embed)
#######################
client.run(os.environ['BOT_TOKEN'])
