from datetime import datetime
import pytz
import discord 

##########################################################
################# VARIABLES ##############################
##########################################################
class Boss:
    def __init__(self, boss, _time, day):
        self.boss = boss
        self._time = _time
        self.day = day

day_sec = 86400
UTC = pytz.utc
utc = datetime.now(UTC)
cur_day = utc.weekday()
cur_day_sec = (cur_day * day_sec)
cur_seconds = (utc.hour * 3600) + (utc.minute * 60) + utc.second + cur_day_sec

all_boss_list = [
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
  Boss("Kzarka", "06:00", 5),
  Boss("Nouver", "07:00", 5),
  Boss("Kutum", "09:00", 5),
  Boss("Muraka", "11:00", 5),
  Boss("Quint", "11:00", 5),
  Boss("Karanda", "13:00", 5),
  Boss("Kutum", "15:00", 5),
  Boss("Garmoth", "16:00", 5),
  Boss("Mudster", "18:30", 5),
  Boss("RedNose", "18:30", 5),
  Boss("DimTree", "20:30", 5),
  Boss("Bheg", "20:30", 5),
  Boss("Kzarka", "22:00", 5),
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
    "Muraka",
    "Quint",
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
    "quint",
    "muraka",
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
    "muraka": "https://imgur.com/xRGrSeS.png",
    "quint": "https://imgur.com/bDQpObP.png",
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
    "muraka": 0x0A43A3,
    "quint": 0x8C797A,
}

##########################################################
################# BOT FUNCTIONS ##########################
##########################################################

#returns todays bosses that hasnt been spawned and next days bosses
def GetBossInfoData():
    array_list = []
    temp_list = GetBossListbyDay(cur_day)
    temp_list2 = GetBossListbyDay (cur_day + 1)
    for x in temp_list:
        sec = GetGivenTimeAsSecond(cur_day, x._time)
        left = sec - cur_seconds
        if left < -15: continue
        array_list.append(x.boss + " " + str(left) + " " + str(x.day))

    for x in temp_list2:
        sec = GetGivenTimeAsSecond(cur_day + 1, x._time)
        left = sec - cur_seconds
        array_list.append(x.boss + " " + str(left) + " " + str(x.day))

    return array_list

#converts get_boss_list arraylist to discord text
def GetListView(value):
    temp = value
    view_list = ""
    li = []
    for x in temp:
        boss = x.split()[0]
        left = int(float(x.split()[1]))
        y = ConvertToBossView(boss, left)
        if y is not False: li.append(y)
    
    for x in li: view_list += str(x) + "\n"

    view_list = "```css\n" + view_list + "```"
    return view_list

#used at notify loop check it will check if theres boss before the given time as minute
def GetSpawnsLessThen(value):  #value must be minute    
    li = GetBossInfoData()
    temp = []
    for x in li:
        left = int(x.split()[1])
        if left < -15: continue
        elif left > (value * 60) + 15 or left < (value * 60) - 15: continue
        temp.append(x)
    return temp

def GetCalendarDayList(daynumber,_timezone):
  temp = "```css\n"
  for x in all_boss_list:
    if x.day == daynumber:
      h = x._time.split(":")[0]
      m = x._time.split(":")[1]
      added_info = ""  
      time_tz = int(h) + int(_timezone)
         
      if time_tz >= 24: 
        time_tz -= 24
        added_info =  " (next day)"
      elif time_tz < 0:
        time_tz += 24
        added_info =  " (previous day)"

      gmt = str(time_tz) + ":" + m
      temp += x.boss.upper() + " at " + gmt + added_info + "\n" 
  return temp + "```"

def GetCalendarEmbed(_title,_timezone): 
  x = discord.Embed(title=_title, color=0xffffff)
  val = 0
  while val < 7:
    x.add_field(
    name= day_list[val],    
    value= GetCalendarDayList(val,_timezone),
    inline=False)
    val+=1
  return x
  
#converts the given boss and value left to spawn as seconds to view value as bot posts it to boss-info channel
def ConvertToBossView(boss, value):
  rounded = int(RoundTo60(value))
  
  rest = ""
  if rounded < 0: return False
  elif rounded <= 60 and rounded > 0 :
    rest = str(rounded) + " sec"
  elif rounded < 3600 and rounded > 60:
    rest = " in " + str(int(rounded / 60)) + " mins"
  elif rounded > 3600:
    if rounded < 7200: 
      rest = str(int(rounded / 3600)) + " hour and " + str(int((rounded % 3600) / 60)) + " mins"
    rest =  str(int(rounded / 3600)) + " hours and " + str(int((rounded % 3600) / 60)) + " mins"

  return boss.upper() + " in " + rest
  

#returns the time and day given as seconds 
#day number multiplied with day_sec and it converts current time to seconds and returns it
def GetGivenTimeAsSecond(day, _time):
  # 0 -> Monday | ... |6 -> Sunday
  h = int(_time.split(":")[0])
  m = int(_time.split(":")[1])
  result = (h * 3600) + (m * 60) + (day * day_sec)
  return result


#returns the icon link for the given boss name 
def GetIconLink(boss):
  for x in icon_list:
      if x.split()[0] == boss.lower():
          return x.split()[1]
   
#returns list of bosses in given day
def GetBossListbyDay(val):
  temp = []
  for x in all_boss_list:
    if x.day == val:
      temp.append(x)
  return temp


#returns the list of all spawn times for given boss name 
def GetBossListbyName(boss):
    temp = []
    for x in all_boss_list:
        if x.boss.lower() != boss.lower(): continue

        sec = GetGivenTimeAsSecond(x.day, x._time)
        left = sec - cur_seconds
        if left <= 0: left = sec - cur_seconds + 604800     

        temp.append(x.boss + " " + str(left) + " " + str(x.day))

    return temp

#rounds the number given to 60 if it is higher than 30 else 0
def RoundTo60(value):
  a = (int(value) % 60)
  b = int(value) - a
  if a < 30: a = 0
  elif a >= 30: a = 60
  return b + a




