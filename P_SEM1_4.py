# -*- coding: utf-8 -*-
print("\n4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.\nПрограмма должна подсказывать «больше» или «меньше» после каждой попытки.\nДля генерации случайного числа используйте код:\nfrom random import randint\nnum = randint(LOWER_LIMIT, UPPER_LIMIT)\n") 

from random import randint
print("Кто угадывает число?\n1 - пользователь\n2 - компьютер\n")
a = int(input())
if a == 1:
    num = randint(0, 1000)
    for i in range(1,11):
        print("Попытка №",i)
        n = int(input("Угадайте число : "))
        if num==n:
            print("Поздравляю!")
            break
        elif num>n:
            print("больше")
        elif num<n:
            print("меньше")
    if num!=n:
        print("Казнить, объяснительную и, чтоб к завтрему был как штык!")
elif a == 2:
    num = int(input("Загадайте число : "))
    b = y = 1000
    x = res = 0
    for i in range(1,11):
        if res==1:
            x = b
            b = b + ((y-b)//2)
        elif res==2:
            y = b
            b = b - ((b-x)//2)
        elif res==0:
            b = b//2   
        print("\nПопытка №",i)
        print("Ваше число",b,"\n1 - Ваше число больше?\n2 - Ваше число меньше?\n3 - Число угадано?\n")
        res = int(input())
        if res==3:
            print("\nУра!\n")
            break
    if num!=b:
        print("\nЕще не вечер...\n")
print("END\n")