a = float(input('Hello. How old are you?  '))
b = input('What is your name?  ')
if a > 16 and a<70:
    print('Welcome', b, 'on our website.')
elif a == 16:
    print('Dear', b, 'need to wait one year.')
elif a >= 70 and a <=90:
    print('You are lucky', b, 'welcome.')
elif a > 121:
    print('You are not real', b)
else:
    print("I'm sorry", b, 'you are too young.')

