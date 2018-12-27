print("Starting Cube...")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

''''''

Client = discord.Client()
bot_prefix= ["px!", "Px!"]
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "Pixels"
limit = 10000000000000000
version = '1.0'
default_link = 'https://discord.gg/Xj6beq7'


mods = ['299761993382887425']
mods_chnl = '527410541191495680'
banned_users = []
banned_servers = []
ignored = []
currency_t = []
responses_t = []
currencies = []

hug_links = []
pat_links = []
kiss_links = []
nom_links = []
throw_links = []
bite_links = []
bloodsuck_links = []
cuddle_links = []
highfive_links = []
poke_links = []
slap_links = []
punch_links = []
stare_links = []
facepalm_links = []
lick_links = []
spank_links = []
cry_links = []
dance_links = []
bow_links = []
dab_links = []

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

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

revivals = []
nhie_msgs = []
wyr_msgs = []
marriages = []
dicks = []
howgays = []
ships = []
rates = []
balances = []

con_messages = []
con_wait = []
slots_wait = []
worked = []
stole = []

responses_msgs = {"good bot" : ["C:", "yey me good botty", "I'm not your dog, human.", "uwu"],
             "bad bot" : [";c", "so sad", "I'm not your fucking dog.", "much cri"],
             "fun" : ["fun?", "fun.", "fun!", "( ͡° ͜ʖ ͡°)"],
             "ayy" : ["lmao", "ayy bro", "aye"],
             "lol" : ["hahaha", "lmao", "xD", "lol"],
             "hi" : ["hello", "haalloo", "hey", "hi, how you doing?"],
             "whalecum" : ["stop saying that shit", "c r i n g e", ">.>", "(╯°□°）╯︵ ┻━┻", "just why", "fucking pervert"],
             "fuck you" : ["well fuck you right back", ":(", "so rude"],
             "fuck" : ["you", "me", "us", "everyone"],
             "heck" : ["no swearing on this christian server", "ban this filth", ">:C"],
             "ok" : ["ok", "yes", "not ok", "k"],
             "cool" : ["cool cool", "cool indeed"],
             "spook" : ["sp00k3d"],
             "zero" : ["zero is actually a girl", "zero should really take a shower", "zero's ass is flatter than earth", "aint zero gay?"],
             "yas" : ["fucking hell that was cringy as shit", "...", ">.>", "yass moist fam"],
             "owo" : ["OWO", "OwO", "uwu", "UwU"],
             "bitch" : ["betch", "benches be benching", "*bench*"],
             "nigga" : ["YOU CAN'T SAY THAT, IT'S RACIST", "ni:b::b:a", "gigga nigga"],
             "same" : ["same", "me too"],
             "welcome" : ["welcome", "welcome, have fun", "enjoy your stay", "heyo, welcome to this beautiful server"],
             "bye" : ["no wait ;-; come back", "cyah", "goodnight", "bai"],
             "jk" : ["its joke", "syke its just a prank", "lol", "xd"],
             "no u" : ["yesn't u", "no us", "no no u", "aint you"],
             "rip" : ["gg", "f"]}


banned_users_chnl = '527769371292991500'
banned_servers_chnl = '527769888735887360'
log_chnl = '527769404893691924'
tickets_chnl = '527769434190774272'
dicks_chnl = '527769459008733184'
balances_chnl = '527769484308643850'
marriages_chnl = '527769509164220416'
gays_chnl = '527769532354527253'
ships_chnl = '527769555075072000'
wyr_chnl = '527769574716997632'
nhie_chnl = '527769594975354901'
revivals_chnl = '527769624595660800'
interactions_chnl = '527769649400643600'
ignored_chnl = '527769671655620609'
currency_t_chnl = '527769697824014336'
responses_t_chnl = '527769725942366208'
rates_chnl = '527769744439508995'

staff_role = '504702557428383754'
splitter = "**~~`====================`~~**"

loading_e = ":arrows_counterclockwise: "
slotsgif1_e = "<a:slotsgif1:519832184039669760>"
slotsgif2_e = "<a:slotsgif2:519832184622940160>"
slotsgif3_e = "<a:slotsgif3:519832184383733761>"
slotsgif4_e = "<a:slotsgif4:519832184123686922>"
error_e = ":x:"
bug_e = ":bug: "
close_e = ":heavy_multiplication_x: "
log_e = ":newspaper2: "
msg_e = ":bow: "
noperms_e = "<:x:"
pingbad_e = ":beginner: "
pinggood_e = ":beginner: "
pingok_e = ":beginner: "
reload_e = ":arrows_counterclockwise:"
servers_e = ":shield: "
support_e = ":shield: "
users_e = ":grinning: "
worked_e = ":black_heart:"
check_e = ":white_check_mark: "
interactions_e = ":tada: "
game_e = ":video_game: "
battle_e = ":crossed_swords: "
messages_e = ":comet: "
bannedservers_e = ":no_entry_sign: "
bannedusers_e = ":no_entry: "
cointoss_e = ":heavy_dollar_sign: "
suicide_e = ":skull: "
roast_e = ":fire: "
calculator_e = ":1234: "
ship_e = ":sparkles: "
kill_e = ":gun: "
rate_e = ":100: "
dicklength_e = ":eggplant: "
howgay_e = ":gay_pride_flag: "
suggestion_e = ":bulb: "
coins_e = ":gem: "
divorce_e = ":broken_heart: "
marriage_e = ":heart: "
convert_e = ":recycle: "
slots_e = ":slot_machine: "
on_e = ":black_square_button: "
off_e = ":black_large_square:  "
ignored_e = ":no_entry_sign: "
work_e = ":dollar: "
generator_e = ":bulb: "
steal_e = ":bust_in_silhouette: "
gift_e = ":gift: "
ban_e = ":wave: "
link_e = ":link: "


help1 = "```diff"
help1 += "\n--- COMMANDS FOR EVERYONE ---"
help1 += "\npx!help"
help1 += "\n-    Gives you a list of commands."
help1 += "\npx!ping"
help1 += "\n-    Pings the bot. Used to check if the bot is lagging."
help1 += "\npx!tos"
help1 += "\n-    Gives you the bot's TOS and rules."
help1 += "\npx!invite"
help1 += "\n-    Gives you invite links for the bot."
help1 += "\npx!features"
help1 += "\n-    Shows a list of features."
help1 += "\npx!support <text>"
help1 += "\n-    Sends a support ticket to the bot staff."
help1 += "\npx!bug <text>"
help1 += "\n-    Sends a bug report ticket to the bot staff."
help1 += "\npx!info"
help1 += "\n-    Shows information about the bot."
help1 += "\npx!stats"
help1 += "\n-    Shows the bot's statistics."
help1 += "\npx!suggest <text>"
help1 += "\n-    Sends a suggestion to the bot staff."
help1 += "\npx!serverinfo"
help1 += "\n-    Shows information about the server."
help1 += "\npx!cointoss"
help1 += "\n-    Flips a coin."
help1 += "\npx!suicide"
help1 += "\n-    Use this to commit suicide."
help1 += "\npx!roast <user>"
help1 += "\n-    Roasts the mentioned user."
help1 += "\npx!eightball <yes/no question>"
help1 += "\n-    Answers yes-no questions."
help1 += "\npx!pfp"
help1 += "\n-    Gives you a random user's profile picture."
help1 += "\npx!calculator <math problem>"
help1 += "\n-    Solves simple math problems."
help1 += "\npx!battle <user>"
help1 += "\n-    Use this to fight someone."
help1 += "\npx!ship <something> | <something else>"
help1 += "\n-    Makes lovely ships."
help1 += "\npx!rps <rock/paper/scissors>"
help1 += "\n-    Use this to play rock, paper, scissors with the bot."
help1 += "\npx!kill <user>"
help1 += "\n-    Use this to kill someone."
help1 += "\nxf!leave"
help1 += "\n-    Creates a fake leave message."
help1 += "\npx!join"
help1 += "\n-    Creates a fake join message."
help1 += "\npx!rate <something>"
help1 += "\n-    Rates stuff."
help1 += "\nxf!dicklength [user]"
help1 += "\n-    Tells you the length of someone's dick even if they don't have one."
help1 += "\nxf!howgay <user>"
help1 += "\n-    Tells you how gay someone is."
help1 += "\nxf!chatrevive"
help1 += "\n-    Sends a random conversation starter as an atempt to revive the chat."
help1 += "\nxf!nhie"
help1 += "\n-    Tells a random 'never have i ever' sentence."
help1 += "\npx!wyr"
help1 += "\n-    Tells a random 'would you rather' sentence."
help1 += "\npx!lettergen <number of letters>"
help1 += "\n-    Generates the specified amout of random letters."
help1 += "\nxf!numbergen <minimum number> <maximum number>"
help1 += "\n-    Generates random numbers."
help1 += "\npx!ban <text>"
help1 += "\n-    Creates a fake ban message."
help1 += "\n```"

