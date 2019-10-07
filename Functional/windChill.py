import math
windchil=0
t=float(input('Temprature in Fahrenheit(less than 50)'))
s=float(input('Speed in miles per second(b\w 3 qnd 120)'))
windchil=13.12+0.6215*t- 11.37*math.pow(s, 0.16) + \
          0.3965*t*math.pow(s, 0.16)
print(windchil)