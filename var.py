##########################################################
################# VARIABLES ##############################
##########################################################

class Timer:
  def __init__(self, boss, _time, day):
    self.boss = boss
    self._time = _time
    self.day = day
  
class Boss:
  def __init__(self, name, icon, color):
    self.name = name
    self.icon = icon
    self.color = color

night_time_list = [  
  "03:40"
  "07:40",
  "11:40",
  "15:40",
  "19:40",
  "23:40",
]

timer_list = [
  Timer("RedNose", "07:00", 0),
  Timer("Mudster", "07:00", 0),
  Timer("Kutum", "09:00", 0),
  Timer("Nouver", "11:00", 0),
  Timer("Karanda", "13:00", 0),
  Timer("Kutum", "15:00", 0),
  Timer("Karanda", "18:30", 0),
  Timer("Nouver", "18:30", 0),
  Timer("Kzarka", "20:30", 0),
  Timer("Karanda", "22:00", 0),
  Timer("Bheg", "07:00", 1),
  Timer("DimTree", "07:00", 1),
  Timer("Karanda", "09:00", 1),
  Timer("Kzarka", "11:00", 1),
  Timer("Kutum", "13:00", 1),
  Timer("Karanda", "15:00", 1),
  Timer("Garmoth", "16:00", 1),
  Timer("RedNose", "18:30", 1),
  Timer("Mudster", "18:30", 1),
  Timer("Kutum", "20:30", 1),
  Timer("Nouver", "22:00", 1),
  Timer("RedNose", "07:00", 2),
  Timer("Mudster", "07:00", 2), 
  Timer("Karanda", "11:00", 2),
  Timer("Nouver", "13:00", 2),
  Timer("Offin", "14:00", 2),
  Timer("Kzarka", "15:00", 2),
  Timer("Bheg", "18:30", 2),
  Timer("DimTree", "18:30", 2),
  Timer("Karanda", "20:30", 2),
  Timer("Kutum", "22:00", 2),
  Timer("DimTree", "07:00", 3),
  Timer("Bheg", "07:00", 3),
  Timer("Nouver", "09:30", 3),
  Timer("Kutum", "11:00", 3),
  Timer("Nouver", "13:00", 3),
  Timer("Offin", "14:00", 3),
  Timer("Kzarka", "15:00", 3),
  Timer("RedNose", "18:30", 3),
  Timer("Mudster", "18:30", 3),
  Timer("Nouver", "20:30", 3),
  Timer("Kzarka", "22:00", 3),
  Timer("RedNose", "07:00", 4),
  Timer("Mudster", "07:00", 4),
  Timer("Karanda", "09:00", 4),
  Timer("Kutum", "11:00", 4),
  Timer("Nouver", "13:00", 4),
  Timer("Offin", "14:00", 4),
  Timer("Kzarka", "15:00", 4),
  Timer("Garmoth", "16:00", 4),
  Timer("DimTree", "18:30", 4),
  Timer("Bheg", "18:30", 4),
  Timer("Nouver", "20:30", 4),
  Timer("Kzarka", "20:30", 4),
  Timer("Kutum", "22:00", 4),
  Timer("Kzarka", "06:00", 5),
  Timer("Nouver", "07:00", 5),
  Timer("Kutum", "09:00", 5),
  Timer("Muraka", "11:00", 5),
  Timer("Quint", "11:00", 5),
  Timer("Karanda", "13:00", 5),
  Timer("Kutum", "15:00", 5),
  Timer("Garmoth", "16:00", 5),
  Timer("Mudster", "18:30", 5),
  Timer("RedNose", "18:30", 5),
  Timer("DimTree", "20:30", 5),
  Timer("Bheg", "20:30", 5),
  Timer("Kzarka", "22:00", 5),
  Timer("Karanda", "06:00", 6),
  Timer("Kutum", "07:00", 6),
  Timer("Kzarka", "09:00", 6),
  Timer("Kutum", "11:00", 6),
  Timer("DimTree", "13:00", 6),
  Timer("Bheg", "13:00", 6),
  Timer("Vell", "14:00", 6),
  Timer("Nouver", "15:00", 6),
  Timer("Kzarka", "15:00", 6),
  Timer("Garmoth", "16:00", 6),
  Timer("RedNose", "18:30", 6),
  Timer("Mudster", "18:30", 6),
  Timer("Karanda", "20:30", 6),
  Timer("Kzarka", "20:30", 6),
  Timer("Nouver", "22:00", 6),
]

boss_list = [
  Boss("kzarka", "https://imgur.com/95OFQTe.png", 0xff0000),
  Boss("karanda", "https://imgur.com/OVOrFZR.png", 0xdedcd7),
  Boss("nouver", "https://imgur.com/Kt5EOxS.png", 0xffaa00),
  Boss("kutum", "https://imgur.com/Ip4i2oa.png", 0xaa00ff),
  Boss("garmoth", "https://imgur.com/P9MjV5A.png", 0xff4000),
  Boss("offin", "https://imgur.com/mAzQglC.png", 0x00c8ff),
  Boss("vell", "https://imgur.com/TfeSrVn.png", 0x007bff),
  Boss("bheg", "https://imgur.com/GI59dGr.png", 0x754105),
  Boss("dimtree", "https://imgur.com/5F9SMhe.png", 0x036910),
  Boss("mudster", "https://imgur.com/H3Wdmnf.png", 0x727136),
  Boss("rednose", "https://imgur.com/uyChweO.png", 0x86040d),
  Boss("muraka", "https://imgur.com/xRGrSeS.png", 0x0A43A3),
  Boss("quint", "https://imgur.com/bDQpObP.png", 0x8C797A),
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

welcome_message = '**EN**\n**Welcome to Melissia Boss Timer discord server!**\nIn order to get notified you have to go to <#851464537479315557> channel and react to the roles with the name of bosses you want to get notified. Enjoy not missing any boss!\nUse !help command in server to get more information.\n\n*This is not made by Melissia Games developers.*\n\n**TR**\n**Melissia Boss Timer discord sunucusuna hoşgeldiniz!**\nBildirim almak için <#851464537479315557> kanalına gidip istediğiniz boss isimlerinin olduğu rollere tepki veriniz. Hiçbir bossu kaçırmamanın tadını çıkarın!\n!help komutunu kullanarak daha fazla bilgi edinebilirsiniz.\n\n*Bu bot Melissia Games geliştiricileri tarafından yapılmamıştır.*\n\n**RU**\n**Добро пожаловать на сервер разногласий Melissia Boss Timer! **\nЧтобы получить уведомление, вам нужно перейти на канал <#851464537479315557> и реагировать на роли, указав имена боссов, которых вы хотите получать. Наслаждайтесь, не пропуская ни одного босса! \n Используйте команду! help на сервере, чтобы получить дополнительную информацию.\n\n*Это сделано не разработчиками Melissia Games.*\n\n*Переведено с помощью Google Translate*'
