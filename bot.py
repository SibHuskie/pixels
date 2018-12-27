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
admin_roles = "527373859335176202"
mod_roles = []
helper_roles = []
partner_manager_roles = []
partner_roles = []
muted_roles = []
member_roles = []
self_roles = []
logs = [527410630798475274]
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
rates = []
revivals = ["Tell me the 3 best things about you.",
            "On a scale of 1-10, how strict are/were your parents?",
            "Who was your worst teacher? Why?",
            "Who was your favorite teacher? Why?",
            "Which would you pick: being world-class attractive, a genius or famous for doing something great?",
            "Who are the 3 greatest living musicians?",
            "If you could change one thing about yourself, what would it be?",
            "What was your favorite toy growing up?",
            "Name 3 celebrities you most admire.",
            "Name a celebrity you think is lame.",
            "What accomplishment are you most proud of?",
            "Which of your friends are you proudest of? Why?",
            "What's the most beautiful place you've ever been?",
            "What are your 3 favorite movies?",
            "How would you describe me to your friends?",
            "Which historical figure would you like to be?",
            "What's the right age to get married?",
            "Tell me 3 things you remember about kindergarten.",
            "What paper that you've written are you most proud of?",
            "What would you do if you were invisible for a day?",
            "Who would you like to live like for a day?",
            "If you could time travel, where would you go?",
            "If you could live in any TV home, what would it be?",
            "What's your favorite ice cream flavor?",
            "Would you rather live for a week in the past or the future?",
            "What's your most embarrassing childhood memory?",
            "What's your best childhood memory?",
            "What's your favorite holiday?",
            "If you could eat only 3 foods for the rest of your life, what would they be?",
            "If you could be a cartoon character for a week, who would you be?",
            "If you could have dinner with anyone from history, who would it be?",
            "What's one choice you really regret?",
            "What's your favorite childhood book?",
            "What's a great book you've read recently?",
            "Do you feel like a leader or a follower?",
            "If you could ask your pet 3 questions, what would they be?",
            "What's the most courageous thing you've ever done?",
            "Who would play you in a movie of your life?",
            "If you could be an Olympic athlete, in what sport would you compete?",
            "If you had to live in a different state, what would it be?",
            "What living person, other than family members, do you most admire?",
            "What has been your favorite family vacation?",
            "If you could choose your own nickname, what would it be?",
            "Who is the funniest person you know?",
            "What's your favorite thing about one of your grandparents?",
            "Tell the person to your right your favorite thing about them.",
            "Do you ever talk to yourself? When and what do you say?",
            "When you're having a bad day, what do you do to make yourself feel better?",
            "Which TV family is most like your own?",
            "What's your favorite smell in the whole world?",
            "What do you think is the greatest invention of all time?",
            "Using one word, how would you describe your family?",
            "Would you rather win an Olympic medal, an Academy Award or the Nobel Peace prize?",
            "What's your favorite time of day?",
            "What's your favorite season?",
            "What's the one food you could never bring yourself to eat?",
            "What is the sound you love the most?",
            "What 3 famous people, living or dead, would you want at your fantasy dinner party?",
            "If you could ask the President one question, what would it be?",
            "If you could pick a new first name, what would it be?",
            "If you had to leave earth on a spaceship and take 4 friends with you, who would they be?",
            "What is your favorite movie quote?",
            "What's your pet peeve(s)?",
            "Do you sleep with your sheets tucked in or out?",
            "Do you ever count your steps when you walk?",
            "What's your favorite kind of sandwich?",
            "What's your dream job?",
            "Cake or pie?",
            "Who is the kindest person you know?",
            "What's the best part about having siblings?",
            "What is the scariest movie you've ever seen?",
            "If you could travel anywhere in the world, where would it be?",
            "What is your favorite family tradition?",
            "Who's your celebrity crush?",
            "What trait do you like the most about yourself?",
            "What are you good at?",
            "What fictional character do you wish you could meet?",
            "If you could be great at one sport which would you choose?",
            "What's the first thing you do when you get home from a trip?",
            "Would you rather spend five days exploring Disney or New York City?",
            "Whose parents do/did you wish you had?",
            "If you could shop for free at one store, which one would you choose?",
            "What personal trait has gotten you in the most trouble?",
            "Which celebrity chef would you most like to fix you a meal?",
            "Who is your favorite athlete?",
            "What is the best piece of advice you've received?",
            "If you had to pick a new name for yourself, what name would you pick?",
            "Would you rather be the most popular kid in school or the smartest kid in school?",
            "What do you like to do on a rainy day?",
            "Would you rather be the best player on a horrible team or the worst player on a great team?",
            "What is your favorite thing about the beach?",
            "If you could be anywhere else right now, where would it be?",
            "What is your favorite Disney movie?",
            "Which of the Seven Dwarfs is most like you?",
            "If someone made a movie of your life would it be a drama, a comedy, a romantic-comedy, action film, or science fiction?",
            "Name a product or service you love so much that you'd happily be that company's spokesperson.",
            "If you were guaranteed to be successful in a different profession, what would you want to do?",
            "As a child, what did you wish to become when you grew up?",
            "What's the worst thing you did as a kid?",
            "What is the best part of being a part of your family?",
            "What is your favorite day of the week?"]

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
rates_chnl = '527714528721633280'
revivals_chnl = '515851181722173460'


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
kill_e = ":busts_in_silhouette: "
rate_e = ":rate:"
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
            
# }kill <user>
@client.command(pass_context=True)
async def kill(ctx, user: discord.Member = None):
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
                        "**{}** saw Huskie's face reveal and instantly died.".format(user.name),
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
        a = ["Cya `{}` :wave:".format(ctx.message.author.name)]
        await client.say(random.choice(a))
        await client.delete_message(ctx.message)
            
# }rate <something>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
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
            
# }chatrevive
@client.command(pass_context=True)
async def topic(ctx):
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
        await client.say(random.choice(revivals))
        await client.delete_message(ctx.message)
      
      
      
 










######################################################## STAFF #############################################################













# }cb
@client.command(pass_context=True)
async def cb(ctx):
    embed = discord.Embed(colour=0x000000)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    embed.description = "{} Deleting latest messages sent by bots... {}".format(clearbots_e, loading_e)
                    h = await client.say(embed=embed)
                    msgs = [1]
                    async for o in client.logs_from(ctx.message.channel, limit=100, before=ctx.message):
                        if o.author.bot and o.id != h.id:
                            msgs.append(o)
                try:
                    await client.delete_messages(msgs)
                    embed.description = "{} **{}** removed the latest messages sent by bots.".format(clearbots_e, author.name)
                    await client.edit_message(h, embed=embed)
                except:
                    for o in msgs:
                        await client.delete_message(o)
                    embed.description = "{} **{}** removed the latest messages sent by bots.".format(clearbots_e, author.name)
                    await client.edit_message(h, embed=embed)
                a.append("+1")
                break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
            await client.say(embed=embed)

































#######################
client.run(os.environ['BOT_TOKEN'])