help2 = "```diff"
help2 += "\n--- INTERACTION COMMANDS FOR EVERYONE ---"
help2 += "\npx!hug <user>"
help2 += "\n-    Hugs the mentioned user."
help2 += "\npx!kiss <user>"
help2 += "\n-    Kisses the mentioned user."
help2 += "\nxf!pat <user>"
help2 += "\n-    Pats the mentioned user."
help2 += "\npx!punch <user>"
help2 += "\n-    Punches the mentioned user."
help2 += "\nxf!cuddle <user>"
help2 += "\n-    Cuddles the mentioned user."
help2 += "\npx!bite <user>"
help2 += "\n-    Bites the mentioned user."
help2 += "\npx!bloodsuck <user>"
help2 += "\n-    Sucks blood from the mentioned user."
help2 += "\npx!throw <user>"
help2 += "\n-    Throws the mentioned user."
help2 += "\npx!nom <user>"
help2 += "\n-    Noms the mentioned user."
help2 += "\npx!highfive <user>"
help2 += "\n-    Highfives the mentioned user."
help2 += "\npx!poke <user>"
help2 += "\n-    Pokes the mentioned user."
help2 += "\npx!slap <user>"
help2 += "\n-    Slaps the mentioned user."
help2 += "\npx!stare <user>"
help2 += "\n-    Stares at the mentioned user."
help2 += "\npx!spank <user>"
help2 += "\n-    Spanks the mentioned user."
help2 += "\npx!lick <user>"
help2 += "\n-    Licks the mentioned user."
help2 += "\npx!facepalm"
help2 += "\n-    Use this when someone says something stupid."
help2 += "\npx!cry"
help2 += "\n-    Use this when you want to cry."
help2 += "\npx!dance"
help2 += "\n-    Use this to dance."
help2 += "\npx!bow"
help2 += "\n-    Use this to show respect."
help2 += "\npx!dab"
help2 += "\n-    Use this to dab."
help2 += "```"

help3 = "```diff"
help3 += "\n--- CURRENCY COMMANDS ---"
help3 += "\npx!convert"
help3 += "\n-    Converts your sent messages into coins."
help3 += "\npx!marry <user>"
help3 += "\n-    Use this to marry someone."
help3 += "\npx!divorce"
help3 += "\n-    Use this to divorce."
help3 += "\npx!ma"
help3 += "\n-    Accepts a marriage request."
help3 += "\npx!md"
help3 += "\n-    Denies a marriage request."
help3 += "\npx!profile [user]"
help3 += "\n-    Shows user profiles."
help3 += "\npx!bal [user]"
help3 += "\n-    Shows your's or the mentioned user's balance."
help3 += "\npx!slots <number>"
help3 += "\n-    Use this to gamble your money."
help3 += "\npx!work"
help3 += "\n-    Gives you some coins. Can be used once every 2 hours."
help3 += "\npx!steal <user>"
help3 += "\n-    Steals coins from the mentioned user. Can be used once every 2 hours."
help3 += "\npx!gift <user> <amount>"
help3 += "\n-    Gives the specified amount of coins to the mentioned user."
help3 += "\n```"

help4 = "```diff"
help4 += "\n--- COMMANDS FOR CO OWNERS ---"
help4 += "\npx!responses"
help4 += "\n-    Toggles the bot's automatic responses."
help4 += "\npx!currency"
help4 += "\n-    Toggles the bot's currency features."
help4 += "\npx!ignore <channel name>"
help4 += "\n-    Ignores/unignores a channel. Messages from ignored channels will not trigger responses and will not reward coins."
help4 += "\n```"

help5 = "```diff"
help5 += "\n--- COMMANDS FOR BOT MODERATORS ---"
help5 += "\npx!umsg <user ID> <text>"
help5 += "\n-    Sends a message to a user."
help5 += "\npx!smsg <server ID> <text>"
help5 += "\n-    Sends a message to a server owner."
help5 += "\npx!close <ticket number>"
help5 += "\n-    Closes a ticket."
help5 += "\npx!link <server ID>"
help5 += "\n-    Gets an invite link to a server."
help5 += "\n"
help5 += "\n--- COMMANDS FOR BOT OWNER ---"
help5 += "\npx!mod <user ID>"
help5 += "\n-    Adds/removes a user to/from the mods list."
help5 += "\npx!say <text>"
help5 += "\n-    Forces the bot to say something,"
help5 += "\n```"

tos_m = "\n{} **__Bot rules:__**".format(error_e)
tos_m += "\n"
tos_m += "\n{} Spamming the bot's commands or making the bot lag will get you instantly banned.".format(check_e)
tos_m += "\n{} Continuous asking to become a bot moderator is not allowed.".format(check_e)
tos_m += "\n{} Raiding, spamming, nuking and similar acts will get you banned.".format(check_e)
tos_m += "\n{} Sending NSFW or gore files/links in non-NSFW channels will get you banned.".format(check_e)
tos_m += "\n{} Making drama about the bot, stealing the bot's code, sending viruses or any kind of malicious files/links will get you banned.".format(check_e)
tos_m += "\n{} Do not mess with the support, report and suggestion systems.".format(check_e)
tos_m += "\n{} Only suggest things that can actually improve the bot.".format(check_e)
tos_m += "\n{} Do not take advantage of bugs. Please report them instead.".format(check_e)
tos_m += "\n"
tos_m += "\n"
tos_m += "\n{} Thanks for using this bot. Use `xf!info` for more information and `xf!features` to see the bot's features.".format(worked_e)

''''''

started = ["1"]
# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(banned_users_chnl), limit=limit):
        a = i.content.split(' | ')
        banned_users.append(a[0])
    print("[START UP] Loaded banned users.")
    async for i in client.logs_from(client.get_channel(banned_servers_chnl), limit=limit):
        a = i.content.split(' | ')
        banned_servers.append(a[0])
    print("[START UP] Loaded banned servers.")
    async for i in client.logs_from(client.get_channel(wyr_chnl), limit=limit):
        wyr_msgs.append(i.content)
    print("[START UP] Loaded 'would you rather' messages.")
    async for i in client.logs_from(client.get_channel(nhie_chnl), limit=limit):
        nhie_msgs.append(i.content)
    print("[START UP] Loaded 'never have I ever' messages.")
    async for i in client.logs_from(client.get_channel(revivals_chnl), limit=limit):
        revivals.append(i.content)
    print("[START UP] Loaded chat revivals.")
    async for i in client.logs_from(client.get_channel(marriages_chnl), limit=limit):
        marriages.append(i.content)
    print("[START UP] Loaded marriages.")
    async for i in client.logs_from(client.get_channel(dicks_chnl), limit=limit):
        dicks.append(i.content)
    print("[START UP] Loaded dick lengths.")
    async for i in client.logs_from(client.get_channel(gays_chnl), limit=limit):
        howgays.append(i.content)
    print("[START UP] Loaded how-gays.")
    async for i in client.logs_from(client.get_channel(ships_chnl), limit=limit):
        ships.append(i.content)
    print("[START UP] Loaded ships.")
    async for i in client.logs_from(client.get_channel(rates_chnl), limit=limit):
        rates.append(i.content)
    print("[START UP] Loaded rates.")
    async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
        a = i.content.split(' | ')
        balances.append(a[0])
    print("[START UP] Loaded balances.")
    interaction_sys = {"hug" : hug_links,
                       "kiss" : kiss_links,
                       "pat" : pat_links,
                       "slap" : slap_links,
                       "punch" : punch_links,
                       "cuddle" : cuddle_links,
                       "bloodsuck" : bloodsuck_links,
                       "bite" : bite_links,
                       "bow" : bow_links,
                       "dance" : dance_links,
                       "dab" : dab_links,
                       "nom" : nom_links,
                       "throw" : throw_links,
                       "highfive" : highfive_links,
                       "poke" : poke_links,
                       "stare" : stare_links,
                       "spank" : spank_links,
                       "lick" : lick_links,
                       "facepalm" : facepalm_links,
                       "cry" : cry_links}
    interactions_total = []
    async for i in client.logs_from(client.get_channel(interactions_chnl), limit=limit):
        a = i.content.split(' | ')
        interaction_sys[a[0]].append(a[1])
        interactions_total.append("+1")
    print("[START UP] Loaded interactions.")
    async for i in client.logs_from(client.get_channel(ignored_chnl), limit=limit):
        ignored.append(i.content)
    print("[START UP] Loaded ignored channels.")
    async for i in client.logs_from(client.get_channel(currency_t_chnl), limit=limit):
        currency_t.append(i.content)
    print("[START UP] Loaded currency toggles.")
    async for i in client.logs_from(client.get_channel(responses_t_chnl), limit=limit):
        responses_t.append(i.content)
    print("[START UP] Loaded responses toggles.")
    async for i in client.logs_from(client.get_channel(mods_chnl), limit=limit):
        mods.append(i.content)
    print("[START UP] Loaded mods.")
    started.append("+1")
    print("[START UP] Finished.")
    await client.change_presence(game=discord.Game(name="xf!help | xf!invite | xf!support | Running DEV version."))
    m = splitter
    m += "\n{} **__Bot Restart__** {} `-` Version: {}".format(log_e, reload_e, version)
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel(log_chnl))
    t2 = time.perf_counter()
    m += "\n{} Ping: `{}ms`".format(pingok_e, round((t2-t1)*1000))
    await client.send_message(client.get_channel(log_chnl), m)

# CURRENCY SYSTEM / AUTO-RESPONSES
@client.event
async def on_message(msg):
    if len(started) != 0:
        if msg.channel.id not in ignored and not msg.author.bot:
            con_messages.append(msg.author.id)
            if msg.author.id not in balances:
                await client.send_message(client.get_channel(balances_chnl), "{} | 0".format(msg.author.id))
                balances.append(msg.author.id)
            if msg.content.lower() in responses_msgs and msg.server.id not in responses_t:
                p = random.randint(0, 1)
                if p == 0:
                    await client.send_message(msg.channel, random.choice(responses_msgs[msg.content.lower()]))
    await client.process_commands(msg)

''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=0x0)
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
        try:
            await client.send_message(ctx.message.author, help1)
            await client.send_message(ctx.message.author, help2)
            await client.send_message(ctx.message.author, help3)
            await client.send_message(ctx.message.author, help4)
            if ctx.message.author.id in mods:
                await client.send_message(ctx.message.author, help5)
            embed.description = "{} A list of commands has been sent to your DMs.".format(worked_e)
            await client.say(embed=embed)
        except:
            embed.description = "{} I was unable to DM you my list of commands.".format(error_e)
            await client.say(embed=embed)

