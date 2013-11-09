from LPD8806 import *
from animation import *
import time
import pywapi
import string



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
  if (temp < -40):
    return '0000cc'
  elif temp < -30:
    return '0000ff'
  elif temp < 0:
    return '0000ff'
  elif temp < 10:
    return '00ddff'
  elif temp < 15:
    return 'ffffcc'
  elif temp < 20:
    return 'ffff00'
  elif temp < 25:
    return 'ff9900'
  elif temp < 30:
    return 'cc9900'
  elif temp < 35:
    return 'cc3300'
  elif temp < 40:
    return 'ff0000'
  elif temp < 45:
    return '880000'
  else:
    return '880000'

def fillStrip(led, color='ffffff'):
  led.fill(color_hex(color))
  led.update()

def main():
  print pickColor(40)

  led = LEDStrip(32, False)
# lightning(led)  

  while(True):
    theWeather = pywapi.get_weather_from_yahoo('08544')
    condition = theWeather['condition']['code']
    temperature = theWeather['condition']['temp']

    nextColor = pickColor(temperature)

    fillStrip(led, nextColor)

    print 'Condition Code; ' + condition
    print 'Temp:' + temperature
    print 'Color:' + nextColor

    time.sleep(60)


 # for i in range(-10,45):
 #   fillStrip(led, pickGradientColor(i))
 #   time.sleep(1)
  

main()
