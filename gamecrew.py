import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import bot
import os

bot = commands.Bot(command_prefix="겜!동 ")

dir = "./Games"

@bot.event
async def on_ready():
  print("이등몸장")
  if not os.path.isdir(dir):
    print("게임 파일을 생성합니다.")
    os.mkdir(dir)

@bot.command(name="명령어")
async def 명령어(ctx):
  embed = discord.Embed(title="GameCrew Bot 명령어", color=0x62c1cc)
  embed.set_author(name="GameCrew")
  embed.set_footer(text="GameCrew")
  embed.add_field(name="겜!동 목록", value="등록된 게임들을 보여줍니다", inline=False)
  embed.add_field(name="겜!동 선호 (게임이름)", value="등록된 게임을 선호합니다", inline=False)
  embed.add_field(name="겜!동 선호삭제 (게임이름)", value="게임을 선호하지 않습니다.", inline=False)
  embed.add_field(name="겜!동 선호자 (게임이름)", value="등록된 게임을 선호하는 사람을 보여줍니다.", inline=False)
  await ctx.send(embed=embed)

@bot.command(name="목록")
async def 목록(ctx):
  games = os.listdir(dir)
  embed = discord.Embed(title="게임목록", color=0x62c1cc)
  embed.set_author(name="GameCrew")
  embed.set_footer(text="GameCrew")
  for i in range(len(games)):
    embed.add_field(name=games[i], value="게임", inline=False)
  await ctx.send(embed=embed)

@bot.command(name="게임등록")
async def 게임등록(ctx,*,text):
  if ctx.author.guild_permissions.administrator:
    filepath=dir+"/"+text
    if os.path.isfile(filepath):
      await ctx.send(text+"은(는) 이미 등록된 게임입니다.")
    else:
      gamefile=open(filepath,'w')
      await ctx.send(text+"을(를) 등록했습니다!")
      gamefile.close()
  else:
    await ctx.send("당신은 권한이 없습니다.")

@bot.command(name="게임삭제")
async def 게임삭제(ctx,*,text):
  if ctx.author.guild_permissions.administrator:
    filepath=dir+"/"+text
    if not os.path.isfile(filepath):
      await ctx.send(text+"은(는) 존재하지 않습니다.")
    else:
      os.remove(filepath)
      await ctx.send(text+"을(를) 삭제했습니다.")
  else:
    await ctx.send("당신은 권한이 없습니다.")

@bot.command(name="선호")
async def 선호(ctx,*,text):
  filepath=dir+"/"+text
  if not os.path.isfile(filepath):
    await ctx.send(text+"은(는) 존재하지 않습니다.")
  else:
    if open(filepath, 'r').read().find(str(ctx.author.nick)) == 0:
      await ctx.send("이미 "+text+"을(를) 선호 하고있습니다.")
    else:
      gamefile=open(filepath,"a")
      gamefile.write(str(ctx.author.nick)+"\n")
      await ctx.send(text+"에 선호를 추가했습니다.")
      gamefile.close()

@bot.command(name="선호삭제")
async def 선호삭제(ctx,*,text):
  filepath=dir+"/"+text
  if not os.path.isfile(filepath):
    await ctx.send(text+"은(는) 존재하지 않습니다.")
  else:
    if open(filepath, 'r').read().find(str(ctx.author.nick)) == -1:
      await ctx.send("당신은"+text+"을(를) 선호 하고있지 않습니다.")
    else:
      with open(filepath, 'r') as infile:
        data = infile.readlines()
        infile.close()
      with open(filepath, 'w') as outfile:
        for i in data:
          if not i.startswith(str(ctx.author.nick)):
            outfile.write(i)
        outfile.close()
      await ctx.send("이제 "+text+"을(를) 선호하지 않습니다.")
      

@bot.command(name="선호자")
async def 선호자(ctx,*,text):
  filepath=dir+"/"+text
  if not os.path.isfile(filepath):
    await ctx.send(text+"은(는) 존재하지 않습니다.")
  else:
    file=open(filepath,'r')
    names=file.readlines()
    if len(names) == 0:
      await ctx.send("선호하는 사람이 없습니다.")
    else:
      titlename=text+"을(를) 선호하는 사람들"
      embed = discord.Embed(title=titlename, color=0x62c1cc)
      embed.set_author(name="GameCrew")
      embed.set_footer(text="GameCrew")
      for i in range(len(names)):
        embed.add_field(name=names[i], value="동아리 맴버", inline=False)
      await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("제대로된 명령어를 입력해주세요.")
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("게임명을 입력해주세요")

bot.run(os.environ['token'])