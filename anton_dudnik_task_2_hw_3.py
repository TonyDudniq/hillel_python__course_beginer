print("Hello Dear")
nick_name, gender, age = input('Specify your nickname, gender(M or W), and age(use numbers), through a space: ').split()
age = int(age)
if nick_name == 'admin':
    print('Привет, повелитель!')
elif nick_name == 'Женя':
    print('Советую Вам посмотреть "TENET"')
elif 10 < age < 14 and gender == 'M' or age > 30 and gender == 'M':
    print('Советую Вам посмотреть "StarWars"')
elif 22 < age < 32 and gender == 'W':
    print('Советую Вам посмотреть "Трансформеры"')
elif age < 16 and gender == 'W':
    print('Советую Вам посмотреть "Инсургент"')
elif age < 11 and gender == 'M':
    print('Советую Вам посмотреть "TMNT"')
elif nick_name == 'Guido':
    print('Огромное спасибо!')
else:
    print('Советую Вам сделать прогулку на свежем воздухе')
