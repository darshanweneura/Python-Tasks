def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b  

def division(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b

def square(a):
    return a*a

def square_root(a):
    if a < 0:
        return "Error: Square root of negative number is not defined."
    return a**0.5

def power(a,b):
    return a**b 

def modulus(a,b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b 

def factorial(n):
    if n < 0:
        return "Error: Factorial of negative number is not defined."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def calculate():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Power")
    print("8. Modulus")
    print("9. Factorial")

    choice = input("Enter choice (1-9): ")

    if choice in ['1', '2', '3', '4', '7', '8']:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == '1':
            print("the addition is", addition(n1, n2))
        elif choice == '2':
            print("the subtraction is", subtraction(n1, n2))
        elif choice == '3':
            print("the multiplication is", multiplication(n1, n2))
        elif choice == '4':
            print("the division is", division(n1, n2))
        elif choice == '7':
            print(f"the power of {n1} is", power(n1, n2))
        elif choice == '8':
            print(f"the modulus of {n1} is", modulus(n1, n2))

    elif choice in ['5', '6', '9']:
        n = float(input("Enter a number: "))

        if choice == '5':
            print(f"the square of {n} is", square(n))
        elif choice == '6':
            print(f"the square root of {n} is", square_root(n))
        elif choice == '9':
            if n.is_integer():
                print(f"the factorial of {int(n)} is", factorial(int(n)))
            else:
                print("Error: Factorial is only defined for integers.")

    else:
        print("Invalid input")


calculate()