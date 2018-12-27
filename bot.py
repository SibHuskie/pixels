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

eb = ["Hell no!",
      "No!",
      "Hell yes!",
      "Yes!",
      "Definitely!",
      "Definitely not!",
      "Probably!",
      "Probably not!",
      "Most likely!",
      "Yes! I'm sure of it!",
      "No! I'm sure of it!"]

rps_choices = ["rock", "paper", "scissors", "r", "p", "s"]
rps_r = ["rock", "r"]
rps_p = ["paper", "p"]
rps_s = ["scissors", "s"]
rps_tie = {"rock" : "rock",
           "paper" : "paper",
           "scissors" : "scissors",
           "r" : "rock",
           "p" : "paper",
           "s" : "scissors"}

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
mods = ['527373873394483200']
mods_chnl = '527410541191495680'
banned_users = []
banned_servers = []
ignored = []
currency_t = []
responses_t = []
currencies = []
ships = []

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
ships_chnl = '527708373144174594'


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
loading_e = "<a:loading:484705261609811979>"
slotsgif1_e = "<a:slotsgif1:519832184039669760>"
slotsgif2_e = "<a:slotsgif2:519832184622940160>"
slotsgif3_e = "<a:slotsgif3:519832184383733761>"
slotsgif4_e = "<a:slotsgif4:519832184123686922>"
bug_e = "<:bug1:515909292491014144>"
close_e = "<:close:515909294818983936>"
log_e = "<:log:515909294818983936>"
msg_e = "<:msg:515909301051850753>"
noperms_e = "<:noperms:515909299461947402>"
pingbad_e = "<:pingbad:515911795307970565>"
pinggood_e = "<:pinggood:515911795492257793>"
pingok_e = "<:pingok:515911795693715476>"
reload_e = "<:reload:515909299755548672>"
servers_e = "<:servers:515909300271448080>"
support_e = "<:support:515909300275904512>"
users_e = "<:users:515909300334362624>"
worked_e = "<:worked:516244345473597470>"
check_e = "<:check:515909294042906665>"
interactions_e = "<:interactions:515909296043851796>"
game_e = ":video_game: "
battle_e = ":crossed_swords: "
messages_e = "<:messages:515909299495763968>"
bannedservers_e = "<:bannedservers:515909292101074945>"
bannedusers_e = "<:bannedusers:515909292419973130>"
cointoss_e = ":moneybag: "
suicide_e = ":skull: "
roast_e = ":fire: "
calculator_e = ":1234: "
ship_e = ":100: "
kill_e = "<:kill:515909300149944321>"
rate_e = "<:rate:515909299793428501>"
dicklength_e = "<:dicklength:515909294546485248>"
howgay_e = "<:howgay:515909296043589633>"
suggestion_e = "<:suggestion:515909299914932250>"
coins_e = "<:coins:515909294059814913>"
divorce_e = "<:divorce:515909294080786434>"
marriage_e = "<:marriage:515909297272651794>"
convert_e = "<:convert:515909300330430476>"
slots_e = "<:slots:515909300196212747>"
on_e = "<:on1:515911795836321802>"
off_e = "<:off:515911795454509057>"
ignored_e = "<:ignored:515909296303767552>"
work_e = "<:work:519837021850566667>"
generator_e = "<:generator:519841353077751809>"
steal_e = "<:steal:519845656928452632>"
gift_e = "<:gift1:519849587100614658>"
ban_e = "<:ban:519859483330215936>"
link_e = "<:link1:520593270494199819>"


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
                "**{}** saw Huskie's face. They instantly commited suicide after that.".format(ctx.message.author.name),
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
        
