x = int(input("Enter Any number to check whether it is prime or not: "))


if x<1:
    print("Please enter a number greater than 1")
elif x==1:
    print("1 is neither prime nor composite")
elif x==2:
    print("2 is a prime number")
elif x>2:
    for i in range(2,x):
        if x%i==0:
            print(x,"is not a prime number")
            break
        else:
            print(x,"is a prime number")