# }ping
@client.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(colour=0x00)
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
    elif '}ping f' in str(ctx.message.content) or '}ping all' in str(ctx.message.content) or '}' not in str(ctx.message.content):
        t1 = time.perf_counter()
        await client.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        ping = round((t2-t1)*1000)
        if ping > 300:
            m = "{} The bot is lagging.\nAttempting to fix the bot's ping. This should take about a minute to finish.".format(pingbad_e)
        elif ping > 200:
            m = "{} The bot might be lagging.".format(pingok_e)
        else:
            m = "{} The bot isn't lagging.".format(pinggood_e)
        embed.description = "My ping is `{}ms`.\n{}".format(ping, m)
        await client.say(embed=embed)

# }tos
@client.command(pass_context=True)
async def tos(ctx):
    embed = discord.Embed(colour=0x00)
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
        embed.description = tos_m
        await client.say(embed=embed)

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(colour=0x00)
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
        m = ":link: [Click here](https://discordapp.com/oauth2/authorize?client_id=453210408384462848&scope=bot&permissions=8) to invite the bot."
        m += "\n"
        m += "\n{} [Click here]({}) to join the support server where you can find all information about the bot.".format(support_e, default_link)
        embed.description = m
        await client.say(embed=embed)

# }features
@client.command(pass_context=True)
async def features(ctx):
    embed = discord.Embed(colour=0x00)
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
        embed.description = ":scroll: **__BOT FEATURES__**\n[Join the support server]({}) to find more information about each of these features.".format(default_link)
        embed.add_field(name="{} SUPPORT TEAM:".format(support_e), value="The bot has its own support team which will help you whatever issues you have with the bot and answer all your questions about it.", inline=True)
        embed.add_field(name="{} INTERACTIONS:".format(interactions_e), value="The bot has lots of commands that let you interact with other users thru this bot.", inline=True)
        embed.add_field(name="{} DEATH BATTLES:".format(battle_e), value="This feature allows you to battle other users to the death. It uses randomized systems.", inline=True)
        embed.add_field(name="{} FUN MINI-GAMES:".format(game_e), value="Allows you to play a few fun mini-games like 'Would you rather', 'Never have I ever' and more.", inline=True)
        embed.add_field(name="{} CHAT REVIVER:".format(messages_e), value="Conversations can end pretty quickly, especially if the people in it don't have anything interesting to say. That's why the bot will try to keep the chat alive by telling some interesting, funny and sometimes random conversation starters.", inline=True)
        embed.add_field(name="{} CURRENCY SYSTEM:".format(coins_e), value="The bot has a currency system based on chat activity. It has a gambling command as well.", inline=True)
        embed.add_field(name="{} MARRIAGES:".format(marriage_e), value="You can use the money from the currency system to marry someone you love.", inline=True)
        embed.add_field(name="{} SUGGESTIONS SYSTEM:".format(suggestion_e), value="Allows you to send suggestions and ideas to help us improve the bot and make it even more entertaining.", inline=True)
        embed.add_field(name="{} IGNORED CHANNELS:".format(ignored_e), value="Allows server managers to ignore channels so users can't spam and get lots of money. Ignored channels also ignore the bot's response triggers.", inline=True)
        embed.add_field(name="{} TOGGLES:".format(log_e), value="This feature allows server managers to toggle some of the features like the currency system and responses.", inline=True)
        embed.add_field(name="{} RESPONSES:".format(messages_e), value="The bot will sometimes reply to someone if they say a specific word in chat.", inline=True)
        embed.add_field(name="{} PLANNED FEATURES:".format(msg_e), value="One feature that we plan to add in the future is a shop feature that will let you buy things like banners, perks, pets and more stuff with the currency system.", inline=True)
        await client.say(embed=embed)

# }support <text>
@client.command(pass_context=True)
async def support(ctx, *, args = None):
    embed = discord.Embed(colour=0x00)
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
        if args == None:
            embed.description = "{} No text given.\nYou can also just join the support server and ask for help there. [Click here]({}) to join the support server.".format(error_e, default_link)
            await client.say(embed=embed)
        elif len(str(args)) > 500:
            embed.description = "{} The text cannot be longer than 500 characters.\nYou can also just join the support server and ask for help there. [Click here]({}) to join the support server.".format(error_e, default_link)
            await client.say(embed=embed)
        else:
            embed.description = "{} Sending support ticket... {}".format(support_e, loading_e)
            h = await client.say(embed=embed)
            k = await client.send_message(client.get_channel(tickets_chnl), "<@&{}> new support ticket incoming...".format(staff_role))
            m = "{} **__Support Ticket__** `{}`".format(support_e, k.id)
            m += "\n:small_red_triangle_down: :label: "
            m += "\n`SENT BY:` {} ### {}".format(ctx.message.author, ctx.message.author.id)
            m += "\n:small_red_triangle_down: :map: "
            m += "\n`FROM:` {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
            m += "\n:small_red_triangle_down: :speech_balloon: "
            m += "\n`TEXT:` {}".format(args)
            embed.description = m
            await client.edit_message(k, "<@&{}>".format(staff_role), embed=embed)
            embed.description = "{} Support ticket sent!\nThe staff will contact you as soon as possible.".format(worked_e)
            await client.edit_message(h, embed=embed)

# }bug <text>
@client.command(pass_context=True)
async def bug(ctx, *, args = None):
    embed = discord.Embed(colour=0x00)
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
        if args == None:
            embed.description = "{} No text given.\nYou can also just join the support server and report the bug there. [Click here]({}) to join the support server.".format(error_e, default_link)
            await client.say(embed=embed)
        elif len(str(args)) > 500:
            embed.description = "{} The text cannot be longer than 500 characters.\nYou can also just join the support server and report the bug there. [Click here]({}) to join the support server.".format(error_e, default_link)
            await client.say(embed=embed)
        else:
            embed.description = "{} Sending bug report ticket... {}".format(bug_e, loading_e)
            h = await client.say(embed=embed)
            k = await client.send_message(client.get_channel(tickets_chnl), "<@&{}> new bug report ticket incoming...".format(staff_role))
            m = "{} **__Bug Report Ticket__** `{}`".format(bug_e, k.id)
            m += "\n:small_red_triangle_down: :label: "
            m += "\n`SENT BY:` {} ### {}".format(ctx.message.author, ctx.message.author.id)
            m += "\n:small_red_triangle_down: :map: "
            m += "\n`FROM:` {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
            m += "\n:small_red_triangle_down: :speech_balloon: "
            m += "\n`TEXT:` {}".format(args)
            embed.description = m
            await client.edit_message(k, "<@&{}>".format(staff_role), embed=embed)
            embed.description = "{} Bug report ticket sent!\nThe bot's administrators will look into it and contact you as soon as possible.".format(worked_e)
            await client.edit_message(h, embed=embed)

# }info
@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(colour=0x00)
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
        m = ":clipboard: **__BOT INFORMATION__**"
        m += "\n"
        m += "\n{} Version `{}`".format(reload_e, version)
        m += "\n{} Prefix `xf!`".format(check_e)
        embed.description = m
        a = []
        for i in client.servers:
            for o in range(len(i.members)):
                a.append("+1")
        embed.add_field(name="{} DESCRIPTION:".format(log_e), value="{} This bot is made for fun and entertainment. It's main purpose is to keep your server alive and make it more enjoyable for others.".format(log_e), inline=True)
        embed.add_field(name="{} SERVERS:".format(servers_e), value="{} `{}`".format(servers_e, len(client.servers)), inline=True)
        embed.add_field(name="{} USERS:".format(users_e), value="{} `{}`".format(users_e, len(a)), inline=True)
        embed.add_field(name="{} MODERATORS:".format(kill_e), value="{} `{}`".format(kill_e, len(mods)), inline=True)
        embed.add_field(name="{} BOT INVITE:".format(ignored_e), value="{} [click here](https://discordapp.com/oauth2/authorize?client_id=453210408384462848&scope=bot&permissions=8)".format(ignored_e), inline=True)
        embed.add_field(name="{} SUPPORT SERVER:".format(support_e), value="{} [click here]({})".format(support_e, default_link), inline=True)
        embed.add_field(name="{} FEATURES:".format(msg_e), value="{} Use `xf!features`".format(msg_e), inline=True)
        embed.add_field(name="{} STATISTICS:".format(slots_e), value="{} Use `xf!stats`".format(slots_e), inline=True)
        embed.add_field(name=":label: MADE BY:", value=":label: `Realm ✘`", inline=True)
        embed.add_field(name="**~~==========~~**", value="**~~==========~~**", inline=True)
        await client.say(embed=embed)

# }stats
@client.command(pass_context=True)
async def stats(ctx):
    embed = discord.Embed(colour=0x00)
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
        embed.description = "{} Loading statistics...".format(loading_e)
        h = await client.say(embed=embed)
        m = ":bar_chart: **__BOT STATISTICS__**"
        m += "\n"
        m += "\n{} Version `{}`".format(reload_e, version)
        m += "\n{} Prefix `xf!`".format(check_e)
        m += "\n"
        m += "\n{} SERVERS: `{}`".format(servers_e, len(client.servers))
        a = []
        for i in client.servers:
            for o in range(len(i.members)):
                a.append("+1")
        m += "\n{} USERS: `{}`".format(users_e, len(a))
        m += "\n{} BALANCES: `{}`".format(coins_e, len(balances))
        m += "\n{} MARRIAGES: `{}`".format(marriage_e, len(marriages))
        m += "\n{} DICK LENGTHS: `{}`".format(dicklength_e, len(dicks))
        m += "\n{} HOW-GAYS: `{}`".format(howgay_e, len(howgays))
        m += "\n{} RATES: `{}`".format(rate_e, len(rates))
        m += "\n{} SHIPS: `{}`".format(ship_e, len(ships))
        m += "\n{} WYR MESSAGES: `{}`".format(messages_e, len(wyr_msgs))
        m += "\n{} NHIE MESSAGES: `{}`".format(messages_e, len(nhie_msgs))
        m += "\n{} CHAT REVIVALS: `{}`".format(suggestion_e, len(revivals))
        c = []
        async for i in client.logs_from(client.get_channel(interactions_chnl), limit=limit):
            c.append("+1")
        m += "\n{} INTERACTIONS: `{}`".format(interactions_e, len(c))
        m += "\n{} IGNORED CHANNELS: `{}`".format(ignored_e, len(ignored))
        m += "\n{} CURRENCY TOGGLES: `{}`".format(on_e, len(currency_t))
        m += "\n{} RESPONSES TOGGLES: `{}`".format(off_e, len(responses_t))
        m += "\n{} MODERATORS: `{}`".format(kill_e, len(mods))
        embed.description = m
        await client.edit_message(h, embed=embed)

