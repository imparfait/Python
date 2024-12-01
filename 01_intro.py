# Ex 1
a=int(input("Enter the number- "))
b=a%2
if b==0:
    print(a, "- Even number")
elif b!=0:
    print(a, "- Odd number")
#Ex 2
a=int(input("Enter the number- "))
if a%7==0:
    print(a, " - Number is multiple 7")
else:
    print(a, "- Number isn't multiple 7")    
#Ex 3
a=input("Enter the number- ")
b=input("Enter the number- ")
if a>b:
    print(a, " - max")
elif a<b:
    print(b, " - max")
else:
    print(a, "=", b)        
#Ex 4
a=input("Enter the number- ")
b=input("Enter the number- ")
if a<b:
    print(a, "is min")
elif a>b:
    print(b, "is min")
else:
    print(a, "=", b)        
#Ex 5
a=int(input("Введіть число- "))
b=int(input("Введіть число- "))
print("Виберіть яку дію виконати над числами: \n\t-введіть 1, щоб додати чисел; \n\t-введіть 2, щоб відняти числа; \n\t-введіть 3, щоб знайти середнє арифметичне; \n\t-введіть 4, щоб знайти добуток чисел.")
c=int(input("Виберіть дію, яку хочете виконати- "))
if c==1:
    print("Сума=", a+b)
elif c==2:
    print("Різниця=", a-b)
elif c==3:
    print("Серднє арифметичне=", (a-b)/2)
elif c==4:
    print("Добуток=", a*b)
else:
    print("Ви ввели не вірне число")           