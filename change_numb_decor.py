def change_numbers_decorator(input_func):
    def output_func(*args):
        arguments=[]
        for arg in args:
            if isinstance(arg, (int, float)):
                if arg<0:
                    arg=1
            arguments.append(arg)
        return input_func(*arguments)
    return output_func
    

@change_numbers_decorator
def function(*args):
    for arg in args:
        print(arg, end=" ")

function(22,500,"jeff", -4,99.99,-3.5)