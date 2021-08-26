from keep_alive import keep_alive
from datetime import datetime
import pytz
import discord
import os
import random
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import fnc

load_dotenv()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)
client = discord.Client()
prefix = '!'

UTC = pytz.utc
utc = datetime.now(UTC)

def get_text_ch_id(name):
  for server in bot.guilds:
    for channel in server.channels:
        if str(channel.type) == 'text':
            if channel.name.lower() == name.lower():
              return channel.id

#returns the given boss name role id in order to tag
def get_role_id(rolename,c):
    if c == 1 or rolename.lower() in fnc.boss_list :
        for server in bot.guilds:
            for role in server.roles:
                if role.name.lower() == rolename.lower():
                    return role.id
    return False

##########################################################
################# BOT LOOPS ##############################
##########################################################

#boss-info channel loop refreshes every min
@tasks.loop(minutes=1)
async def info_loop():
    timer_exact.cancel()
    info_channel = bot.get_channel(get_text_ch_id("boss-info"))
    await info_channel.purge(limit=5)
    ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    x = discord.Embed(title="BOSS TIMES LIST | " + str(ctime) + " UTC", description=fnc.get_view(fnc.get_boss_list()), color=0xffffff)
    await info_channel.send(embed=x)

#boss-notifications loop checks every min
@tasks.loop(minutes=1)
async def notify_loop_v4():
  _channel = bot.get_channel(get_text_ch_id("boss-notifications"))

  temp0 = fnc.get_lessthen(0)
  temp5 = fnc.get_lessthen(5)
  temp15 = fnc.get_lessthen(15)
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
      bossurl = fnc.icon_list[boss.lower()]
      _color = fnc.color_list[boss.lower()]
      _title = boss.upper() + " will spawn in " + str(int(fnc.round_60(left) / 60)) + " mins"
      if temp == temp0:  _title = boss.upper() + " spawned"

      embedVar = discord.Embed(title=_title, description="", color=_color)
      embedVar.set_image(url=bossurl)
      tag = "<@&" + str(get_role_id(boss.lower(),0)) + ">"
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
    game = discord.Game("with " + random.choice(fnc.status_list))
    await bot.change_presence(status=discord.Status.online, activity=game)

##########################################################
################# BOT EVENTS #############################
##########################################################
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

    info_channel = bot.get_channel(get_text_ch_id("boss-info"))    
    await info_channel.purge(limit=2)
    ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    x = discord.Embed(title="BOSS TIMES LIST | " + str(ctime) + " UTC",  description=fnc.get_view(fnc.get_boss_list()),color=0xffffff)
    await info_channel.send(embed=x)

    timer_exact.start()
    change_status.start()

@bot.event 
async def on_member_join(member):
  await member.send('**EN**\n**Welcome to Melissia Boss Timer discord server!**\nIn order to get notified you have to go to <#851464537479315557> channel and react to the roles with the name of bosses you want to get notified. Enjoy not missing any boss!\nUse !help command in server to get more information.\n\n*This is not made by Melissia Games developers.*\n\n**TR**\n**Melissia Boss Timer discord sunucusuna hoşgeldiniz!**\nBildirim almak için <#851464537479315557> kanalına gidip istediğiniz boss isimlerinin olduğu rollere tepki veriniz. Hiçbir bossu kaçırmamanın tadını çıkarın!\n!help komutunu kullanarak daha fazla bilgi edinebilirsiniz.\n\n*Bu bot Melissia Games geliştiricileri tarafından yapılmamıştır.*\n\n**RU**\n**Добро пожаловать на сервер разногласий Melissia Boss Timer! **\nЧтобы получить уведомление, вам нужно перейти на канал <#851464537479315557> и реагировать на роли, указав имена боссов, которых вы хотите получать. Наслаждайтесь, не пропуская ни одного босса! \n Используйте команду! help на сервере, чтобы получить дополнительную информацию.\n\n*Это сделано не разработчиками Melissia Games.*\n\n*Переведено с помощью Google Translate*')
  role = discord.utils.get(member.guild.roles, id=get_role_id("member",1))
  await member.add_roles(role)


##########################################################
################# BOT COMMANDS ###########################
##########################################################

