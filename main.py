import random
#Создаём случайный список из 20 значений по 4 случайных целых чисел от -10 до 10.
a = [ [random.randint(-10,10) for i in range(4)] for k in range(20)]
print(a)
#Cоздаем список в который будем помещать комбинации пар
b=list()
#Cортировка массивов
for i in a:
    i.sort()
#Перебор чисел 
for el in a:
    if a.count(el) == 1:
        x = tuple(el)
        b.append(x)
print("Уникальные комбинации:")
print(b)
x = int(input("Введи целое число: "))
sum = 0
count = 0
for i in b:
    for el in i:
        sum +=el
    if sum < x:
        count =+1
print("Кол-во пар, чья сумма меньше:",count)
        