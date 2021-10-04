import discord, os, pafy
from discord.ext import commands
from discord.ext.commands import bot
from time import sleep
from ydl import *
from collections import deque
bot = commands.Bot(command_prefix="겜!동 노래 ")

song_list=deque([])
voice=None

def youtube():
    global song_list
    name=[]
    for i in range(len(song_list)):
        info=pafy.new(song_list[i])
        name.append(info.title)
    return name

def play_next(ctx):
    global song_list, voice
    play(ctx,song_list[0])

def play(ctx,ur):
    global song_list
    if ur==None:
        print("")
    else:
        song_list.append(ur)
    if len(song_list) < 1:
        return
    url=song_list[0]
    channel = ctx.author.voice.channel
    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        voice=bot.voice_clients[0]
        if bot.voice_clients[0].is_playing():
            print("")
        else:
            song_list.popleft()
            voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))
    except:
        song_list.popleft()
@bot.event
async def on_message(ctx):
    global song_list
    if "888802297356886036"==str(ctx.channel.id):
        if ctx.content==("skip"):
            voice = bot.voice_clients[0]
            voice.pause()
            await ctx.delete()
            play(ctx,None)
        elif ctx.content==("leave"):
            await bot.voice_clients[0].disconnect()
        elif ctx.content==("stop"):
            voice = bot.voice_clients[0]
            voice.pause()
        elif ctx.content.find("youtube") or ctx.content.find("yotu.be"):
            if bot.voice_clients == []:
                await ctx.author.voice.channel.connect()
            play(ctx,ctx.content)
        elif ctx.content==("list"):
            names=youtube()
            embed=discord.Embed(title="재생목록", description="재생목록", color="0x62c1cc")
            for i in range(names):
                embed.add_field(name=str(i), value=names[i])
            await ctx.send(embed=embed)
        await ctx.delete()
        print(song_list)
    else:
        return 0

bot.run(os.environ['token'])
