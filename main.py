from keep_alive import keep_alive
from datetime import datetime
import pytz
import time
import sched
from replit import db
import threading
from time import sleep
import discord
import asyncio

import os
import random

from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', help_command=None)

client = discord.Client()
prefix = '!'


class Boss:
    def __init__(self, boss, _time, day):
        self.boss = boss
        self._time = _time
        self.day = day


monday_list = [
    Boss("RedNose", "07:00", 0),
    Boss("Mudster", "07:00", 0),
    Boss("Kutum", "09:00", 0),
    Boss("Nouver", "11:00", 0),
    Boss("Karanda", "13:00", 0),
    Boss("Kutum", "15:00", 0),
    Boss("Karanda", "18:30", 0),
    Boss("Nouver", "18:30", 0),
    Boss("Kzarka", "20:30", 0),
    Boss("Karanda", "22:00", 0),
]
tuesday_list = [
    Boss("Bheg", "07:00", 1),
    Boss("DimTree", "07:00", 1),
    Boss("Karanda", "09:00", 1),
    Boss("Kzarka", "11:00", 1),
    Boss("Kutum", "13:00", 1),
    Boss("Karanda", "15:00", 1),
    Boss("Garmoth", "16:00", 1),
    Boss("RedNose", "18:30", 1),
    Boss("Mudster", "18:30", 1),
    Boss("Kutum", "20:30", 1),
    Boss("Nouver", "22:00", 1),
]
wednesday_list = [
    Boss("RedNose", "07:00", 2),
    Boss("Mudster", "07:00", 2),
    Boss("Karanda", "11:00", 2),
    Boss("Nouver", "13:00", 2),
    Boss("Offin", "14:00", 2),
    Boss("Kzarka", "15:00", 2),
    Boss("Bheg", "18:30", 2),
    Boss("DimTree", "18:30", 2),
    Boss("Karanda", "20:30", 2),
    Boss("Kutum", "22:00", 2),
]
thursday_list = [
    Boss("DimTree", "07:00", 3),
    Boss("Bheg", "07:00", 3),
    Boss("Nouver", "09:30", 3),
    Boss("Kutum", "11:00", 3),
    Boss("Nouver", "13:00", 3),
    Boss("Offin", "14:00", 3),
    Boss("Kzarka", "15:00", 3),
    Boss("RedNose", "18:30", 3),
    Boss("Mudster", "18:30", 3),
    Boss("Nouver", "20:30", 3),
    Boss("Kzarka", "22:00", 3),
]
friday_list = [
    Boss("RedNose", "07:00", 4),
    Boss("Mudster", "07:00", 4),
    Boss("Karanda", "09:00", 4),
    Boss("Kutum", "11:00", 4),
    Boss("Nouver", "13:00", 4),
    Boss("Offin", "14:00", 4),
    Boss("Kzarka", "15:00", 4),
    Boss("Garmoth", "16:00", 4),
    Boss("DimTree", "18:30", 4),
    Boss("Bheg", "18:30", 4),
    Boss("Nouver", "20:30", 4),
    Boss("Kzarka", "20:30", 4),
    Boss("Kutum", "22:00", 4),
]
saturday_list = [
    Boss("Kzarka", "06:00", 5),
    Boss("Nouver", "07:00", 5),
    Boss("Kutum", "09:00", 5),
    Boss("Karanda", "13:00", 5),
    Boss("Kutum", "15:00", 5),
    Boss("Garmoth", "16:00", 5),
    Boss("Mudster", "18:30", 5),
    Boss("RedNose", "18:30", 5),
    Boss("DimTree", "20:30", 5),
    Boss("Bheg", "20:30", 5),
    Boss("Kzarka", "22:00", 5),
]
sunday_list = [
    Boss("Karanda", "06:00", 6),
    Boss("Kutum", "07:00", 6),
    Boss("Kzarka", "09:00", 6),
    Boss("Kutum", "11:00", 6),
    Boss("DimTree", "13:00", 6),
    Boss("Bheg", "13:00", 6),
    Boss("Vell", "14:00", 6),
    Boss("Nouver", "15:00", 6),
    Boss("Kzarka", "15:00", 6),
    Boss("Garmoth", "16:00", 6),
    Boss("RedNose", "18:30", 6),
    Boss("Mudster", "18:30", 6),
    Boss("Karanda", "20:30", 6),
    Boss("Kzarka", "20:30", 6),
    Boss("Nouver", "22:00", 6),
]

