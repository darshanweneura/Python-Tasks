n = int(input("Enter a number of which multiplication table is to be printed: "))

for i in range(1, 11):
    print(n, "x", i, "=", n*i)