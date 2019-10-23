
def fact(n):
    if (n == 0):
        return 1

    return n * fact(n-1)

x = int(input("Enter a number for factorial : "))

result = fact(x)

print ("Factorial of input number is : ", result)
