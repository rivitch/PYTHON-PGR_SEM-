# -*- coding: utf-8 -*-
print("\n3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.\nИспользуйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. \nСделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.\n")

n = ""
j = 0
while n.isdigit()==False or 0<=int(n)>100000:
    n = input("Введите неотрицательное число и не больше 100000 : ")   
r = int(n)+1
for i in range(2,r):
    if int(n)%i == 0 :
        j=j+1
    #print(int(n),int(n)%i,i,j,r)
if j>1:
    print("\nЧисло составное")
elif int(n)==0 or int(n)==1:
    print("\nЧисла 0 и 1 не являются ни простыми, ни составными")    
else:
    print("\nЧисло простое")
print("\nEND\n")        
