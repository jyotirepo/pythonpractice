from array import *

arr = array('i', [])

n = int(input("Enter a length: "))

for i in range(n):
    x = int(input("enter a value: "))
    arr.append(x)

print(arr)

vals = int(input("Enter the value to search : "))

k = 0
for e in arr:
    if e == vals:
        print (k)
        break
    k = k +1

print(arr.index(vals))

