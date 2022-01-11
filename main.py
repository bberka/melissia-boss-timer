from keep_alive import keep_alive
from datetime import datetime
import pytz
import discord
import os
import random
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import cmd,var

load_dotenv()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)
client = discord.Client()
prefix = '!'

UTC = pytz.utc
utc = datetime.now(UTC)

def GetTextChIDbyName(name):
  for server in bot.guilds:
    for channel in server.channels:
        if str(channel.type) == 'text':
            if channel.name.lower() == name.lower():
              return channel.id

#returns the given boss name role id in order to tag
def GetRoleIDbyName(rolename):
  if rolename.lower() in var.boss_list :
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
async def BossInfoLoop():      
  info_channel = bot.get_channel(GetTextChIDbyName("boss-info"))
  await info_channel.purge(limit=5)
  ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
  x = discord.Embed(
    title=f"BOSS TIMES LIST | {ctime} UTC", 
    description=cmd.GetDiscordText(cmd.GetBossInfo(0)), 
    color=0xffffff)
  await info_channel.send(embed=x)


#boss-notifications loop checks every min
@tasks.loop(minutes=1)
async def BossNotifyCheckLoop():  
  channel = bot.get_channel(GetTextChIDbyName("boss-notifications"))
  temp = cmd.GetSpawn()
  
  if not temp: 
    print(f'No boss yet: {datetime.now(UTC).strftime("%m-%d %H:%M")}')
    return 0        
  
  for x in temp:
    boss = x.split()[0]
    left = int(x.split()[1])
    for y in var.boss_list:
      if boss == y.name: 
        bosicon = y.icon
        color = y.color

    title =  f"{boss.upper()} will spawn in {int(cmd.RoundTo60(left) / 60)} mins"      
    if -20 <  left < 360: 
      await channel.purge(limit=len(temp))
      if left < 20: title =  f"{boss.upper()} spawned"      
    
    embedVar = discord.Embed(
      title=title, 
      description="", 
      color=color
      ).set_image(url=bosicon)
    tag = f"<@&{str(GetRoleIDbyName(boss.lower()))}>"

    await channel.send(tag, embed=embedVar)    
    print(f"Notification sent {boss} : {left}")
  
    
    

#starts info and notify loop at exact 00 seconds
@tasks.loop(seconds=1)
async def BossTimerExact():  
  sec = int(datetime.now(UTC).strftime("%S"))
  if sec == 00:
    print("Info Loop Started!")
    BossInfoLoop.start()
    print("Notify v4 Loop Started!")
    BossNotifyCheckLoop.start()
    BossTimerExact.stop()

#changes boss status every 10 mins
@tasks.loop(minutes=10)
async def ChangeStatus():
    game = discord.Game(f"with {random.choice(var.status_list)}")
    await bot.change_presence(status=discord.Status.online, activity=game)

##########################################################
################# BOT EVENTS #############################
##########################################################
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    BossTimerExact.start()
    ChangeStatus.start()
   

@bot.event 
async def on_member_join(member):
  await member.send(var.welcome_message)
  role = discord.utils.get(
    member.guild.roles, 
    id=851464964279238666)
  await member.add_roles(role)


##########################################################
################# BOT COMMANDS ###########################
##########################################################

@bot.command(name="help",pass_context=True)
async def help(ctx):
  if str(ctx.channel.type) != 'private': await ctx.message.delete()  
  x = discord.Embed(title="Here is some commands you can use;", color=0xffffff)
  x.add_field(
    name="!calendar *TIMEZONE*",
    value=
    "I will DM you with all boss spawn times. Enter timezone as number value.",
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
  if str(ctx.channel.type) != 'private': await ctx.message.delete()  
  await ctx.channel.send("https://discord.gg/9CYzgrEpyj")



@bot.command(name="boss",pass_context=True)
async def boss(ctx):
  bossname = str(ctx.message.content.lstrip("!boss").strip().lower())
  ctime = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
  
  if cmd.BossnameCheck(bossname):            
    x = discord.Embed(
      title= f"{bossname.upper()} BOSS TIMES LIST | {ctime} UTC",  
      description=cmd.GetDiscordText(cmd.GetBossInfo(bossname)), 
      color=0xffffff)
  else: 
    await ctx.channel.send(f'{ctx.author.mention} please enter correct boss name.',delete_after=10.0)
    return

  await ctx.author.create_dm()
  await ctx.author.dm_channel.send(embed=x)

  if str(ctx.channel.type) != 'private':  
    await ctx.message.delete()     
    await ctx.channel.send(f'{ctx.author.mention} check your DM\'s!',delete_after=10.0)



@bot.command(name="shutdown",pass_context=True)
async def shutdown(ctx):
  if str(ctx.channel.type) != 'private': await ctx.message.delete()   
  if ctx.author.id == 174213672535588864 or ctx.author.id == 654780853414789153:
    await bot.close()
    print("Bot logged out")

@bot.command(name="refreshcalendar",pass_context=True)
async def refreshcalendar(ctx):
  if ctx.author.id == 174213672535588864 or ctx.author.id == 654780853414789153:
    cal_ch = bot.get_channel(GetTextChIDbyName("calendar"))    
    await cal_ch.purge(limit=5)  
    await cal_ch.send(embed=cmd.GetCalendarEmbed("BOSS CALENDAR (UTC)",0))


@bot.command(name="calendar",pass_context=True)
async def calendar(ctx):
  timez = str(ctx.message.content.lstrip("!calendar").strip())
  if timez == "": timez = 0
  try: timez = int(timez)
  except: None
  if type(timez) is int and- 12 < timez < 13:  
    if timez < 0: title = f"(UTC {str(timez)})"
    elif timez > 0: title = f" (UTC +{str(timez)})"
    elif timez == 0: title = "(UTC)"
  else: 
    await ctx.channel.send(f"{ctx.author.mention} please enter a valid number", delete_after=10.0)
    return 0

  await ctx.author.create_dm()
  await ctx.author.dm_channel.send(embed=cmd.GetCalendarEmbed(f"BOSS CALENDAR {title}",timez))
  
  if str(ctx.channel.type) != 'private':   
    await ctx.message.delete()   
    await ctx.channel.send(f'{ctx.author.mention} check your DM\'s!', delete_after=10.0)


#BOT RUN
keep_alive()
bot.run(os.getenv("TOKEN"))