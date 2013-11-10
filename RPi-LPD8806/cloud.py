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
  twinkle.run(None, 50)

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

  tempDict = ['000de4', '001be5', '0000e3', '0c00e2'
    '1900e2', '2500e1',
    '3200e0', '3f00e0',  '4b00df',
    '5800de',  '6400dd', '7100dd',
    '7d00dc',
    '8900db',
    '9500db', 'a100da', 'ad00d9','b900d9', 'c500d8',
    'd100d7', 'd600d1', 'd600c4', 'd500b7', 'd400aa',
    'd4009d', 'd30091', 'd20084', 'd20078', 'd1006b',
    'd0005f', 'cf0053', 'cf0047', 'ce003b', 'cd002f',
    'cd0023', 'cc0017', 'cb000b', 'ca0000', 'ca0b00', 'c91700',
    'c82200','c82d00', 'c73900', 'c64400', 'c64f00', 'c55a00',
    'c46500', 'c37000', 'c37b00', 'c28500', 'c19000', 'c19a00',
    'c0a500','bfaf00', 'bfb900']

  if (temp < -10):
    return tempDict[0]
  else:
    index = temp + 10
    if (index >= len(tempDict)):
      return tempDict[len(tempDict) -1]
    return tempDict[index]

  # Good enough for the demo lol

def fillStrip(led, color='ffffff'):
  led.fill(color_hex(color))
  led.update()

def doRain(led, color='ffffff'):
  #led.all_off()
  #led.set(10, color_hex(color))
  #led.update()
  r = Rain(led, color_hex(color), 20, 3)
  r.run(None, 200)

def main():
  print pickColor(40)

  led = LEDStrip(32, False)
# lightning(led)  

  pastNewEmails = 0


  while(True):
    DEBUG = True
    if (DEBUG):
      lightning(led)
      continue
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

    time.sleep(2)


 # for i in range(-10,45):
 #   fillStrip(led, pickGradientColor(i))
 #   time.sleep(1)
  

main()