day_list = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
status_list = [
    "Kzarka",
    "Karanda",
    "Vell",
    "Garmoth",
    "Red Nose",
    "Dim Tree Spirit",
    "Offin",
    "Kutum",
    "Nouver",
    "Mudster",
    "Bheg",
    "Black Spirit",
    "Griffon",
    "Muskan",
]
boss_list = [
    "kzarka",
    "karanda",
    "vell",
    "garmoth",
    "rednose",
    "dimtree",
    "offin",
    "kutum",
    "nouver",
    "mudster",
    "bheg",
]

icon_list = {
    "karanda": "https://imgur.com/OVOrFZR.png",
    "kzarka": "https://imgur.com/95OFQTe.png",
    "nouver": "https://imgur.com/Kt5EOxS.png",
    "kutum": "https://imgur.com/Ip4i2oa.png",
    "garmoth": "https://imgur.com/P9MjV5A.png",
    "offin": "https://imgur.com/mAzQglC.png",
    "vell": "https://imgur.com/TfeSrVn.png",
    "bheg": "https://imgur.com/GI59dGr.png",
    "dimtree": "https://imgur.com/5F9SMhe.png",
    "mudster": "https://imgur.com/H3Wdmnf.png",
    "rednose": "https://imgur.com/uyChweO.png",
}
color_list = {
    "karanda": 0xdedcd7,
    "kzarka": 0xff0000,
    "nouver": 0xffaa00,
    "kutum": 0xaa00ff,
    "garmoth": 0xff4000,
    "offin": 0x00c8ff,
    "vell": 0x007bff,
    "bheg": 0x754105,
    "dimtree": 0x036910,
    "mudster": 0x727136,
    "rednose": 0x86040d,
}

array_list = []
temp_list = []
temp = []

day_sec = 86400
UTC = pytz.utc
utc = datetime.now(UTC)
cur_day = utc.weekday()
cur_day_sec = (cur_day * day_sec)
cur_seconds = (utc.hour * 3600) + (utc.minute * 60) + utc.second + cur_day_sec

#returns the time and day given as seconds 
#day number multiplied with day_sec and it converts current time to seconds and returns it
def get_time_as_sec(day, _time):
  # 0 -> Monday | ... |6 -> Sunday
  h = int(_time.split(":")[0])
  m = int(_time.split(":")[1])
  result = (h * 3600) + (m * 60) + (day * day_sec)
  return result

#rounds the number given to 60 if it is higher than 30 cuz round function it self is only rounds to 1,10,100 
def round_60(value):
  a = (int(value) % 60)
  b = int(value) - a
  if a <= 30: a = 0
  elif a > 30: a = 60
  return b + a

#converts the given boss and value left to spawn as seconds to view value as bot posts it to boss-info channel
def convert(boss, value):
  rounded = int(round_60(value))
  if rounded <= 0: return False
  elif rounded < 60 and rounded > 0 or rounded / 60 == 0:
      return boss.upper() + " in " + str(rounded) + " sec"
  elif rounded < 3600 and rounded > 60:
      return boss.upper() + " in " + str(int(rounded / 60)) + " mins"
  elif rounded > 3600:
    if rounded < 7200: 
      return boss.upper() + " in " + str(int(rounded / 3600)) + " hour and " + str(int((rounded % 3600) / 60)) + " mins"
    return boss.upper() + " in " + str(int(rounded / 3600)) + " hours and " + str(int((rounded % 3600) / 60)) + " mins"

