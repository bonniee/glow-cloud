from LPD8806 import *
from animation import *
import time
import pywapi
import string
import feedparser


DEBUG = True

USERNAME = "allhailglowcloud"
PASSWORD = "hackprinceton"

NEWMAIL_OFFSET = 0

# Weather codes used for effects in the glowcloud
rain = [1, 8, 9, 10, 11, 12, 40]
thunderstorm = [3, 4, 37, 38, 39, 45, 47]
snow = [5, 6, 7, 13, 14, 15, 16, 17, 18, 35, 41, 42, 43, 46]
reallybad = [1, 2]
badvisibility = [19, 20, 21, 22]
windy = [23, 24]
cloudy = [27, 28, 29, 30, 36, 44]
noEffect = [25, 31, 32, 33, 34, 3200]

def lightning(led, color='ffffff'):
  twinkle = FireFlies(led, [color_hex(color)], 30)
  twinkle.run(None, 20)

def pickGradientColor(temp):
  low = -40.0
  high = 60

  percentile = (high - temp) / (high - low)
  print percentile
  bluePart = 255 * percentile
  redPart = 255 * (1.0 - percentile)
  blueHex = hex(int(bluePart))[2:]
  redHex = hex(int(redPart))[2:]
  if (len(blueHex) < 2):
    blueHex = '0' + blueHex
  if len(redHex) < 2:
    redHex= '0' + redHex
  code = redHex + '00' + blueHex  
  print code
  return code

def pickColor(temp):
  temp = int(float(temp))

  tempDict = ['000de4',]

  if temp < -10:
    return '001be5'
  elif temp < -8:
    return '0000e3'
  elif temp < -7:
    return '0c00e2'
  elif temp < -6:
    return '1900e2'
  elif temp < -5:
    return '2500e1'
  elif temp < -4:
    return '3200e0'
  elif temp < -3:
    return '3f00e0'
  elif temp < -2:
    return '4b00df'
  elif temp < -1:
    return '5800de'
  elif temp < 0:
    return '6400dd'
  elif temp < 1:
    return '7100dd'
  elif temp < 2:
    return '7d00dc'
  elif temp < 3:
    return '8900db'
  elif temp < 4:
    return '9500db'
  elif temp < 5:
    return 'a100da'
  elif temp < 6:
    return 'ad00d9'
  elif temp < 7:
    return 'b900d9'
  elif temp < 8:
    return 'c500d8'
  elif temp < 9:
    return 'd100d7'
  elif temp < 10:
    return 'd600d1'
  elif temp < 11:
    return 'd600c4'
  elif temp < 12:
    return 'd500b7'
  elif temp < 13:
    return 'd400aa'
  elif temp < 14:
    return 'd4009d'
  elif temp < 15:
    return 'd30091'
  elif temp < 16:
    return 'd20084'
  elif temp < 17:
    return 'd20078'
  elif temp < 18:
    return 'd1006b'
  elif temp < 19:
    return 'd0005f'
  elif temp < 20:
    return 'cf0053'
  elif temp < 21:
    return 'cf0047'
  elif temp < 22:
    return 'ce003b'
  elif temp < 23:
    return 'cd002f'
  elif temp < 24:
    return 'cd0023'
  elif temp < 25:
    return 'cc0017'
  elif temp < 26:
    return 'cb000b'
  elif temp < 27:
    return 'ca0000'
  elif temp < 28:
    return 'ca0b00'
  elif temp < 29:
    return 'c91700'
  elif temp < 30:
    return 'c82200'
  elif temp < 31:
    return 'c82d00'
  elif temp < 32:
    return 'c73900'
  elif temp < 33:
    return 'c64400'
  elif temp < 34:
    return 'c64f00'
  elif temp < 35:
    return 'c55a00'
  elif temp < 36:
    return 'c46500'
  elif temp < 37:
    return 'c37000'
  elif temp < 38:
    return 'c37b00'
  elif temp < 39:
    return 'c28500'
  elif temp < 40:
    return 'c19000'
  elif temp < 41:
    return 'c19a00'
  elif temp < 42:
    return 'c0a500'
  elif temp < 43:
    return 'bfaf00'
  else:
    return 'bfb900'

  # Good enough for the demo lol

def fillStrip(led, color='ffffff'):
  led.fill(color_hex(color))
  led.update()

def main():
  print pickColor(40)

  led = LEDStrip(32, False)
# lightning(led)  

  pastNewEmails = 0

  while(True):
    theWeather = pywapi.get_weather_from_yahoo('08544')
    condition = theWeather['condition']['code']
    temperature = theWeather['condition']['temp']

    nextColor = pickColor(temperature)

    fillStrip(led, nextColor)

    print 'Condition Code; ' + condition
    print 'Temp:' + temperature
    print 'Color:' + nextColor

    newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
    
    print "raw:", newmails

    if pastNewEmails < newmails:
      newmailsdiff = (newmails - pastNewEmails)
      print "You have", newmailsdiff, "new emails!"
      pastNewEmails = newmails
    elif newmails < pastNewEmails:
      pastNewEmails = newmails

#    if DEBUG:
#      print "You have", newmails, "new emails!"
#    else:
#      print "no new emails"

    time.sleep(2)


 # for i in range(-10,45):
 #   fillStrip(led, pickGradientColor(i))
 #   time.sleep(1)
  

main()