# }suggest <text>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    embed = discord.Embed(colour=0x00)
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
        if args == None:
            embed.description = "{} No text given.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The suggestion cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "{} {}\n**~~= = = = = = = = = = = = = = = = = = = =~~**\nSuggested by: `{} ### {}`\nIf you like this suggestion react with <:upvote:516253732955226114> and if you don't like it react with <:downvote:515909294479376414>.".format(suggestion_e, args, ctx.message.author, ctx.message.author.id)
            message = await client.send_message(client.get_channel('516575777974648835'), embed=embed)
            await client.add_reaction(message, ':downvote:515909294479376414')
            await client.add_reaction(message, ':upvote:516253732955226114')
            embed.description = "{} Suggestion sent! You can find it in the [support server]({}).".format(worked_e, default_link)
            await client.say(embed=embed)

# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(colour=0x00)
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

# }cointoss
@client.command(pass_context=True)
async def cointoss(ctx):
    embed = discord.Embed(colour=0x00)
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

# }suicide
@client.command(pass_context=True)
async def suicide(ctx):
    embed = discord.Embed(colour=0x00)
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

# }roast <user>
@client.command(pass_context=True)
async def roast(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
                    "**{}**, you remind me of Zero. Get out of here!".format(user.name),
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

# }eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args = None):
    embed = discord.Embed(colour=0x00)
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
    embed = discord.Embed(colour=0x00)
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
    embed = discord.Embed(colour=0x00)
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
    embed = discord.Embed(colour=0x00)
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

# }ship <something> | <something else>
@client.command(pass_context=True)
async def ship(ctx, *, args = None):
    embed = discord.Embed(colour=0x00)
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
        if args == None or ' | ' not in str(args):
            embed.description = "{} The command was used incorrectly.\nProper usage: `<something> | <something else>`.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The ship cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            a = args.split(' | ')
            if len(a) != 2:
                embed.description = "{} The command was used incorrectly.\nProper usage: `<something> | <something else>`.".format(error_e)
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
                        b = i.split(' | ')
                        p = int(b[2])
                        c.append("+1")
                        break
                if len(c) == 0:
                    p = random.randint(0, 101)
                    await client.send_message(client.get_channel(ships_chnl), "{} | {} | {}".format(a[0], a[1], p))
                    ships.append("{} | {} | {}".format(a[0], a[1], p))
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
    embed = discord.Embed(colour=0x00)
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

# }kill <user>
@client.command(pass_context=True)
async def kill(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
            embed.description = "{} Please mention the user you want to kill.".format(error_e)
            await client.say(embed=embed)
        else:
            author = ctx.message.author
            if user.id == client.user.id:
                embed.description = "**{}**, don't you try anything like that ever again, you fucking dirt bag.".format(author.name)
                await client.say(embed=embed)
            else:
                msgs = ["On a beautiful, sunny day, **{}**, went to the store. As they walked in to the store, they slipped and the doors cut off their head.".format(user.name),
                        "**{}** was sitting on a tree, but because of their weight the branch broke and they fell right on their head.".format(user.name),
                        "On a beautiful morning **{}** suddenly jumped out of bed and started running towards the bathroom. However, they slipped on a banana and fell out of the window.".format(user.name),
                        "**{}** watched the Emoji movie. The next day they died from cringing too much.".format(user.name),
                        "**{}** was browsing the web one day. They accidentaly clicked on a pop-up saying 'DIE FOR FREE!'.".format(user.name),
                        "**{}** got caught watching hentai. They had no choice but to kill themselves in order to wash away their sins.".format(user.name),
                        "All of **{}**'s memes got stolen! They couldn't live for more than 0.420 seconds without memes.".format(user.name),
                        "**{}** was walking down the village when all of a sudden a piano fell on top of them, crashing all their bones.".format(user.name),
                        "Long time ago **{}** lived in peace and harmony, until the fire nation attacked. Now **{}** is pretty much dead.".format(user.name, user.name),
                        "**{}** died a virgin. LMAO what a loser.".format(user.name),
                        "**{}** was playing hopscotch on a landmine field. You can tell how that went.".format(user.name),
                        "**{}** was playing the Sims. Their computer crashed and they got a heart attack.".format(user.name),
                        "Wait, **{}** died? Oh well.".format(user.name),
                        "**{}** commited suicide. I guess it's a way of saying 'You can't fire me! I quit!' to God.".format(user.name),
                        "**{}** gave their heart to **{}**... Literally.".format(user.name, author.name),
                        "**{}** decided to go on the moon. However they forgot their space suit. All the kids wanted to hear about the corpse on the moon...".format(user.name),
                        "One day **{}** was chilling with their friends. All of them were bored, they didn't have anything to do. One of them said 'So gentlemen, what do we do now?', **{}** replied: 'We die.'. Yeah, they were really bored.".format(user.name, user.name),
                        "**{}** tried to lay an egg. Humans can't do that, nor can bots!".format(user.name),
                        "All of **{}**'s diamonds were stolen on their Christian minecraft server. Out of anger they said 'heck' and got killed instantly.".format(user.name),
                        "**{}** forgot how to breathe.".format(user.name),
                        "**{}** saw **{}**'s face and instantly died.".format(user.name, author.name),
                        "**{}** said: Mr.**{}** I don't feel so good...".format(user.name, author.name),
                        "**{}** livedn't.".format(user.name),
                        "**{}** had a lot of mental disorders and couldn't live with them anymore. They commited suicide by cutting a deep wound on their chest with a kitchen knife.".format(user.name),
                        "**{}** drowned **{}** in a glass of water.".format(author.name, user.name),
                        "**{}** threw **{}** in a pool with sharks.".format(author.name, user.name),
                        "**{}** spammed **{}**'s DMs and they died from all the notifications they got.".format(author.name, user.name),
                        "**{}** stole all of **{}**'s chocolate. **{}** simply couldn't live without their chocolate and decided that their life is not worth living anymore.".format(author.name, user.name, user.name),
                        "**{}**'s toaster was hacked by **{}**. They couldn't live with no toast.".format(user.name, author.name),
                        "**{}** watched furry porn and died from what they saw.".format(user.name),
                        "**{}** 'accidentally' fell off a building.".format(user.name),
                        "**{}** may have ate food with cyanide.".format(user.name),
                        "**{}** saw Zero's face reveal and instantly died.".format(user.name),
                        "**{}** starved in a fast food restaurant. What a fucking idiot.".format(user.name),
                        "...And **{}** died happily ever after... Wait no, I messed it up!".format(user.name),
                        "**{}** joined this server and died. Oh well, that's not a first.".format(user.name),
                        "**{}** was gay in Iran.".format(user.name),
                        "**{}** choked on a banana ( ͡° ͜ʖ ͡°) and died.".format(user.name),
                        "**{}** drove off a cliff and survived, but died from shock when they saw the high price of the hospital bill.".format(user.name),
                        "**{}** listened to Justin Beiber for more than 0.69 seconds.".format(user.name),
                        "**{}** drank too much anti-freeze.".format(user.name),
                        "**{}** got stabbed with a cucumber by **{}**.".format(user.name, author.name),
                        "**{}** died from a heatstroke in the artic.".format(user.name),
                        "**{}** tried to fly. It worked till they hit the ground.".format(user.name),
                        "**{}** wanted to get a haircut in a faster way. They thought setting their hair on fire would do the trick.".format(user.name),
                        "On a peaceful night. The moon was shining and everyone was sleeping and enjoying their dreams while **{}** suffocated in their pillow.".format(user.name),
                        "**{}** got run over by a boat. A fricking boat!".format(user.name),
                        "What's that smell? It smells like toast... Hey, **{}**! Don't take out the toast with a fork- too late...".format(user.name),
                        "**{}** got a paper cut on both of their eyes, walked off a cliff and died. I guess books are evil.".format(user.name),
                        "**{}** tried putting out fire with gasoline.".format(user.name),
                        "**{}**'s head exploded while they were sitting on the toilet and pressing.".format(user.name),
                        "**{}** died of laughter. No, I mean they actually died.".format(user.name),
                        "**{}** got locked in a refrigerator and died of hunger.".format(user.name),
                        "**{}** drowned in their own tears after losing a game of Fortnite.".format(user.name),
                        "**{}** got beat up by their imaginary friends.".format(user.name),
                        "**{}** played My Little Ponny for too long.".format(user.name),
                        "**{}** choked on air.".format(user.name),
                        "**{}** got poked by Chuck Norris.".format(user.name),
                        "**{}** took a selfie with a gun.".format(user.name),
                        "**{}**'s brain exploded after **{}** saying 'What if dolphins had legs?'.".format(user.name, author.name),
                        "**{}** died after eating their favourite snack, tide pods.".format(user.name),
                        "**{}** survived the biggest waves then tripped on a rock and died.".format(user.name),
                        "**{}** ate white chocolate. Who the fuck eats white chocolate?".format(user.name),
                        "**{}** demonstrated how to die and then had a heart attack. How ironic.".format(user.name),
                        "**{}** fell in a toilet and then got flushed.".format(user.name),
                        "**{}** got stuck in a vending machine.".format(user.name),
                        "**{}** choked on their toothbrush and died.".format(user.name),
                        "**{}** found their butthole and died from excitement.".format(user.name),
                        "**{}** died. That's it. They just died.".format(user.name),
                        "**{}** saw **{}** naked and instantly died.".format(user.name, author.name),
                        "**{}** touched **{}**'s spaghet and died.".format(user.name, author.name),
                        "**{}** had too much porn and their mom cought them before they deleted it.".format(user.name)]
                embed.description = "{} {}".format(kill_e, random.choice(msgs))
                await client.say(embed=embed)

# }leave
@client.command(pass_context=True)
async def leave(ctx):
    embed = discord.Embed(colour=0x00)
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
        a = ["**{}** left the server!".format(ctx.message.author.name),
             "**{}** left your party!".format(ctx.message.author.name),
             "**{}** left the game!".format(ctx.message.author.name),
             "**{}** disconnected from your channel!".format(ctx.message.author.name),
             "**{}** left!".format(ctx.message.author.name)]
        await client.say(random.choice(a))
        await client.delete_message(ctx.message)

# }join
@client.command(pass_context=True)
async def join(ctx):
    embed = discord.Embed(colour=0x00)
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
        a = ["**{}** joined the server!".format(ctx.message.author.name),
             "**{}** joined your party!".format(ctx.message.author.name),
             "**{}** joined the game!".format(ctx.message.author.name),
             "**{}** connected to your channel!".format(ctx.message.author.name),
             "**{}** joined!".format(ctx.message.author.name)]
        await client.say(random.choice(a))
        await client.delete_message(ctx.message)

# }rate <something>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    embed = discord.Embed(colour=0x00)
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
            embed.description = "{} Please give me something to rate.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 100:
            embed.description = "{} The text cannot be longer than 100 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            c = []
            for i in rates:
                if args in str(i):
                    a = i.split(' | ')
                    p = int(a[1])
                    c.append("+1")
                    break
            if len(c) == 0:
                p = random.randint(0, 11)
                await client.send_message(client.get_channel(rates_chnl), "{} | {}".format(args, p))
                rates.append("{} | {}".format(args, p))
            embed.description = "{} I'd rate {} a `{}/10`.".format(rate_e, args, p)
            await client.say(embed=embed)

# }dicklength [user]
@client.command(pass_context=True)
async def dicklength(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
            author = ctx.message.author
        else:
            author = user
        c = []
        for i in dicks:
            a = i.split(' | ')
            if a[0] == author.id:
                p = int(a[1])
                c.append("+1")
                break
        if len(c) == 0:
            p = random.randint(0, 101)
            await client.send_message(client.get_channel(dicks_chnl), "{} | {}".format(author.id, p))
            dicks.append("{} | {}".format(author.id, p))
        if p <= 5:
            embed.description = "{} I'm sorry, **{}**. Your dick ran away.".format(dicklength_e, author.name)
            await client.say(embed=embed)
        elif p <= 10:
            embed.description = "{} I'm sorry, **{}**. Your dick fell off.".format(dicklength_e, author.name)
            await client.say(embed=embed)
        elif p >= 90:
            embed.description = "{} **{}**'s dick is too big for me to take the length of it.".format(dicklength_e, author.name)
            await client.say(embed=embed)
        else:
            embed.description = "{} **{}**'s dick is {}cm long.".format(dicklength_e, author.name, p)
            await client.say(embed=embed)

# }howgay [user]
@client.command(pass_context=True)
async def howgay(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
            author = ctx.message.author
        else:
            author = user
        c = []
        for i in howgays:
            a = i.split(' | ')
            if a[0] == author.id:
                p = int(a[1])
                c.append("+1")
                break
        if len(c) == 0:
            p = random.randint(0, 101)
            await client.send_message(client.get_channel(gays_chnl), "{} | {}".format(author.id, p))
            howgays.append("{} | {}".format(author.id, p))
        if p <= 5:
            embed.description = "{} **{}** is hella fucking gay.".format(howgay_e, author.name)
            await client.say(embed=embed)
        elif p <= 10:
            embed.description = "{} **{}** is not gay at all.".format(howgay_e, author.name)
            await client.say(embed=embed)
        else:
            embed.description = "{} **{}** is {}% gay.".format(howgay_e, author.name, p)
            await client.say(embed=embed)

# }chatrevive
@client.command(pass_context=True)
async def chatrevive(ctx):
    embed = discord.Embed(colour=0x00)
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
        await client.say(random.choice(revivals))
        await client.delete_message(ctx.message)

# }nhie
@client.command(pass_context=True)
async def nhie(ctx):
    embed = discord.Embed(colour=0x00)
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
        embed.description = "{} {}".format(messages_e, random.choice(nhie_msgs))
        await client.say(embed=embed)

# }wyr
@client.command(pass_context=True)
async def wyr(ctx):
    embed = discord.Embed(colour=0x00)
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
        embed.description = "{} {}".format(messages_e, random.choice(wyr_msgs))
        await client.say(embed=embed)

# }lettergen <number of letters>
@client.command(pass_context=True)
async def lettergen(ctx, number = None):
    embed = discord.Embed(colour=0x00)
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
        if number == None:
            embed.description = "{} Generated `1` random letter:\n\n{}".format(generator_e, random.choice(letters))
            await client.say(embed=embed)
        else:
            try:
                k = int(number)
                if k > 250:
                    embed.description = "{} The bot can generate up to 250 letters at once only.".format(error_e)
                    await client.say(embed=embed)
                else:
                    m = ""
                    for i in range(k):
                        m += " {}".format(random.choice(letters))
                    embed.description = "{} Generated `{}` random letters:\n\n{}".format(generator_e, k, m)
                    await client.say(embed=embed)
            except:
                embed.description = "{} Invalid number given.".format(error_e)
                await client.say(embed=embed)

# }numbergen <minimum number> <maximum number>
@client.command(pass_context=True)
async def numbergen(ctx, mi = None, ma = None):
    embed = discord.Embed(colour=0x00)
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
        if mi == None:
            minimum = 0
        else:
            minimum = mi
        if ma == None:
            maximum = 100
        else:
            maximum = ma
        try:
            k = int(maximum)
            p = int(minimum)
            embed.description = "{} Generated a random number from `{}` to `{}`:\n\n{}".format(generator_e, minimum, maximum, random.randint(p, k))
            await client.say(embed=embed)
        except:
            embed.description = "{} Invalid number(s) given.".format(error_e)
            await client.say(embed=embed)

# }ban <text>
@client.command(pass_context=True)
async def ban(ctx, *, text = None):
    embed = discord.Embed(colour=0x00)
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
        if text == None:
            embed.description = "{} No text given.".format(error_e)
            await client.say(embed=embed)
        elif len(str(text)) > 200:
            embed.description = "{} The text cannot be longer than 200 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "{} **{}** banned **{}**.".format(ban_e, ctx.message.author.name, text)
            await client.say(embed=embed)

''' CURRENCY COMMANDS FOR EVERYONE '''
# }convert
@client.command(pass_context=True)
async def convert(ctx):
    embed = discord.Embed(colour=0x00)
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
    elif ctx.message.author.id in con_wait:
        embed.description = "{} You have to wait a few minutes before converting again.".format(noperms_e)
        await client.say(embed=embed)
    else:
        con_wait.append(ctx.message.author.id)
        embed.description = "{} Converting messages into coins... {}".format(convert_e, loading_e)
        h = await client.say(embed=embed)
        async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
            a = i.content.split(' | ')
            if a[0] == ctx.message.author.id:
                new = int(a[1]) + con_messages.count(ctx.message.author.id)
                await client.edit_message(i, "{} | {}".format(ctx.message.author.id, new))
                embed.description = "{} Converted `{}` messages into `{}` coins!\n{} New balance: `{}` coins.".format(convert_e, con_messages.count(ctx.message.author.id), con_messages.count(ctx.message.author.id), coins_e, new)
                await client.edit_message(h, embed=embed)
                break
        for i in con_messages:
            if i == ctx.message.author.id:
                con_messages.remove(i)
        await asyncio.sleep(15)
        con_wait.remove(ctx.message.author.id)

# }marry <user>
@client.command(pass_context=True)
async def marry(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
            embed.description = "{} No user mentioned.".format(error_e)
            await client.say(embed=embed)
        else:
            author = ctx.message.author
            embed.description = "{} Checking profiles...".format(loading_e)
            h = await client.say(embed=embed)
            o = []
            for i in marriages:
                a = i.split(' | ')
                if author.id in i:
                    if author.id == a[0]:
                        k = await client.get_user_info(a[1])
                        if a[2] == "pending":
                            embed.description = "{} **{}**, you've already asked **{}** to marry you.\nUse `xf!md` to remove the request.".format(marriage_e, author.name, k.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                        else:
                            embed.description = "{} **{}**, you're already married to **{}**.".format(marriage_e, author.name, k.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                    elif author.id == a[1]:
                        k = await client.get_user_info(a[0])
                        if a[2] == "pending":
                            embed.description = "{} **{}**, **{}** has already asked to marry you.\nUse `xf!ma` to accept or `xf!md` to deny.".format(marriage_e, author.name, k.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                        else:
                            embed.description = "{} **{}**, **{}** is already married to you.".format(marriage_e, author.name, k.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                elif user.id in i:
                    if user.id == a[0]:
                        k = await client.get_user_info(a[1])
                        if a[2] == "pending":
                            embed.description = "{} **{}** has already asked **{}** to marry them.".format(marriage_e, user.name, k.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                        else:
                            embed.description = "{} **{}** is already married to **{}**.".format(marriage_e, user.name, k.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                    elif user.id == a[1]:
                        k = await client.get_user_info(a[0])
                        if a[2] == "pending":
                            embed.description = "{} **{}** has already asked **{}** to marry them.".format(marriage_e, k.name, user.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                        else:
                            embed.description = "{} **{}** is already married to **{}**.".format(marriage_e, k.name, user.name)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
            if len(o) == 0:
                embed.description = "{} **{}** asked **{}** to marry them!\n**{}**, use `xf!ma` to accept or `xf!md` to deny.".format(marriage_e, author.name, user.name, user.name)
                await client.edit_message(h, embed=embed)
                marriages.append("{} | {} | pending".format(author.id, user.id))
                await client.send_message(client.get_channel(marriages_chnl), "{} | {} | pending".format(author.id, user.id))

# }md
@client.command(pass_context=True)
async def md(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "{} Checking marriage requests...".format(loading_e)
        h = await client.say(embed=embed)
        o = []
        for i in marriages:
            a = i.split(' | ')
            if a[0] == author.id and a[2] == "pending":
                k = await client.get_user_info(a[1])
                embed.description = "{} **{}** removed the marriage request towards **{}**. :(".format(divorce_e, author.name, k.name)
                await client.edit_message(h, embed=embed)
                async for u in client.logs_from(client.get_channel(marriages_chnl), limit=limit):
                    if u.content == i:
                        await client.delete_message(u)
                        marriages.remove(i)
                        break
                o.append("+1")
                break
            elif a[1] == author.id and a[2] == "pending":
                k = await client.get_user_info(a[0])
                embed.description = "{} **{}** denied **{}**'s marriage request. :(".format(divorce_e, author.name, k.name)
                await client.edit_message(h, embed=embed)
                async for u in client.logs_from(client.get_channel(marriages_chnl), limit=limit):
                    if u.content == i:
                        await client.delete_message(u)
                        marriages.remove(i)
                        break
                o.append("+1")
                break
        if len(o) == 0:
            embed.description = "{} No marriage requests found.".format(marriage_e)
            await client.edit_message(h, embed=embed)

# }ma
@client.command(pass_context=True)
async def ma(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "{} Checking marriage requests...".format(loading_e)
        h = await client.say(embed=embed)
        o = []
        ubal = []
        abal = []
        umsg = []
        amsg = []
        for i in marriages:
            a = i.split(' | ')
            if a[0] == author.id and a[2] == "pending":
                o.append(i)
                o.append(i)
                user = await client.get_user_info(a[1])
                embed.description = "{} You have sent a marriage request to **{}**.\nThey still haven't replied.".format(marriage_e, user.name)
                await client.edit_message(h, embed=embed)
            elif a[1] == author.id and a[2] == "pending":
                o.append(i)
                user = await client.get_user_info(a[0])
                async for u in client.logs_from(client.get_channel(balances_chnl), limit=limit):
                    b = u.content.split(' | ')
                    if b[0] == author.id:
                        abal.append(b[1])
                        amsg.append(u)
                    elif b[0] == user.id:
                        ubal.append(b[1])
                        umsg.append(u)
        if len(o) == 0:
            embed.description = "{} No marriage requests found.".format(marriage_e)
            await client.edit_message(h, embed=embed)
        elif len(o) == 1:
            if int(abal[0]) >= 5000 and int(ubal[0]) >= 5000:
                await client.edit_message(umsg[0], "{} | {}".format(user.id, int(ubal[0]) - 5000))
                await client.edit_message(amsg[0], "{} | {}".format(author.id, int(abal[0]) - 5000))
                embed.description = "{} **{}** and **{}** married each other!\nCongratulations!".format(marriage_e, author.name, user.name)
                await client.edit_message(h, embed=embed)
                async for i in client.logs_from(client.get_channel(marriages_chnl), limit=limit):
                    if i.content == o[0]:
                        a = i.content.split(' | ')
                        await client.edit_message(i, "{} | {} | married".format(a[0], a[1]))
                        marriages.remove(i.content)
                        marriages.append("{} | {} | married".format(a[0], a[1]))
                        break
            else:
                embed.description = "{} Both you and **{}** have to have `5000` coins to marry each other.".format(error_e, user.name)
                await client.edit_message(h, embed=embed)

# }divorce
@client.command(pass_context=True)
async def divorce(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "{} Checking profiles...".format(loading_e)
        h = await client.say(embed=embed)
        o = []
        abal = []
        amsg = []
        for i in marriages:
            a = i.split(' | ')
            if a[0] == author.id and a[2] == "married":
                o.append(i)
                user = await client.get_user_info(a[1])
                async for u in client.logs_from(client.get_channel(balances_chnl), limit=limit):
                    b = u.content.split(' | ')
                    if b[0] == author.id:
                        abal.append(b[1])
                        amsg.append(u)
                        break
            elif a[1] == author.id and a[2] == "married":
                o.append(i)
                user = await client.get_user_info(a[0])
                async for u in client.logs_from(client.get_channel(balances_chnl), limit=limit):
                    b = u.content.split(' | ')
                    if b[0] == author.id:
                        abal.append(b[1])
                        amsg.append(u)
                        break
        if len(o) == 0:
            embed.description = "{} You are not married.".format(marriage_e)
            await client.edit_message(h, embed=embed)
        else:
            if int(abal[0]) >= 2500:
                await client.edit_message(amsg[0], "{} | {}".format(author.id, int(abal[0]) - 2500))
                embed.description = "{} **{}** and **{}** divorced!\nCongrats..?".format(divorce_e, author.name, user.name)
                await client.edit_message(h, embed=embed)
                async for i in client.logs_from(client.get_channel(marriages_chnl), limit=limit):
                    if i.content == o[0]:
                        a = i.content.split(' | ')
                        await client.delete_message(i)
                        marriages.remove(i.content)
                        break
            else:
                embed.description = "{} You have to have `2500` coins to divorce.".format(error_e)
                await client.edit_message(h, embed=embed)

# }bal [user]
@client.command(pass_context=True)
async def bal(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
            author = ctx.message.author
        else:
            author = user
        embed.description = "{} Checking balances...".format(loading_e)
        h = await client.say(embed=embed)
        async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
            a = i.content.split(' | ')
            if a[0] == author.id:
                embed.description = "{} **{}** has `{}` coins.".format(coins_e, author.name, a[1])
                await client.edit_message(h, embed=embed)

# }profile [user]
@client.command(pass_context=True)
async def profile(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        if user == None:
            author = ctx.message.author
        else:
            author = user
        embed.description = "{} Loading profile... {}".format(users_e, loading_e)
        h = await client.say(embed=embed)
        m = "{} *Profile*".format(users_e)
        m += "\n**{}**".format(author.name)
        m += "\n**~~`=====`~~**"
        async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
            a = i.content.split(' | ')
            if a[0] == author.id:
                m += "\n{} Balance: `{} coins`".format(coins_e, a[1])
                break
        for i in marriages:
            if author.id in i and 'married' in i:
                a = i.split(' | ')
                if a[0] == author.id:
                    k = await client.get_user_info(a[1])
                    m += "\n{} Married to: `{}`".format(marriage_e, k.name)
                    o.append("+1")
                    break
                else:
                    k = await client.get_user_info(a[0])
                    m += "\n{} Married to: `{}`".format(marriage_e, k.name)
                    break
        for i in dicks:
            if author.id in i:
                a = i.split(' | ')
                m += "\n{} Dick length: `{}cm`".format(dicklength_e, a[1])
                break
        for i in howgays:
            if author.id in i:
                a = i.split(' | ')
                m += "\n{} Gay percentage: `{}%`".format(howgay_e, a[1])
                break
        m += "\n**~~`=====`~~**"
        embed.description = m
        await client.edit_message(h, embed=embed)

# }slots <number>
@client.command(pass_context=True)
async def slots(ctx, number = None):
    embed = discord.Embed(colour=0x00)
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
    elif ctx.message.author.id in slots_wait:
        embed.description = "{} You have to wait a few seconds before gambling again.".format(error_e)
        await client.say(embed=embed)
    else:
        if number == None:
            embed.description = "{} No amount given.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                k = int(number)
                slots_wait.append(ctx.message.author.id)
                m = "**`-----------------`**"
                m += "\n**`|` {} | {} | {} `|`**".format(slotsgif1_e, slotsgif2_e, slotsgif3_e)
                m += "\n**`|` {} | {} | {} `|`**".format(slotsgif4_e, slotsgif1_e, slotsgif2_e)
                m += "\n**`|` {} | {} | {} `|`**".format(slotsgif3_e, slotsgif4_e, slotsgif1_e)
                m += "\n**`-----------------`**"
                embed.description = "{} Gambling... {}\n{}".format(slots_e, loading_e, m)
                h = await client.say(embed=embed)
                async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
                    a = i.content.split(' | ')
                    if a[0] == ctx.message.author.id:
                        if int(a[1]) >= k:
                            p = random.randint(0, 1)
                            if p == 0:
                                new = int(a[1]) - k
                                embed.description = "{} **{}** gambled and lost `{}` coins!\n{} New balance: `{}` coins.".format(slots_e, ctx.message.author.name, number, coins_e, new)
                                await client.edit_message(i, "{} | {}".format(ctx.message.author.id, new))
                                await client.edit_message(h, embed=embed)
                                break
                            else:
                                new = int(a[1]) + k
                                embed.description = "{} **{}** gambled and won `{}` coins!\n{} New balance: `{}` coins.".format(slots_e, ctx.message.author.name, number, coins_e, new)
                                await client.edit_message(i, "{} | {}".format(ctx.message.author.id, new))
                                await client.edit_message(h, embed=embed)
                                break
                        else:
                            embed.description = "{} You don't have enough coins.".format(error_e)
                            await client.edit_message(h, embed=embed)
                slots_wait.remove(ctx.message.author.id)
            except:
                embed.description = "{} Invalid amount.".format(error_e)
                await client.say(embed=embed)

# }work
@client.command(pass_context=True)
async def work(ctx):
    embed = discord.Embed(colour=0x00)
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
    elif ctx.message.author.id in worked:
        embed.description = "{} You have to get some rest before working again.".format(error_e)
        await client.say(embed=embed)
    else:
        worked.append(ctx.message.author.id)
        embed.description = "{} **{}** went to work... {}".format(work_e, ctx.message.author.name, loading_e)
        h = await client.say(embed=embed)
        async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
            a = i.content.split(' | ')
            if a[0] == ctx.message.author.id:
                p = random.randint(100, 300)
                new = int(a[1]) + p
                await client.edit_message(i, "{} | {}".format(ctx.message.author.id, new))
                embed.description = "{} **{}** worked for a few hours and gained `{}` coins.\n{} New balance: `{}` coins.".format(work_e, ctx.message.author.name, p, coins_e, new)
                await client.edit_message(h, embed=embed)
                break
        await asyncio.sleep(7200)
        worked.remove(ctx.message.author.id)

# }steal <user>
@client.command(pass_context=True)
async def steal(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
    elif ctx.message.author.id in stole:
        embed.description = "{} You have to get some rest before going out to steal again.".format(error_e)
        await client.say(embed=embed)
    else:
        if user == None:
            embed.description = "{} No user mentioned.".format(error_e)
            await client.say(embed=embed)
        else:
            stole.append(ctx.message.author.id)
            embed.description = "{} **{}** went to find someone to steal from... {}".format(steal_e, ctx.message.author.name, loading_e)
            h = await client.say(embed=embed)
            p = random.randint(50, 150)
            o = []
            async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
                if len(o) == 2:
                    break
                else:
                    a = i.content.split(' | ')
                    if a[0] == ctx.message.author.id:
                        new = int(a[1]) + p
                        embed.description = "{} **{}** stole `{}` coins from **{}**.\n{} New balance: `{}` coins.".format(steal_e, ctx.message.author.name, p, user.name, coins_e, new)
                        await client.edit_message(i, "{} | {}".format(ctx.message.author.id, new))
                        o.append("+1")
                    elif a[0] == user.id:
                        new = int(a[1]) - p
                        await client.edit_message(i, "{} | {}".format(user.id, new))
                        o.append("+1")
            await client.edit_message(h, embed=embed)
            await asyncio.sleep(7200)
            stole.remove(ctx.message.author.id)

# }gift <user> <amount>
@client.command(pass_context=True)
async def gift(ctx, user: discord.Member = None, number = None):
    embed = discord.Embed(colour=0x00)
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
    elif ctx.message.author.id in stole:
        embed.description = "{} You have to get some rest before going out to steal again.".format(error_e)
        await client.say(embed=embed)
    else:
        if user == None or number == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `xf!gift <user> <amount>`".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                k = int(number)
                embed.description = "{} Checking balances... {}".format(gift_e, loading_e)
                h = await client.say(embed=embed)
                o = []
                async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
                    a = i.content.split(' | ')
                    if a[0] == ctx.message.author.id:
                        if int(a[1]) >= k:
                            o.append("+1")
                            break
                        else:
                            embed.description = "{} You do not have enough coins.".format(error_e)
                            await client.edit_message(h, embed=embed)
                            break
                if len(o) != 0:
                    b = []
                    async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
                        if len(b) == 2:
                            break
                        else:
                            a = i.content.split(' | ')
                            if a[0] == ctx.message.author.id:
                                new = int(a[1]) - k
                                await client.edit_message(i, "{} | {}".format(ctx.message.author.id, new))
                                b.append("+1")
                                break
                            elif a[1] == user.id:
                                new = int(a[1]) + k
                                await client.edit_message(i, "{} | {}".format(user.id, new))
                                b.append("+1")
                                break
                    embed.description = "{} **{}** gave `{}` coins to **{}**.".format(gift_e, ctx.message.author.name, number, user.name)
                    await client.edit_message(h, embed=embed)
            except:
                embed.description = "{} Invalid amount given.".format(error_e)
                await client.say(embed=embed)
            

''' INTERACTION COMMANDS FOR EVERYONE '''
# }hug <user>
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to hug.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** hugged **{}**. How cute.".format(author.name, user.name)
            embed.set_image(url=random.choice(hug_links))
            await client.say(embed=embed)

# }kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to kiss.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** kissed **{}**. owo".format(author.name, user.name)
            embed.set_image(url=random.choice(kiss_links))
            await client.say(embed=embed)

# }pat <user>
@client.command(pass_context=True)
async def pat(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to pat.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** got a pat from **{}**. Aww.".format(user.name, author.name)
            embed.set_image(url=random.choice(pat_links))
            await client.say(embed=embed)

# }punch <user>
@client.command(pass_context=True)
async def punch(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to punch.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** punched **{}**. Wow, calm down!".format(author.name, user.name)
            embed.set_image(url=random.choice(punch_links))
            await client.say(embed=embed)

# }cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to cuddle.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** cuddled **{}**. uwu".format(author.name, user.name)
            embed.set_image(url=random.choice(cuddle_links))
            await client.say(embed=embed)

# }bite <user>
@client.command(pass_context=True)
async def bite(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to bite.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** got biten by **{}**. Ouch.".format(user.name, author.name)
            embed.set_image(url=random.choice(bite_links))
            await client.say(embed=embed)

# }bloodsuck <user>
@client.command(pass_context=True)
async def bloodsuck(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to suck blood from.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** sucked some of **{}**'s blood. Yum.".format(author.name ,user.name)
            embed.set_image(url=random.choice(bloodsuck_links))
            await client.say(embed=embed)

# }throw <user>
@client.command(pass_context=True)
async def throw(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to throw.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** got thrown by **{}**. Weee.".format(user.name, author.name)
            embed.set_image(url=random.choice(throw_links))
            await client.say(embed=embed)

# }nom <user>
@client.command(pass_context=True)
async def nom(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to nom.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** nommed **{}**. Hehe.".format(author.name, user.name)
            embed.set_image(url=random.choice(nom_links))
            await client.say(embed=embed)

# }highfive <user>
@client.command(pass_context=True)
async def highfive(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to highfive.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** highfived **{}**. Woo.".format(author.name, user.name)
            embed.set_image(url=random.choice(highfive_links))
            await client.say(embed=embed)

# }poke <user>
@client.command(pass_context=True)
async def poke(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to poke.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** poked **{}**. Hmm?".format(author.name, user.name)
            embed.set_image(url=random.choice(poke_links))
            await client.say(embed=embed)

# }slap <user>
@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to slap.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** slapped **{}**. They probably deserved it.".format(author.name, user.name)
            embed.set_image(url=random.choice(slap_links))
            await client.say(embed=embed)

# }stare <user>
@client.command(pass_context=True)
async def stare(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to stare at.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** is staring at **{}**. Creep.".format(author.name, user.name)
            embed.set_image(url=random.choice(stare_links))
            await client.say(embed=embed)

# }spank <user>
@client.command(pass_context=True)
async def spank(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to spank.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** got spanked by **{}**. Huehuehue.".format(user.name, author.name)
            embed.set_image(url=random.choice(spank_links))
            await client.say(embed=embed)

# }lick <user>
@client.command(pass_context=True)
async def lick(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        if user == None:
            embed.description = "{} Please mention someone you want to lick.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "**{}** licked **{}**. Weirdo.".format(author.name, user.name)
            embed.set_image(url=random.choice(lick_links))
            await client.say(embed=embed)

# }facepalm
@client.command(pass_context=True)
async def facepalm(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "**{}** facepalmed. Oh.".format(author.name)
        embed.set_image(url=random.choice(facepalm_links))
        await client.say(embed=embed)

# }cry
@client.command(pass_context=True)
async def cry(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "**{}** is crying. So sad.".format(author.name)
        embed.set_image(url=random.choice(cry_links))
        await client.say(embed=embed)

# }dance
@client.command(pass_context=True)
async def dance(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "**{}** is dancing. Wooo!".format(author.name)
        embed.set_image(url=random.choice(dance_links))
        await client.say(embed=embed)

# }bow
@client.command(pass_context=True)
async def bow(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "**{}** bows. Respect.".format(author.name)
        embed.set_image(url=random.choice(bow_links))
        await client.say(embed=embed)

# }dab
@client.command(pass_context=True)
async def dab(ctx):
    embed = discord.Embed(colour=0x00)
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
        author = ctx.message.author
        embed.description = "**{}** dabs. Okay...".format(author.name)
        embed.set_image(url=random.choice(dab_links))
        await client.say(embed=embed)

''' COMMANDS FOR SERVER MANAGERS '''
# }responses
@client.command(pass_context=True)
async def responses(ctx):
    embed = discord.Embed(colour=0x00)
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
        if ctx.message.author.server_permissions.manage_server or ctx.message.author.id in mods:
            embed.description = "{} Saving changes...".format(loading_e)
            h = await client.say(embed=embed)
            if ctx.message.server.id in responses_t:
                async for i in client.logs_from(client.get_channel(responses_t_chnl), limit=limit):
                    if i.content == ctx.message.server.id:
                        await client.delete_message(i)
                        responses_t.remove(ctx.message.server.id)
                        embed.description = "{}{} Automatic responses have been turned on.".format(messages_e, on_e)
                        await client.edit_message(h, embed=embed)
                        break
            else:
                await client.send_message(client.get_channel(responses_t_chnl), ctx.message.server.id)
                responses_t.append(ctx.message.server.id)
                embed.description = "{}{} Automatic responses have been turned off.".format(messages_e, off_e)
                await client.edit_message(h, embed=embed)
        else:
            embed.description = "{} This command can only be used by users with the `Manage Server` permission and can be bypassed by bot moderators.".format(noperms_e)
            await client.say(embed=embed)

# }currency
@client.command(pass_context=True)
async def currency(ctx):
    embed = discord.Embed(colour=0x00)
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
        if ctx.message.author.server_permissions.manage_server or ctx.message.author.id in mods:
            embed.description = "{} Saving changes...".format(loading_e)
            h = await client.say(embed=embed)
            if ctx.message.server.id in currency_t:
                async for i in client.logs_from(client.get_channel(currency_t_chnl), limit=limit):
                    if i.content == ctx.message.server.id:
                        await client.delete_message(i)
                        currency_t.remove(ctx.message.server.id)
                        embed.description = "{}{} Currency rewards have been turned on.".format(coins_e, on_e)
                        await client.edit_message(h, embed=embed)
                        break
            else:
                await client.send_message(client.get_channel(currency_t_chnl), ctx.message.server.id)
                currency_t.append(ctx.message.server.id)
                embed.description = "{}{} Currency rewards have been turned off.".format(messages_e, off_e)
                await client.edit_message(h, embed=embed)
        else:
            embed.description = "{} This command can only be used by users with the `Manage Server` permission and can be bypassed by bot moderators.".format(noperms_e)
            await client.say(embed=embed)

# }ignore <channel name>
@client.command(pass_context=True)
async def ignore(ctx, channel = None):
    embed = discord.Embed(colour=0x00)
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
        if ctx.message.author.server_permissions.manage_server or ctx.message.author.id in mods:
            if channel == None:
                embed.description = "{} No channel name given.".format(error_e)
                await client.say(embed=embed)
            else:
                embed.description = "{} Saving changes...".format(loading_e)
                h = await client.say(embed=embed)
                for i in ctx.message.server.channels:
                    if channel.lower() in str(i.name.lower()):
                        if i.id in ignored:
                            async for u in client.logs_from(client.get_channel(ignored_chnl), limit=limit):
                                if u.content == i.id:
                                    await client.delete_message(u)
                                    ignored.remove(i.id)
                                    embed.description = "{} Removed <#{}> from the ignored list.".format(ignored_e, i.id)
                                    await client.edit_message(h, embed=embed)
                                    break
                            break
                        else:
                            await client.send_message(client.get_channel(ignored_chnl), i.id)
                            ignored.append(i.id)
                            embed.description = "{} Added <#{}> to the ignored list.".format(ignored_e, i.id)
                            await client.edit_message(h, embed=embed)
                            break
        else:
            embed.description = "{} This command can only be used by users with the `Manage Server` permission and can be bypassed by bot moderators.".format(noperms_e)
            await client.say(embed=embed)

''' COMMANDS FOR BOT MODERATORS '''
# }umsg <user ID> <text>
@client.command(pass_context=True)
async def umsg(ctx, target = None, *, args = None):
    embed = discord.Embed(colour=0x00)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        if author.id in mods:
            if target == None or args == None:
                embed.description = "{} The command was used incorrectly.\nProper usage: `xf!umsg <user ID> <text>`.".format(error_e)
                await client.say(embed=embed)
            elif len(str(args)) > 1500:
                embed.description = "{} The text cannot be longer than 1500 characters.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    user = await client.get_user_info(target)
                    try:
                        await client.send_message(user, ":wave: **__Hello there!__**\n**__You got a new message from one of the bot's staff.__**\n\n:incoming_envelope: `Message:` {}\n:label: `From:` {} ### {}".format(args, author, author.id))
                        embed.description = "{} Sent message to **{}** ( `{}` ).".format(worked_e, user, target)
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__User Message__** {}".format(log_e, msg_e)
                        m += "\n`Sent to:` {} ### {}".format(user, user.id)
                        m += "\n`Sent by:` {} ## {}".format(ctx.message.author, ctx.message.author.id)
                        await client.send_message(client.get_channel(log_chnl), m)
                    except:
                        embed.description = "{} Unable to DM **{}** ( `{}` ).".format(error_e, user, target)
                        await client.say(embed=embed)
                except:
                    embed.description = "{} A user with that ID was not found.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the bot's staff.".format(error_e)
            await client.say(embed=embed)

# }smsg <user ID> <text>
@client.command(pass_context=True)
async def smsg(ctx, target = None, *, args = None):
    embed = discord.Embed(colour=0x00)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        if author.id in mods:
            if target == None or args == None:
                embed.description = "{} The command was used incorrectly.\nProper usage: `xf!smsg <server ID> <text>`.".format(error_e)
                await client.say(embed=embed)
            elif len(str(args)) > 1500:
                embed.description = "{} The text cannot be longer than 1500 characters.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    server = client.get_server(target)
                    try:
                        await client.send_message(server.owner, ":wave: **__Hello there!__**\n**__You got a new message from one of the bot's staff.__**\n\n:incoming_envelope: `Message:` {}\n:label: `From:` {} ### {}".format(args, author, author.id))
                        embed.description = "{} Sent message to **{}** ( `{}` )'s owner.".format(worked_e, server.name, target)
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__Server Message__** {}".format(log_e, msg_e)
                        m += "\n`Sent to:` {} ### {}".format(server.name, server.id)
                        m += "\n`Sent by:` {} ## {}".format(ctx.message.author, ctx.message.author.id)
                        await client.send_message(client.get_channel(log_chnl), m)
                    except:
                        embed.description = "{} Unable to DM **{}** ( `{}` )'s owner.".format(error_e, server.owner, target)
                        await client.say(embed=embed)
                except:
                    embed.description = "{} A server with that ID was not found.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the bot's staff.".format(error_e)
            await client.say(embed=embed)

# }close <ticket number>
@client.command(pass_context=True)
async def close(ctx, number = None):
    embed = discord.Embed(colour=0x00)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        if author.id in mods:
            if number == None:
                embed.description = "{} No ticket number given.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    test = int(number)
                    embed.description = "{} Looking for ticket...".format(loading_e)
                    h = await client.say(embed=embed)
                    a = []
                    async for i in client.logs_from(client.get_channel(tickets_chnl), limit=limit):
                        if i.id == number:
                            await client.delete_message(i)
                            embed.description = "{} Closed ticket with number `{}`.".format(worked_e, number)
                            await client.edit_message(h, embed=embed)
                            a.append("+1")
                            log = splitter
                            log += "\n{} **__Close Ticket__** {}".format(log_e, close_e)
                            log += "\n`Ticket number:` {}".format(number)
                            log += "\n`Closed by:` {} ### {}".format(ctx.message.author, ctx.message.author.id)
                            await client.send_message(client.get_channel(log_chnl), log)
                            break
                    if len(a) == 0:
                        embed.description = "{} A ticket with that number was not found.".format(error_e)
                        await client.edit_message(h, embed=embed)
                except:
                    embed.description = "{} The ticket number has to be a number.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the bot's staff.".format(error_e)
            await client.say(embed=embed)

# }link <server ID>
@client.command(pass_context=True)
async def link(ctx, target = None):
    embed = discord.Embed(colour=0x00)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        if author.id in mods:
            if target == None:
                embed.description = "{} No server ID given.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    test = int(target)
                    try:
                        server = client.get_server(target)
                        try:
                            invs = await client.invites_from(server)
                            embed.description = "{} Here is the invite link for **{}** ( `{}` ):\n[click here to join]({})".format(worked_e, server.name, target, invs[0])
                            await client.say(embed=embed)
                            m = splitter
                            m += "\n{} **__Link__** {}".format(log_e, link_e)
                            m += "\n`For server:` {} ### {}".format(server.name, server.id)
                            m += "\n`Taken by:` {} ### {}".format(ctx.message.author, ctx.message.author.id)
                            await client.send_message(client.get_channel(log_chnl), m)
                        except:
                            embed.description = "{} Was not able to get an invite link for **{}** ( `{}` ).".format(error_e, server.name, target)
                            await client.say(embed=embed)
                    except:
                        embed.description = "{} A server with that ID was not found.".format(error_e)
                        await client.say(embed=embed)
                except:
                    embed.description = "{} The server ID has to be a number.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the bot's staff.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR BOT OWNER '''
# }mod <user id>
@client.command(pass_context=True)
async def mod(ctx, target = None):
    embed = discord.Embed(colour=0x00)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        if author.id == '412201413335056386':
            if target == None:
                embed.description = "{} No user ID given.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    user = await client.get_user_info(target)
                    if user.id in mods:
                        mods.remove(user.id)
                        async for i in client.logs_from(client.get_channel(mods_chnl), limit=limit):
                            if i.content == user.id:
                                await client.delete_message(i)
                        embed.description = "{} Removed **{}** ( `{}` ) from the mods list.".format(worked_e, user, user.id)
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__Mod List Edit__** {}".format(log_e, worked_e)
                        m += "\n`Added:` {} ### {}".format(user, user.id)
                        m += "\n`Added by:` {} ### {}".format(ctx.message.author, ctx.message.author.id)
                        await client.send_message(client.get_channel(log_chnl), m)
                    else:
                        mods.append(user.id)
                        await client.send_message(client.get_channel(mods_chnl), user.id)
                        embed.description = "{} Added **{}** ( `{}` ) to the mods list.".format(worked_e, user, user.id)
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__Mod List Edit__** {}".format(log_e, worked_e)
                        m += "\n`Removed:` {} ### {}".format(user, user.id)
                        m += "\n`Removed by:` {} ### {}".format(ctx.message.author, ctx.message.author.id)
                        await client.send_message(client.get_channel(log_chnl), m)
                except:
                    embed.description = "{} User with that ID not found.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the bot's owner.".format(error_e)
            await client.say(embed=embed)

# }say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    embed = discord.Embed(colour=0x00)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        if ctx.message.author.id == '412201413335056386':
            if args == None:
                embed.description = "{} No text given.".format(error_e)
                await client.say(embed=embed)
            else:
                await client.say(args)
                await client.delete_message(ctx.message)
        else:
            embed.description = "{} This command can only be used by the bot's owner.".format(error_e)
            await client.say(embed=embed)


#######################
client.run(os.environ['BOT_TOKEN'])