@bot.command(name="help",pass_context=True)
async def help(ctx):
  try: await ctx.message.delete()
  except: None
  x = discord.Embed(title="Here is some commands you can use;", color=0xffffff)
  x.add_field(
      name="!calendar *TIMEZONE*",
      value=
      "I will DM you with all boss spawn times. Enter timezone as number value.",
      inline=False
      )
  x.add_field(
      name="!boss",
      value=
      "I will DM you with bosses remaining time to spawn also you can find that information in here <#850077285356535839>",
      inline=False
      )
  x.add_field(
      name="!boss *ANYBOSSNAME*",
      value=
      "I will DM you with the boss list that you wrote and their remaining time to spawn.",
      inline=False
      )
  x.add_field(
    name="!invite",
    value="I will give you permanent invite link of this server"
  )
  x.set_footer(
      text=
      "This bot is running on development server so bot reactions may be slow"
  )  
  await ctx.channel.send(embed=x)


@bot.command(name="invite",pass_context=True)
async def invite(ctx):
  try: await ctx.message.delete()
  except: None
  await ctx.channel.send("https://discord.gg/9CYzgrEpyj")


@bot.command(name="boss",pass_context=True)
async def boss(ctx):
  bossname = str(ctx.message.content.lstrip("!boss").strip().lower())
  ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
  try: await ctx.message.delete()
  except: None
  if bossname == "":
    x = discord.Embed(title="BOSS TIMES LIST | " + str(ctime) + " UTC",   description=fnc.get_view(fnc.get_boss_list()),color=0xffffff)
  elif bossname in fnc.boss_list:          
    x = discord.Embed(title=bossname.upper() + " BOSS TIMES LIST | " +  str(ctime) + " UTC",  description=fnc.get_view(fnc.get_one_boss_list(bossname)), color=0xffffff)
  else: 
    await ctx.channel.send(ctx.author.mention + ' please enter correct boss name.',delete_after=10.0)
    return

  await ctx.author.create_dm()
  await ctx.author.dm_channel.send(embed=x)

  if str(ctx.channel.type) != 'private':     
    await ctx.channel.send(ctx.author.mention + ' check your DM\'s!',delete_after=10.0)



@bot.command(name="shutdown",pass_context=True)
async def shutdown(ctx):
  try: 
    await ctx.message.delete()
  except: None
  if ctx.author.id == 174213672535588864 or ctx.author.id == 654780853414789153:
    await bot.close()
    print("Bot logged out")
  else: await ctx.channel.send("You don't have permission to do this.",delete_after=10.0 )

@bot.command(name="refreshcalendar",pass_context=True)
async def refreshcalendar(ctx):
  cal_ch = bot.get_channel(get_text_ch_id("calendar"))    
  await cal_ch.purge(limit=5)  
  await cal_ch.send(embed=fnc.get_all_embed("BOSS CALENDAR (UTC)",0))


@bot.command(name="calendar",pass_context=True)
async def calendar(ctx):
  _timezone = str(ctx.message.content.lstrip("!calendar"))
  dm_check = str(ctx.channel.type) != 'private'
  if dm_check: 
    await ctx.message.delete()
  if _timezone != "": 
    try: _timezone = int(_timezone)
    except: 
      await ctx.channel.send(ctx.author.mention + " please enter a valid number", delete_after=10.0)
      return
    if _timezone < -12 or _timezone > 13:    
      await ctx.channel.send(ctx.author.mention + " please enter a valid number", delete_after=10.0)
      return
  else: _timezone = 0

  if _timezone < 0: _title = "BOSS CALENDAR (UTC " + str(_timezone) +")"
  elif _timezone > 0: _title = "BOSS CALENDAR (UTC +" + str(_timezone) +")"
  elif _timezone == 0: _title = "BOSS CALENDAR (UTC)"
  

  await ctx.author.create_dm()
  await ctx.author.dm_channel.send(embed=fnc.get_all_embed(_title,_timezone))
  
  if dm_check:      
    await ctx.channel.send(ctx.author.mention + ' check your DM\'s!', delete_after=10.0)


#BOT RUN
keep_alive()
bot.run(os.getenv("TOKEN"))