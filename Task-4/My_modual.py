
import calculator as calc

def show_menu():
    print("\n===== SMART CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")


while True:

    show_menu()

    try:
        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Thank you for using Smart Calculator!")
            break

        elif choice in range(1, 6):

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = calc.add(num1, num2)
                
            elif choice == 2:
                result = calc.subtract(num1, num2)
                
            elif choice == 3:
                result = calc.multiply(num1, num2)
                
            elif choice == 4:
                result = calc.divide(num1, num2)
                
            elif choice == 5:
                result = calc.modulus(num1, num2)
                
            elif choice == 6:
                result = calc.power(num1, num2)
                

            print("Result:", result)

        else:
            print("Invalid choice! Select between 1 and 8.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except Exception as e:
        print("Unexpected error:", e)
