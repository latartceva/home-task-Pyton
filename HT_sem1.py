# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# n = int(input('Введите трехзначное число: '))
# a = n // 100
# c = n % 10
# b = n // 10  % 10
# print('Сумма цифр трехзначного цисла ', a + b + c )


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры:
# 6 -> 1 4 1
# 24 -> 4 16 4 60 -> 10 40 10

# s = int(input('Введите количество сделанных журавликов: ',))
# if s % 6 == 0:
#     print('Сережа и Петя сделали по ', (s//6), 'Катя ', (4*s//6))
# else:
#     print('Не подходит по условию')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет 
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр 
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета
# Примеры:
# 385916 -> yes
# 123456 -> no

# n = int(input('Введите шестизначный номер билетика ',))
# a = n // 1000
# b = n % 1000
# if ((a // 100 + a % 10 + a // 10 % 10) == (b // 100 + b % 10 + b // 10 % 10)):
#     print('Да, билетик счастливый')
# else:
#     print('Нет, билетик не счастливый')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить kдолек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры: Примечание: каждое считывание производится с новой строки
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек шоколада по вертикали  ',))
m = int(input('Введите количество долек шоколада по горизонтали ',))
k = int (input('Введите количество долек ',))
if k <= m * n and (k % n == 0 or k % m == 0):
    print('yes')
else:
    print('no')

