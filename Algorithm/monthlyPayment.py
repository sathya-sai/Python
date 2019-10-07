p=float(input('Enter principle loan amount'))
y=int(input('Enter the years'))
R=float(input('Percentage of interest'))
n=12*y
r=R/(12*100)
payment = p*r/(1-(1+r)**(-n))
print(payment)