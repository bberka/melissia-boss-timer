from datetime import datetime
import pytz
import discord 
array_list = []
temp_list = []
temp = []

day_sec = 86400
UTC = pytz.utc
utc = datetime.now(UTC)
cur_day = utc.weekday()
cur_day_sec = (cur_day * day_sec)
cur_seconds = (utc.hour * 3600) + (utc.minute * 60) + utc.second + cur_day_sec

##########################################################
################# BOT FUNCTIONS ##########################
##########################################################

#returns the time and day given as seconds 
#day number multiplied with day_sec and it converts current time to seconds and returns it
def get_time_as_sec(day, _time):
  # 0 -> Monday | ... |6 -> Sunday
  h = int(_time.split(":")[0])
  m = int(_time.split(":")[1])
  result = (h * 3600) + (m * 60) + (day * day_sec)
  return result

def get_day_list(daynumber,_timezone):
  #if daynumber is not int or daynumber < 0 or daynumber > 6: return False
  all_list = monday_list + tuesday_list + wednesday_list + thursday_list + friday_list + saturday_list + sunday_list
  added_tz = 0
  h = ""
  m = ""
  add = ""
  temp = "```css\n"
  for x in all_list:
    if x.day == daynumber:
      h = x._time.split(":")[0]
      m = x._time.split(":")[1]
      added_tz = int(h) + int(_timezone)

      if added_tz >= 24: 
        gmt = str(added_tz - 24) + ":" + m
        add = x.boss.upper() + " at " + gmt + " (next day)"
      elif added_tz < 0:
        gmt = str(added_tz + 24) + ":" + m
        add = x.boss.upper() + " at " + gmt + " (previous day)"
      else: 
        gmt = str(added_tz) + ":" + m
        add = x.boss.upper() + " at " + gmt

      temp += add + "\n" 
  return temp + "```"

def get_all_embed(_title,_timezone):
  x = discord.Embed(title=_title, color=0xffffff)
  x.add_field(
      name="Monday",
      value= get_day_list(0,_timezone),
      inline=False
      )
  x.add_field(
      name="Tuesday",
      value=get_day_list(1,_timezone),
      inline=False
      )
  x.add_field(
      name="Wednesday",
      value= get_day_list(2,_timezone),
      inline=False
      )
  x.add_field(
      name="Thursday",
      value= get_day_list(3,_timezone),
      inline=False
      )
  x.add_field(
      name="Friday",
      value= get_day_list(4,_timezone),
      inline=False
      )
  x.add_field(
      name="Saturday",
      value= get_day_list(5,_timezone),
      inline=False
      )
  x.add_field(
      name="Sunday",
      value= get_day_list(6,_timezone),
      inline=False
      )
  return x



#returns todays bosses that hasnt been spawned and next days bosses
def get_boss_list():
    day_sec = 86400
    UTC = pytz.utc
    utc = datetime.now(UTC)
    cur_day = utc.weekday()
    cur_seconds = (utc.hour * 3600) + (utc.minute *  60) + round_60(utc.second) + (cur_day * day_sec)

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
        if left < -15: continue
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
        if left < -15: continue
        elif left > (value * 60) + 15 or left < (value * 60) - 15: continue
        temp.append(x)
    return temp

#returns the icon link for the given boss name 
def get_icon_link(boss):
  for x in icon_list:
      if x.split()[0] == boss.lower():
          return x.split()[1]
   

#returns the list of all spawn times for given boss name
def get_one_boss_list(boss):
    all_list = monday_list + tuesday_list + wednesday_list + thursday_list + friday_list + saturday_list + sunday_list
    day_sec = 86400
    UTC = pytz.utc
    utc = datetime.now(UTC)
    cur_day = utc.weekday()
    cur_seconds = (utc.hour * 3600) + (utc.minute * 60) + utc.second + (cur_day * day_sec)
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

#rounds the number given to 60 if it is higher than 30 cuz round function it self is only rounds to 1,10,100 
def round_60(value):
  a = (int(value) % 60)
  b = int(value) - a
  if a < 30: a = 0
  elif a >= 30: a = 60
  return b + a

#converts the given boss and value left to spawn as seconds to view value as bot posts it to boss-info channel
def convert(boss, value):
  rounded = int(round_60(value))
  if rounded < 0: return False
  elif rounded <= 60 and rounded > 0 :
      return boss.upper() + " in " + str(rounded) + " sec"
  elif rounded < 3600 and rounded > 60:
      return boss.upper() + " in " + str(int(rounded / 60)) + " mins"
  elif rounded > 3600:
    if rounded < 7200: 
      return boss.upper() + " in " + str(int(rounded / 3600)) + " hour and " + str(int((rounded % 3600) / 60)) + " mins"
    return boss.upper() + " in " + str(int(rounded / 3600)) + " hours and " + str(int((rounded % 3600) / 60)) + " mins"
  return False


##########################################################
################# VARIABLES ##############################
##########################################################
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