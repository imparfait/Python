#Ex 1
fruits = ("apple", "banana", "orange", "apple", "mango", "banana")
fruit= input("Enter the name of the fruit: ")
count = fruits.count(fruit)
print(f"The fruit '{fruit}' appears {count} times.")
#Ex 2
fruits = ("apple", "banana", "orange", "bananamango", "strawberry-banana", "mango")
name = input("Enter the name of the fruit: ")
count = sum(1 for fruit in fruits if name in fruit)
print(f"The fruit '{name}' appears as a part of {count} elements.")
#Ex 3
manufacturers = ("Toyota", "Honda", "Ford", "Toyota", "BMW", "Toyota", "Honda")
name = input("Enter the manufacturer to replace: ")
word = input("Enter the replacement word: ")
list = []
for manufacturer in manufacturers:
    if manufacturer == name:
        list.append(word)
    else:
        list.append(manufacturer)
tuple = tuple(list)
print("Updated tuple:", tuple)
#Ex 4
numbers = (1, 23, 456, 78, 9, 3456, 123, 56, 7, 890)
count = {}
for number in numbers:
    num = len(str(abs(number)))
    count[num] = count.get(num, 0) + 1
print(numbers)
for digits, count in sorted(count.items()):
    print(f"{digits}  — {count} element(s)")