#returns the icon link for the given boss name 
def get_icon_link(boss):
  for x in icon_list:
      if x.split()[0] == boss.lower():
          return x.split()[1]

#returns the view text to bot for !calendar command it will change the times as given timezone value
def get_all_list(val):
  value = int(val)
  array_list.clear()
  view_list = ""
  view_list = ">>> **ALL BOSS TIMES LIST (GMT " + str(value) + ")**\n"
  i = 0
  y = 0
  temp_list = []

  while y < 7:
      if y == 0:
          view_list += "\n**Monday**```css\n"
          temp_list = monday_list.copy()
      elif y == 1:
          view_list += "```\n**Tuesday**```css\n"
          temp_list = tuesday_list.copy()
      elif y == 2:
          view_list += "```\n**Wednesday**```css\n"
          temp_list = wednesday_list.copy()
      elif y == 3:
          view_list += "```\n**Thursday**```css\n"
          temp_list = thursday_list.copy()
      elif y == 4:
          view_list += "```\n**Friday**```css\n"
          temp_list = friday_list.copy()
      elif y == 5:
          view_list += "```\n**Saturday**```css\n"
          temp_list = saturday_list.copy()
      elif y == 6:
          view_list += "```\n**Sunday**```css\n"
          temp_list = sunday_list.copy()
      for x in temp_list:
          h = int(x._time.split(":")[0])
          m = x._time.split(":")[1]
          added_tz = h + value
          if added_tz >= 24: 
            gmt = str(added_tz - 24) + ":" + m
            array_list.append(x.boss + " at " + gmt + " (next day)")
          elif added_tz < 0:
            gmt = str(added_tz + 24) + ":" + m
            array_list.append(x.boss + " at " + gmt + " (previous day)")
          else: 
            gmt = str(added_tz) + ":" + m
            array_list.append(x.boss + " at " + gmt)
          view_list += array_list[i] + "\n"
          i += 1
      y += 1
  return view_list + "```"

#returns todays bosses that hasnt been spawned and next days bosses
def get_boss_list():
    day_sec = 86400
    UTC = pytz.utc
    utc = datetime.now(UTC)
    cur_day = utc.weekday()
    cur_seconds = (utc.hour * 3600) + (utc.minute *  60) + utc.second + (cur_day * day_sec)

    array_list.clear()
    temp_list = []
    temp_list2 = []
    if cur_day == 0:
        temp_list = monday_list.copy()
        temp_list2 = tuesday_list.copy()
    elif cur_day == 1:
        temp_list = tuesday_list.copy()
        temp_list2 = wednesday_list.copy()
    elif cur_day == 2:
        temp_list = wednesday_list.copy()
        temp_list2 = thursday_list.copy()
    elif cur_day == 3:
        temp_list = thursday_list.copy()
        temp_list2 = friday_list.copy()
    elif cur_day == 4:
        temp_list = friday_list.copy()
        temp_list2 = saturday_list.copy()
    elif cur_day == 5:
        temp_list = saturday_list.copy()
        temp_list2 = sunday_list.copy()
    elif cur_day == 6:
        temp_list = sunday_list.copy()
        temp_list2 = monday_list.copy()
    for x in temp_list:
        sec = get_time_as_sec(cur_day, x._time)
        left = sec - cur_seconds
        if left < 0: continue
        array_list.append(x.boss + " " + str(left) + " " + str(x.day))

    for x in temp_list2:
        sec = get_time_as_sec(cur_day + 1, x._time)
        left = sec - cur_seconds
        array_list.append(x.boss + " " + str(left) + " " + str(x.day))

    return array_list

#converts get_boss_list arraylist to discord text
def get_view(value):
    temp = value
    view_list = ""
    li = []
    for x in temp:
        boss = x.split()[0]
        left = int(float(x.split()[1]))
        y = convert(boss, left)
        if y is not False: li.append(y)
    
    for x in li: view_list += str(x) + "\n"

    view_list = "```css\n" + view_list + "```"
    return view_list

