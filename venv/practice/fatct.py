

def fact(x):

    f = 1
    for i in range(1,x+1):
        f = f * i
    return f

x = int(input("Enter a number for factorial: "))

result = fact(x)

print ("Factorial of input number is : ", result)


