male_list   = []
female_list = []

for x in range(6):
    user_name = input('Enter your name--')

    gender = input('Please select your gender--')

    if gender == 'M' or gender == 'm':
        male_list.append(user_name)

    elif gender == 'F' or gender == 'f':
        female_list.append(user_name)

    else :
        print ('Select the valid gender')

    print("----------------------->")

for x in male_list:
    print('Mr.',x)

for y in female_list:
    print('Mrs.',y )
