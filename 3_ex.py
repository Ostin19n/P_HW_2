# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.



number = int(input('Введите число '))
search = 1
power = -1
while search <= number:
    search *= 2
    power += 1
    print(power, end=' ')
print('\n')