year=0
for num in range(31):
    year = 2**num
print('year' + str(year))
if year%4==0:
    print('leap')
else:
    print('not leap')


