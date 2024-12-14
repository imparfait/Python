def oddNumbers(start,end):
    for numb in range(start,end+1):
        if numb%2!=0:
            yield numb


for odd in oddNumbers(1,10):
    print(odd)