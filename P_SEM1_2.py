# -*- coding: utf-8 -*-
print("\n2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.\nДано a,b,c, - стороны предпологаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой \nдвух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами\nне существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.\n")
a,b,c = map(int,input("Введите стороны треугольника a,b и c, разделенные знаком пробела : ").split(" ",2))
# print(type(a))
# print(b)
if ((int(a) or int(b) or int(c))!=0) and (a==b or b==c or a==c):
	res = "Треугольник равнобедренный" 
elif a==b==c:
	res = "Треугольник равносторонний" 
else:
	res = "Треугольник разносторонний" 
if a+b<c or a+c<b or b+c<a:
	res = "Треугольника не существует"
print(res)