#used at notify loop check it will check if theres boss before the given time as minute
def get_lessthen(value):  #value must be minute
    
    li = get_boss_list()
    temp = []
    for x in li:
        left = int(x.split()[1])
        if left < 0: continue
        elif left > (value * 60) + 15 or left < (value * 60) - 15: continue
        temp.append(x)
    return temp
    

#returns the id of channel named boss-notifications
def ntf_ch_id():
    for server in bot.guilds:
        for channel in server.channels:
            if str(channel.type) == 'text':
                if channel.name == "boss-notifications":
                    return channel.id

#returns the id of channel named boss-info
def info_ch_id():
    for server in bot.guilds:
        for channel in server.channels:
            if str(channel.type) == 'text':
                if channel.name == "boss-info":
                    return channel.id

#returns the given boss name role id in order to tag
def get_boss_role_id(bossname):
    if bossname.lower() in boss_list:
        for server in bot.guilds:
            for role in server.roles:
                if role.name.lower() == bossname.lower():
                    return role.id
    return False

#returns the list of all spawn times for given boss name
def get_one_boss_list(boss):
    all_list = monday_list + tuesday_list + wednesday_list + thursday_list + friday_list + saturday_list + sunday_list
    day_sec = 86400
    UTC = pytz.utc
    utc = datetime.now(UTC)
    cur_day = utc.weekday()
    cur_seconds = (utc.hour * 3600) + (utc.minute *      60) + utc.second + (cur_day * day_sec)
    temp = []
    temp2 = []
    for x in all_list:
        if x.boss.lower() != boss.lower() and boss != "all": continue
        sec = get_time_as_sec(x.day, x._time)
        left = sec - cur_seconds
        if left <= 0:
            sec += 604800
            left = sec - cur_seconds
            temp2.append(x.boss + " " + str(left) + " " + str(x.day))
            continue
        temp.append(x.boss + " " + str(left) + " " + str(x.day))
    if boss == "all":
        temp2 = temp2[:5]
    for x in temp2:
        temp.append(x)
    return temp

#boss-info channel loop refreshes every min
@tasks.loop(minutes=1)
async def info_loop():
    timer_exact.cancel()
    info_channel = bot.get_channel(info_ch_id())
    await info_channel.purge(limit=2)
    ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    x = discord.Embed(title="BOSS TIMES LIST | " + str(ctime) + " UTC", description=get_view(get_boss_list()), color=0xffffff)
    await info_channel.send(embed=x)

#boss-notifications loop checks every min
@tasks.loop(minutes=1)
async def notify_loop_v4():
  _channel = bot.get_channel(ntf_ch_id())

  temp0 = get_lessthen(0)
  temp5 = get_lessthen(5)
  temp15 = get_lessthen(15)
  temp = []
  if len(temp0) != 0: temp = temp0
  elif len(temp5) != 0: temp = temp5
  elif len(temp15) != 0: temp = temp15

  if len(temp) != 0:
    for x in temp:
      if temp == temp5 or temp == temp0:
        await _channel.purge(limit=len(temp))

      boss = x.split()[0]
      left = x.split()[1]
      bossurl = icon_list[boss.lower()]
      _color = color_list[boss.lower()]
      _title = boss.upper() + " will spawn in " + str(int(round_60(left) / 60)) + " mins"
      if temp == temp0:  _title = boss.upper() + " spawned"

      embedVar = discord.Embed(title=_title, description="", color=_color)
      embedVar.set_image(url=bossurl)
      tag = "<@&" + str(get_boss_role_id(boss.lower())) + ">"
      await _channel.send(tag, embed=embedVar)
      print("notif sent")
  else:
    print("nothing yet: " + str(datetime.now(UTC).strftime("%m-%d %H:%M")))

