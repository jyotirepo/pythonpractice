# more on lambda for Even/odd number

nums = int(input("enter a number to check odd/even: "))


even = lambda nums : nums%2==0
result = even(nums)
print(result)

#odd = lambda nums : nums%2!=0
#result1 = int(odd(nums))
#print(result1)
