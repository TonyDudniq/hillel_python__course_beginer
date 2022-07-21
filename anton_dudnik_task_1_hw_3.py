year = input('Еnter your year of birth: ')
check = year.isdigit()
if check is True:
    age = 2022 - int(year)
    if age == 21:
        print('You should visit Holland.')
    elif age > 21:
        print('You should visit Vietnam.')
    else:
        print('Travell everywhere')
if check is False:
    print('Wrong enter, try again')