# roast <user>
@client.command(pass_context=True)
async def roast(ctx, user: discord.Member = None):
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
        if user == None:
            embed.description = "{} Please mention the user you want to roast.".format(error_e)
            await client.say(embed=embed)
        else:
            if user.id == client.user.id:
                user = ctx.message.author
            else:
                user = user
            msgs = ["Why would I bother roasting someone like **{}** when the mirror does it every morning?".format(user.name),
                    "We all hate you, **{}**. Just not quite enough to think about you.".format(user.name),
                    "**{}** don't play hard to get when you are hard to want.".format(user.name),
                    "God wasted a good asshole when he put teeth in your mouth, **{}**.".format(user.name),
                    "I can't even call **{}** ugly. Nature has beaten me to it.".format(user.name),
                    "I can't roast **{}**. I simply can't imagine the pain they go thru with that face.".format(user.name),
                    "**{}**, I would call you a cunt, but you lack the warmth or the depth.".format(user.name),
                    "**{}**, you remind me of Huskie. Get out of here!".format(user.name),
                    "**{}**'s are trash.".format(user.name),
                    "**{}**, you're a great shower when you speak.".format(user.name),
                    "I can't breathe when I see you, **{}**. Because I'm suffocating from your bullshit.".format(user.name),
                    "**{}**, the only way you'll ever get laid is if you crawl up a chicken's ass and wait.".format(user.name),
                    "**{}**, I just stepped in something that is smarter than you. It smelled better too.".format(user.name),
                    "**{}**, you're as stupid as your father when he thought he didn't need a condom.".format(user.name),
                    "**{}**, it's a joke, not a dick. You don't have to take it so hard.".format(user.name),
                    "**{}**, the only thing that would fuck you is life.".format(user.name),
                    "What's the difference between 3 dicks and a joke? **{}** can't take a joke.".format(user.name),
                    "**{}**, you have more dick in your personality than in your pants.".format(user.name),
                    "**{}**, even your father would be disappointed in your if he stayed.".format(user.name),
                    "**{}** should put a condom on their head. Cause if they're gonna act like a dick, they might as well dress like one too.".format(user.name),
                    "**{}**, you were probably birthed out of your mother's ass cause her pussy was too busy.".format(user.name),
                    "**{}** is such a pussy that fucking them wouldn't be gay.".format(user.name),
                    "If I wanted to kill myself, I'd climb up your ego and jump into your IQ, **{}**.".format(user.name),
                    "If laughter is the best medicine, **{}**'s face must be curing the world.".format(user.name),
                    "**{}**, your family tree is probably a cactus. Cause everyone on it is a prick.".format(user.name),
                    "**{}** is so ugly that when they look in the mirror, their reflection looks away.".format(user.name),
                    "**{}**, it's better to let someone think you're stupid than open your mouth and prove it.".format(user.name),
                    "**{}**, you're so ugly that you have to trick or treat over the phone.".format(user.name),
                    "**{}**, you're so fat that your school photo was a double picture.".format(user.name),
                    "**{}** is so stupid that they called me to ask me for my phone number.".format(user.name),
                    "**{}** is hating themselves too much for me to roast them.".format(user.name),
                    "**{}** is so fat that Thanos had to snap twice.".format(user.name),
                    "**{}**'s hair looks like a virginity helmet.".format(user.name)]
            embed.description = "{} {}".format(roast_e, random.choice(msgs))
            await client.say(embed=embed)
            
# eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args = None):
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
        if args == None:
            embed.description = "{} Please ask me a question.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 200:
            embed.description = "{} The question cannot be longer than 200 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = ":grey_question: `Question`:\n**{}**: {}\n\n:8ball: `Answer`:\n**{}**: {}".format(ctx.message.author.name, args, client.user.name, random.choice(eb))
            await client.say(embed=embed)
            
# }pfp
@client.command(pass_context=True)
async def pfp(ctx):
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
        try:
            a = []
            for i in client.servers:
                a.append(i.id)
            server = client.get_server(random.choice(a))
            b = []
            for i in server.members:
                if not i.bot:
                    b.append(i.id)
            user = await client.get_user_info(random.choice(b))
            embed.description = "Here is **{}**'s profile picture, I found it from **{}**.".format(user.name, server.name)
            embed.set_image(url=user.avatar_url)
            await client.say(embed=embed)
        except:
            embed.description = "{} An unknown error occurred.".format(error_e)
            await client.say(embed=embed)
            
# }calculator <math problem>
@client.command(pass_context=True)
async def calculator(ctx, *, args = None):
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
        if args == None:
            embed.description = "{} Please give a simple math problem for me to solve.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 100:
            embed.description = "{} The math problem cannot be longer than 100 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                embed.description = "{} Problem: `{}`\n{} Answer: `{}`".format(calculator_e, args, calculator_e, eval(args))
                await client.say(embed=embed)
            except:
                embed.description = "{} I'm having trouble solving that math problem.".format(error_e)
                await client.say(embed=embed)
                  
