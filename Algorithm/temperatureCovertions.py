a=int(input('Enter 1 to covert c-f\n2 to covert f-c'))
if a==1:
    c=float(input('Enter temperature in celsius'))
    result=(c*(9/5))+32
    print('The Temperature in Fahrenheit:'+format(result))
if a==2:
    f=float(input('Enter temperature in Fahrenheit'))
    result=(f-32) *5/9
    print('The Temperature in Celsius:'+format(result))
else:
    print("invalid")
