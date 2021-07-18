import discord
from discord import activity
from discord import state
from discord import message
from discord import reaction
from discord import emoji
from discord import channel
from discord import guild
from discord import voice_client
from discord.activity import Activity, BaseActivity, Streaming, Game, CustomActivity
from discord.ext import commands, tasks
import time
import youtube_dl

linux_list=["linux", "Linux"]
gnu_list=["GNU", "gnu", "Gnu"]
arrow_list=[":arrow_left:", ":arrow_right:", ":stop_button:"]

players = {}

#first id = My main acc, second id = My alt acc,
dev_id_list=[832581418634313768, 862464846167801896]
XMR_donate_addr=""

token = '' #put your token here if you're running the code on a private machine

client = discord.Client()
bot = commands.Bot("sudo ", self_bot=False)


print("bot.py started")


@client.event
async def on_ready():
    try:
        print("Bot is ready")
        print(client.user.name)
        print(client.user.id)
        print(client.activity)
    except Exception as e:
        print(e)

@client.event
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name="sudo Help", url='https://youtu.be/9sJUDx7iEJw?t=20'))
    print("changed status???")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        print(f"message sent:\n author: {message.author}\n Location: {message.guild}, {message.channel}\n content: {message.content}")
        
        print("pass on_message()\t No issues so far")


#Join message
@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Thank you for adding this bot, the prefix is <sudo> use <sudo help> for a list of commands\n if you want some information on how this bot was made use <sudo info>\n if you want to help support me use <sudo donate> to see my recieve address (XMR only)')
        break


#if someone sends linux
@bot.event
async def on_linux(ctx, message):
    if linux_list in message.content:
        if gnu_list in message.content:
            pass
        else:
            print("on_linux is working") 
            await ctx.trigger_typing
            await message.channel.send("I'd just like to interject for a moment.")
            await message.channel.send("What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. ")
            await message.channel.send("Linux is not an operating system unto itself,\n but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.")
            await message.channel.send('Many computer users run a modified version of the GNU system every day, without realizing it.  Through a peculiar turn of events, the version of GNU which is widely used today is often called "Linux", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.')
            await message.channel.send("There really is a Linux, and these people are using it, but it is just a part of the system they use." )
            await message.channel.send("Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run.")
            await message.channel.send("The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system.")
            await message.channel.send("Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. ")
            await message.channel.send('All the so-called "Linux" distributions are really distributions of GNU/Linux.')
            print(f"{message.author} said linux without including GNU, location:\v {message.guild} \t {message.channel}")
            if "stupid bot" in message.content:
                await message.channel.send("Fuck you too")
            if "this is getting annoying" in message.content:
                await message.channel.send("that's the point")
    if linux_list in message.content:
        if gnu_list not in message.content:

            print("on_linux is working") 
            await ctx.trigger_typing
            await message.channel.send("I'd just like to interject for a moment.")
            await message.channel.send("What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. ")
            await message.channel.send("Linux is not an operating system unto itself,\n but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.")
            await message.channel.send('Many computer users run a modified version of the GNU system every day, without realizing it.  Through a peculiar turn of events, the version of GNU which is widely used today is often called "Linux", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.')
            await message.channel.send("There really is a Linux, and these people are using it, but it is just a part of the system they use." )
            await message.channel.send("Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run.")
            await message.channel.send("The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system.")
            await message.channel.send("Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. ")
            await message.channel.send('All the so-called "Linux" distributions are really distributions of GNU/Linux.')
            print(f"{message.author} said linux without including GNU, location:\v {message.guild} \t {message.channel}")


#latency command (ping)
@bot.command()
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1)*1000)
    await ctx.send(f"ping = {ping}ms")
    print("ping command working")

#see if the bot is online
@bot.command()
async def test(ctx):
    await ctx.send('Bot Online')
    print("test command working")

#embeded list of commands
@bot.command()
async def under_construction(message, ctx):
    await ctx.trigger_typing()
    await message.channel.send(f"<@{message.author.id}> hey, it says under construction in the name")
    # discord.Embed(title="commands", description="", color=discord.Color.green())
    # M = ctx.send()
    # await ctx.add_reaction(M, ':flushed:')
    # await ctx.add_reaction(M, ':eyes:')

#use this format for debugging something
# @bot.command()
# async def debug(ctx):
#     print(f'debugging\t start')
#     await ctx.trigger_typing()
#     print(f'debugging\t passed ctx.trigger_typing()')
#     await ctx.send("using ctx.send")
#     print(f'debugging\t passed ctx.send')


#command for CD
@bot.command()
async def pj(ctx):
    #CD's current account (at the time of writing this, it's hand crushed by mallet)
    if ctx.author.id == 761951269115396096:
        await ctx.trigger_typing()
        await ctx.send(":wink:")
    #My curent main account (at the time of writing this, it's hello_there)
    if ctx.author.id == 832581418634313768:
        await ctx.trigger_typing()
        await ctx.send(":eyes:")
    else:
        await ctx.send("no")
    print("pj command working")

@bot.command()
async def test_emoji(ctx, message):
    await message.channel.send("starting emoji test . . .")
    for Emoji in arrow_list:
        await message.channel.send("emoji test")
        await message.add_reaction(Emoji)
    await message.channel.send("finished emoji test")


#info about the bot
@bot.command()
async def info(ctx):
    await ctx.send("This bot was made using the discord.py python module, I made this bot in my spare time and I hope you like it\n\n")

#donate with monero
@bot.command()
async def donate(ctx):
    await ctx.send("if you like the bot or want to help me continue to make more things you can donate XMR to this address:\n " + XMR_donate_addr)


# music
@bot.command()
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()

@bot.command(pass_context=True)
async def play(ctx, url):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = await voice_client.create_ytdl_player(url)
    players[guild.id] = player
    player.start()
    print("play function working")

# leave
@bot.command(pass_contex=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()








#token to make it run
bot.run(token)