# }battle <user>
@client.command(pass_context=True)
async def battle(ctx, user: discord.Member = None):
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
        if user == None:
            embed.description = "{} Please mention the user you want to battle.".format(error_e)
            await client.say(embed=embed)
        elif user.id == ctx.message.author.id:
            embed.description = "{} You can't battle yourself.".format(error_e)
            await client.say(embed=embed)
        else:
            author = ctx.message.author
            u_health = []
            a_health = []
            rounds = []
            for i in range(1000):
                a_health.append(".")
                u_health.append(".")
            dmgs = {"punches the opponent! :right_facing_fist:" : random.randint(50, 70),
                    "kicks the opponent! :boot:" : random.randint(55, 75),
                    "grabs and throws the opponent on the ground! :raised_hands:" : random.randint(65, 85),
                    "stabs the opponent! :dagger:" : random.randint(75, 95),
                    "shoots the opponent! :gun:" : random.randint(90, 110),
                    "cuts the opponent! :knife:" : random.randint(65, 85),
                    "hits the opponent with a hammer! :hammer_pick:" : random.randint(75, 95),
                    "attacks the opponent with dark magic! :skull_crossbones:" : random.randint(280, 300),
                    "chokes the opponent using chains! :chains:" : random.randint(65, 85),
                    "casts a spell on the opponent! :sparkles:" : random.randint(155, 175),
                    "pukes on the opponent! :nauseated_face:" : random.randint(50, 70),
                    "scares the opponent! :ghost:" : random.randint(50, 70),
                    "summons a demon to attack the opponent! :smiling_imp:" : random.randint(275, 295),
                    "calls a rabot to attack the opponent! :robot:" : random.randint(125, 145),
                    "farts at the opponent! :dash:" : random.randint(50, 70),
                    "creates a tornado behind the opponent! :cloud_tornado:" : random.randint(130, 150),
                    "summons a meteor above the opponent! :comet:" : random.randint(210, 230),
                    "strikes the opponent with lightning! :zap:" : random.randint(200, 220),
                    "freezes the opponent! :snowflake:" : random.randint(140, 160),
                    "throws a bomb at the opponent! :bomb:" : random.randint(150, 170),
                    "drives over the opponent! :red_car:" : random.randint(110, 130),
                    "stuns the opponent! :dizzy:" : random.randint(60, 80),
                    "uses ear-rape to deafen the opponent! :ear:" : random.randint(50, 70),
                    "poisons the opponent! :syringe:" : random.randint(200, 220),
                    "set the opponent on fire! :fire:" : random.randint(170, 190),
                    "made the opponent not feel so good! :boom:" : random.randint(225, 245),
                    "stole the opponent's memes! :100:" : 420,
                    "deleted the opponent's hentai collections! :no_entry:" : 69,
                    "banned the opponent's memes! :no_entry_sign:" : random.randint(55, 75),
                    "pushed the opponent in the toilet! :toilet:" : 1}
            attacks = ["punches the opponent! :right_facing_fist:",
                       "kicks the opponent! :boot:",
                       "grabs and throws the opponent on the ground! :raised_hands:",
                       "stabs the opponent! :dagger:",
                       "shoots the opponent! :gun:",
                       "cuts the opponent! :knife:",
                       "hits the opponent with a hammer! :hammer_pick:",
                       "attacks the opponent with dark magic! :skull_crossbones:",
                       "chokes the opponent using chains! :chains:",
                       "casts a spell on the opponent! :sparkles:",
                       "pukes on the opponent! :nauseated_face:",
                       "scares the opponent! :ghost:",
                       "summons a demon to attack the opponent! :smiling_imp:",
                       "calls a rabot to attack the opponent! :robot:",
                       "farts at the opponent! :dash:",
                       "creates a tornado behind the opponent! :cloud_tornado:",
                       "summons a meteor above the opponent! :comet:",
                       "strikes the opponent with lightning! :zap:",
                       "freezes the opponent! :snowflake:",
                       "throws a bomb at the opponent! :bomb:",
                       "drives over the opponent! :red_car:",
                       "stuns the opponent! :dizzy:",
                       "uses ear-rape to deafen the opponent! :ear:",
                       "poisons the opponent! :syringe:",
                       "set the opponent on fire! :fire:",
                       "made the opponent not feel so good! :boom:",
                       "stole the opponent's memes! :100:",
                       "deleted the opponent's hentai collections! :no_entry:",
                       "banned the opponent's memes! :no_entry_sign:",
                       "pushed the opponent in the toilet! :toilet:"]
            title = "{} **__`D E A T H    B A T T L E`__** {}\n**{}**\n:vs:\n**{}**".format(battle_e, battle_e, author.name, user.name)
            s = "**~~`=====`~~**"
            embed.description = "{}\n{} **HEALTH** {}\n:small_red_triangle_down: **{}**\n:heart: `1000` HP\n\n:small_red_triangle_down: **{}**\n:heart: `1000` HP".format(title, s, s, author.name, user.name)
            h = await client.say(embed=embed)
            for i in range(1000):
                if len(a_health) == 0 or len(u_health) == 0:
                    await asyncio.sleep(float(5))
                    if len(a_health) > len(u_health):
                        embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: WINNER: **{}**\n:heart: `{}` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, author.name, len(a_health), user.name)
                    elif len(a_health) < len(u_health):
                        embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: WINNER: **{}**\n:heart: `{}` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, user.name, len(u_health), author.name)
                    else:
                        p = random.randint(0, 1)
                        if p == 0:
                            embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: RANDOM WINNER: **{}**\n:heart: `0` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, author.name, user.name)
                        else:
                            embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: RANDOM WINNER: **{}**\n:heart: `0` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, user.name, author.name)
                    await client.edit_message(h, embed=embed)
                    break
                else:
                    await asyncio.sleep(float(5))
                    rounds.append("+1")
                    u_d = random.choice(attacks)
                    a_d = random.choice(attacks)
                    for u in range(dmgs[u_d]):
                        if len(a_health) != 0:
                            a_health.remove('.')
                    for u in range(dmgs[a_d]):
                        if len(u_health) != 0:
                            u_health.remove('.')
                    embed.description = "{}\n{} **ROUND {}** {}\n:small_red_triangle_down: **{}** {}\n:arrow_right: `{}` DMG\n\n:small_red_triangle_down: **{}** {}\n:arrow_right: `{}` DMG\n{} **HEALTH** {}\n:small_red_triangle_down: **{}**\n:heart: `{}` HP\n\n:small_red_triangle_down: **{}**\n:heart: `{}` HP".format(title, s, len(rounds), s, author.name, a_d, dmgs[a_d], user.name, u_d, dmgs[u_d], s, s, author.name, len(a_health), user.name, len(u_health))
                    await client.edit_message(h, embed=embed)
                        
