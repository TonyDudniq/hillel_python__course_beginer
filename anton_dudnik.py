# Создать файл (модуль) с примерами всех методов строк.

# Конкатенация
w1 = ' Hello '
w2 = 'Ruslan'
w3 = w1 + w2
print(w3)

# Дублирование строки
w4 = w3 * 2
print(w4)

# upper() - преобразует все символы нижнего регистра в строке в символы верхнего регистра и возвращает их
up = 'Hello Ruslan'.upper()
print(up)

# lower() - противоположная upper()
down = 'Hello Ruslan'.lower()
print(down)

# capitalize - Возвращает копию строки, переводя первую буквы в верхний регистр, а остальные в нижний.
cap = 'ruslan Hello'.capitalize()
print(cap)

# title() - Возвращает копию строки, в которой каждое новое слово начинается с заглавной буквы и продолжается строчными.
tit = 'hello ruslan'.title()
print(tit)

# count() - строки возвращает количество вхождений подстроки в заданной строке.
stroka = 'Hello Hello Ruslan'
cnt = stroka.count('Hello')
print(cnt)

# replace() - создания строки путем замены некоторых частей другой строки.
s1 = '!!!Hello Ruslan!!!'
s2 = s1.replace('!', '', 5)
print(s2)

# swapcase() - Возвращает копию строки, в которой каждая буква будет иметь противоположный регистр.
swap = 'hELLO rUSLAN'
case = swap.swapcase()
print(case)

# ljust() - принимает символ для прокладки его к входной строке. Затем он заменяет персонаж и делает прокладку справа от входной строки.
a = 'Hello Ruslan'
b = a.ljust(15, '~')
print(b)

# rjust() - противоположная ljust()
c = 'Hello Ruslan'
d = c.rjust(15, '*')
print(d)

# center() - Возвращает строку исходного центра, и дополняется пробелами до новой строки ширины длины. Заполнение символов по умолчанию пространство.
e = 'Hello Ruslan'
f = e.center(20, '/')
print(f)

# lstrip -
g = 'this homework is very big'
z = g.lstrip()
print(z)

# методы удаления
'#####some str####'.lstrip('#')  # => 'some str####'
'#####some str####'.rstrip('#')
'#####some str####'.strip('#')

# метод разделения
'#####some str####'.split()  # => ['#####some', 'str####']

'file.name.zip'.rsplit('.', 1)  # => ['file.name', 'zip']
    # а если нет  расширения?
'file.name.zip.bip'.partition('.')  # => ('file', '.', 'name.zip.bip')
'file.name.zip.bip'.rpartition('.')  # => ('file.name.zip', '.', 'bip')

# с помощью  join можно соединить любую последловательность строк
"".join('Hello my Dear freand'.split())

