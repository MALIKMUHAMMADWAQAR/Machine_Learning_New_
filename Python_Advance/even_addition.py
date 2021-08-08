def fun(numbers):
    sum = 0
    for number in numbers:
        if(number%2 == 0):
            sum += number
        else:
            continue
    print("Sum of even number is : {}".format(sum))
            
print("Best of luck ! for more look at module")

if __name__ == "main":
    
    print("Its a module to add even function \n")
    print("if you want to use only and didn't want to print this statement when this module is exported\n")
    print("put this in main function")