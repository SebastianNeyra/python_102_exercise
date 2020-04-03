# Pick a number from 0-6
day = int(input('Day (0-6) ? '))

# Number between 0 to 6 prints a certain day of the week
if day == 0:
    print('Sunday')
elif day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
else:
    print("Wait. What day is it? ")