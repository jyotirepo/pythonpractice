print("Third Number Pattern")
lastNumber = int(input("Enter a number for pattern: "))
for row in range(1, lastNumber):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