# }ship <something> , <something else>
@client.command(pass_context=True)
async def ship(ctx, *, args = None):
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
        if args == None or ', ' not in str(args):
            embed.description = "{} The command was used incorrectly.\nProper usage: `<something>, <something else>`.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The ship cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            a = args.split(', ')
            if len(a) != 2:
                embed.description = "{} The command was used incorrectly.\nProper usage: `<something>, <something else>`.".format(error_e)
                await client.say(embed=embed)
            else:
                title = "{} **__`LOVELY SHIPPING MACHINE`__** {}".format(ship_e, ship_e)
                s = "**~~`=====`~~**"
                embed.description = "{}\n**{}**\n:heart: :yellow_heart: :green_heart: :blue_heart: :purple_heart:\n**{}**".format(title, a[0], a[1])
                h = await client.say(embed=embed)
                l = [":yellow_heart:", ":green_heart:", ":blue_heart:", ":purple_heart:", ":heart:"]
                for i in range(3):
                    await asyncio.sleep(float(1))
                    r = "{}{}{}{}{}{}{}{}{}{}".format(random.choice(l), random.choice(l), random.choice(l), random.choice(l), random.choice(l), random.choice(l), random.choice(l), random.choice(l), random.choice(l), random.choice(l))
                    embed.description = "{}\n**{}**\n{}\n**{}**\n{} **RESULTS** {}\n**__Loading...__**".format(title, a[0], r, a[1], s, s)
                    await client.edit_message(h, embed=embed)
                c = []
                for i in ships:
                    if a[0] in str(i) and a[1] in str(i):
                        b = i.split(', ')
                        p = int(b[2])
                        c.append("+1")
                        break
                if len(c) == 0:
                    p = random.randint(0, 101)
                    await client.send_message(client.get_channel(ships_chnl), "{}, {}, {}".format(a[0], a[1], p))
                    ships.append("{}, {}, {}".format(a[0], a[1], p))
                await asyncio.sleep(float(1))
                if p >= 0 and p <= 10:
                    embed.description = "{}\n**{}**\n:heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Shit :poop:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 11 and p <= 20:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Awful :sob:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 21 and p <= 30:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Very bad :pensive:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 31 and p <= 40:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Bad :frowning:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 41 and p <= 50:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Okay :neutral_face:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 51 and p <= 60:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Good :slight_smile:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 61 and p <= 70:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Very good :smiley:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 71 and p <= 80:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Fantastic :heart_eyes:__**".format(title, a[0], a[1], s, s, p)
                elif p >= 81 and p <= 90:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Amazing :sparkling_heart:__**".format(title, a[0], a[1], s, s, p)
                else:
                    embed.description = "{}\n**{}**\n:heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse::heartpulse:\n**{}**\n{} **RESULTS** {}\n**__`{}%` Perfect :revolving_hearts:__**".format(title, a[0], a[1], s, s, p)
                await client.edit_message(h, embed=embed)
            
