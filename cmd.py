from datetime import datetime
import pytz
import discord 
import var

##########################################################
################# BOT FUNCTIONS ##########################
##########################################################
day_sec = 86400
UTCZ = pytz.utc
utc = datetime.now(UTCZ)
cur_day = utc.weekday()
cur_day_sec = (cur_day * day_sec)
cur_seconds = (utc.hour * 3600) + (utc.minute * 60) + utc.second + cur_day_sec

# updates global time variables 
def UpdateTime():
  global utc
  global cur_day
  global cur_day_sec
  global cur_seconds
  utc = datetime.now(UTCZ)
  cur_day = utc.weekday()
  cur_day_sec = (cur_day * day_sec)
  cur_seconds = (utc.hour * 3600) + (utc.minute * 60) + utc.second + cur_day_sec


# if value == 0 => returns todays tomorrows spawnlist
# if value == ANYBOSSNAME => returns boss named weekly list
def GetBossInfo(val): 
  def _GetBossDayList(val): # gets given days list 
    if val > 6 : val = val % 6  
    temp = []
    for x in var.timer_list:
      if x.day == val: temp.append(x)
    return temp
  
  global cur_day
  UpdateTime()  

  def _GetBossNamedList(boss):
    UpdateTime()
    array_list = []
    temp = []
    for index in list(range(7)):    
      for x in _GetBossDayList(cur_day + index):
        if x.boss.lower() != boss.lower() : continue
        sec = GetGivenTimeAsSecond(x.day, x._time)
        left = sec - cur_seconds
        if left <= 0: 
          left += 604800     
          temp.append(f"{x.boss} {left} {x.day}")   
        else: array_list.append(f"{x.boss} {left} {x.day}")        
    return array_list + temp

  def _GetBossList():
    global cur_day
    UpdateTime()  
    temp = []
    for x in _GetBossDayList(cur_day) + _GetBossDayList(cur_day + 1) :  
      UpdateTime()
      if cur_day != x.day : cur_day+=1             
      sec = GetGivenTimeAsSecond(cur_day, x._time)    
      left = sec - cur_seconds
      if left < -15: continue
      temp.append(f"{x.boss} {left} {x.day}")
    return temp

  if val: return _GetBossNamedList(val)
  else: return _GetBossList()



# converts given [boss, timelefttospawn] array to discord text 
def GetDiscordText(value):    
  #rounds the number given to 60 if it is higher than 30 else 0
  #converts the given boss and value left to spawn as seconds to view value as bot posts it to boss-info channel
  def _ConvertRow(boss, value):
    rounded = int(RoundTo60(value))   
    r_min = int(rounded / 60)
    if rounded < 0: return False
    return f"{boss.upper()} in {r_min} mins"


  view_list = ""
  li = []
  for x in value:
    boss = x.split()[0]
    left = int(x.split()[1])
    y = _ConvertRow(boss, left)
    if y is not False: li.append(y)    
  
  for x in li: view_list += f"{x} \n"
  return f"```css\n{view_list}```"  

# returns calendar with given timezone added !calendar command
def GetCalendarEmbed(_title,_timezone): 
  def _GetDay(daynumber,_timezone):
    temp = "```css\n"
    for x in var.timer_list:
      if x.day == daynumber:
        h = x._time.split(":")[0]
        m = x._time.split(":")[1]
        added_info = ""  
        time_tz = int(h) + int(_timezone)

        if time_tz >= 24: 
          time_tz -= 24
          added_info =  "(next day)"
        elif time_tz < 0:
          time_tz += 24
          added_info =  "(previous day)"

        gmt = f"{time_tz}:{m}"
        temp += f"{x.boss.upper()} at {gmt} {added_info}\n" 
    return temp + "```"

  embed = discord.Embed(title=_title, color=0xffffff)
  for x in list(range(7)):
    embed.add_field(
    name= var.day_list[x],    
    value= _GetDay(x,_timezone),
    inline=False)
  
  return embed
  
#returns the time and day given as seconds 
#day number multiplied with day_sec and it converts current time to seconds and returns it
def GetGivenTimeAsSecond(day, time):
  # 0 -> Monday | ... |6 -> Sunday
  h = int(time.split(":")[0])
  m = int(time.split(":")[1])
  result = (h * 3600) + (m * 60) + (day * day_sec)
  return result

#checks 0 , 5 , 15 minute bosses
def GetSpawn():
  #used at notify loop check it will check if theres boss before the given time as minute
  def GetLessThen(value):  #value must be minute    
    temp = []
    val_sec = (value * 60)
    for x in GetBossInfo(0):
        left = int(x.split()[1])
        if val_sec - 15 < left < val_sec + 15: temp.append(x)
    return temp

  checklist = [0,5,15]
  for x in checklist:
    temp = GetLessThen(x)
    if temp: return temp
  return 0


def RoundTo60(value):
  left = (int(value) % 60)
  main = int(value) - left
  if left < 30: left = 0
  elif left >= 30: left = 60
  return int(main + left)

def BossnameCheck(val):
  for x in var.boss_list:
    if x.name.lower() == val.lower():
      return val
  return 0


