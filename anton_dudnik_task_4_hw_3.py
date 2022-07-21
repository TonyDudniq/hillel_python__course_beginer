days, hours = map(int, input('"Введите количество_земных_дней, количество_часов, через пробел"').split())
sol = (days + hours / 24) * 1.02595675
print(f'Количество солов: {round(sol, 2)}')