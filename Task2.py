x = int(input('Would you like to convert \n 1. Minutes To Hours? \n or \n 2. Hours To Minutes? \n (Please only answer either 1 or 2 for your choice): '))

if x == 1:
    min = int(input('Enter an amount of minutes to be converted to hours: '))
    hrs = min / 60
    print(str(min) + " minutes is equal to " + str(hrs) + " Hours!")

if x == 2:
    hrs = int(input('Enter an amount of hours to be converted to minutes: '))
    mins = hrs * 60
    print(str(hrs) + ' hours is equal to ' + str(mins) + ' minutes!')

if x != 1 or 2:
    print('Valid answer not entered (please enter either 1 or 2)')
    exit()
