import time
def timeDecorator(input_func):
    def output_func():
        start_time = time.time()
        numb=input_func()
        end_time = time.time()
        funcTime=end_time-start_time
        return numb, funcTime
    return output_func    

@timeDecorator
def listNumb():
    numbers=[]
    for n in range(1,100000):
        if n%2==0:
            numbers.append(n)
    return numbers

print(listNumb())
