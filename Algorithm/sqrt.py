import math
c=float(input('Enter the non negative integer'))
t=c
epsilon = 1.0e-15;

while ((t - c / t) > epsilon * t):
    t = (c / t + t) / 2.0
    print(t)