# }rps <rock/paper/scissors>
@client.command(pass_context=True)
async def rps(ctx, choice = None):
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
        if choice == None:
            embed.description = "{} Please choose what you want to use.\nChoices: `rock`, `paper`, `scissors`.".format(error_e)
            await client.say(embed=embed)
        elif choice not in rps_choices:
            embed.description = "{} Invalid choice.\nChoices: `rock`, `paper`, `scissors`.".format(error_e)
            await client.say(embed=embed)
        else:
            a = random.choice(rps_choices)
            s = "**~~`=====`~~**"
            title = "{} **__`ROCK, PAPER, SCISSORS`__** {}\n**{}**\n:vs:\n**{}**\n{} **OVER** {}".format(game_e, game_e, ctx.message.author.name, client.user.name, s, s)
            if choice in rps_r and a in rps_s:
                embed.description = "{}\n:crown: WINNER: **{}**\n:arrow_right: `rock`\n\n:poop: LOSER: **{}**\n:arrow_right: `scissors`".format(title, ctx.message.author.name, client.user.name)
            elif choice in rps_p and a in rps_r:
                embed.description = "{}\n:crown: WINNER: **{}**\n:arrow_right: `paper`\n\n:poop: LOSER: **{}**\n:arrow_right: `rock`".format(title, ctx.message.author.name, client.user.name)
            elif choice in rps_s and a in rps_p:
                embed.description = "{}\n:crown: WINNER: **{}**\n:arrow_right: `scissors`\n\n:poop: LOSER: **{}**\n:arrow_right: `paper`".format(title, ctx.message.author.name, client.user.name)
            elif a in rps_r and choice in rps_s:
                embed.description = "{}\n:crown: WINNER: **{}**\n:arrow_right: `rock`\n\n:poop: LOSER: **{}**\n:arrow_right: `scissors`".format(title, client.user.name, ctx.message.author.name)
            elif a in rps_p and choice in rps_r:
                embed.description = "{}\n:crown: WINNER: **{}**\n:arrow_right: `paper`\n\n:poop: LOSER: **{}**\n:arrow_right: `rock`".format(title, client.user.name, ctx.message.author.name)
            elif a in rps_s and choice in rps_p:
                embed.description = "{}\n:crown: WINNER: **{}**\n:arrow_right: `scissors`\n\n:poop: LOSER: **{}**\n:arrow_right: `paper`".format(title, client.user.name, ctx.message.author.name)
            else:
                embed.description = "{}\n:no_entry:\n**{}**\n:arrow_right: `{}`\n\n**{}**\n:arrow_right: `{}`".format(title, ctx.message.author.name, rps_tie[choice], client.user.name, rps_tie[a])
            await client.say(embed=embed)
#######################
client.run(os.environ['BOT_TOKEN'])
