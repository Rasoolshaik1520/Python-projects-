import calculator_app
print("Welcome to the calculator app.")

print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. modulo")
print("6. square_root")
print("7. power")

choice = input("Enter the choice (1/2/3/4/5/6/7): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

if choice == '1':
    print("Result:", calculator_app.add(num1, num2))
elif choice == '2':
    print("Result: ",calculator_app. subtract(num1, num2))
elif choice == '3':
    print("Result:", calculator_app.multiply(num1, num2))
elif choice == '4':
    print("Result:", calculator_app. divide(num1, num2))
elif choice == '5':
    print("Result:", calculator_app.modulo(num1, num2))
elif choice == '6':
    print("Result:", calculator_app.square_root(num1))
elif choice == '7':
    print("Result:", calculator_app.power(num1, num2))

else:
    print("Invalid input")
