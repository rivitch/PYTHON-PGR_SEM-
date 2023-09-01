print("\nВыведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.\n")

for i in range(2,10):
    for j in range(1,11):
        if i==2 and j==1: 
            print("\t\t\t\t",i+1,"*",j,"=",(i+1)*j)  
        elif i<3:
            print("\t\t",i,"*",j,"=",i*j,"\t",i+1,"*",j,"=",(i+1)*j)  
            if (i+1)*j==30: print("")
        elif 3<i<5:
            print(i,"*",j,"=",i*j,"\t",i+1,"*",j,"=",(i+1)*j,"\t",i+2,"*",j,"=",(i+2)*j)
            if (i+2)*j==60: print("")
        elif 6<i<8:
            print(i,"*",j,"=",i*j,"\t",i+1,"*",j,"=",(i+1)*j,"\t",i+2,"*",j,"=",(i+2)*j)
            if (i+2)*j==90: print("")
        pass