#starts info and notify loop at exact 00 seconds
@tasks.loop(seconds=1)
async def timer_exact():
  UTC = pytz.utc
  sec = int(datetime.now(UTC).strftime("%S"))
  if sec == 00:
    print("Info Loop Started!")
    info_loop.start()
    print("Notif v4 Loop Started!")
    notify_loop_v4.start()
    timer_exact.stop()

#changes boss status every 10 mins
@tasks.loop(minutes=10)
async def change_status():
    game = discord.Game("with " + random.choice(status_list))
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    game = discord.Game("with Kzarka")
    await bot.change_presence(status=discord.Status.online, activity=game)
    info_channel = bot.get_channel(info_ch_id())
    await info_channel.purge(limit=2)
    ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    x = discord.Embed(title="BOSS TIMES LIST | " + str(ctime) + " UTC",  description=get_view(get_boss_list()),color=0xffffff)
    await info_channel.send(embed=x)
    db["msg_ntf"] = 0
    timer_exact.start()
    change_status.start()


@bot.event
async def on_message(ctx):
    msg = ctx.content.casefold()
    if ctx.author == client.user:
        return
  
    else:
        if msg == prefix + 'boss':
            ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
            x = discord.Embed(title="BOSS TIMES LIST | " + str(ctime) + " UTC +0",   description=get_view(get_boss_list()),color=0xffffff)
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(embed=x)
            if str(ctx.channel.type) != 'private':
                await ctx.delete()
                await ctx.channel.send(ctx.author.mention + ' check your DM\'s!', delete_after=10.0)

        elif msg.startswith(prefix + 'calendar'):
            check = str(ctx.channel.type) != 'private'
            gmt = str(msg.lstrip("!calendar"))
            if gmt == "": gmt = 0
            try:
                gmt = int(gmt)
            except:
                if check: await ctx.delete()
                await ctx.channel.send(ctx.author.mention + " please enter a valid number", delete_after=10.0)
                return
            if gmt < -12 or gmt > 13:
                if check: await ctx.delete()
                await ctx.channel.send(ctx.author.mention + " please enter a valid number", delete_after=10.0)
                return
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(get_all_list(gmt))
            if check:
                await ctx.delete()
                await ctx.channel.send(ctx.author.mention + ' check your DM\'s!', delete_after=10.0)

        elif msg.startswith(prefix + 'boss'):
            check = str(ctx.channel.type) != 'private'
            boss = str(msg.lstrip("!boss")).strip().lower()
            if boss in boss_list:
                ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
                x = discord.Embed(title=boss.upper() + " BOSS TIMES LIST | " +  str(ctime) + " UTC",  description=get_view( get_one_boss_list(boss)),   color=0xffffff)
                await ctx.author.create_dm()
                await ctx.author.dm_channel.send(embed=x)
                if check:
                    await ctx.delete()
                    await ctx.channel.send(ctx.author.mention +  ' check your DM\'s!', delete_after=10.0)

            else:
                await ctx.channel.send(ctx.author.mention +' please enter a valid boss name.', delete_after=10.0)

        
        elif msg == prefix + 'help':
            x = discord.Embed(title="Here is some commands you can use;", color=0xffffff)
            x.add_field(
                name="!calendar *TIMEZONE*",
                value=
                "I will DM you with all boss spawn times. Enter timezone as number value.",
                inline=False)
            x.add_field(
                name="!boss",
                value=
                "I will DM you with bosses remaining time to spawn also you can find that information in here <#850077285356535839>",
                inline=False)
            x.add_field(
                name="!boss *ANYBOSSNAME*",
                value=
                "I will DM you with the boss list that you wrote and their remaining time to spawn.",
                inline=False)
            x.set_footer(
                text=
                "This bot is running on development server so bot reactions may be slow"
            )
            await ctx.channel.send(embed=x)

        elif msg == prefix + "shutdown" and ctx.author.id == 174213672535588864:
            await client.close()
            print("Bot logged out")


keep_alive()
bot.run(os.getenv("TOKEN"))
