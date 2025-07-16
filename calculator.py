print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")

option = int(input("choose an operation: "))
if(option in [1,2,3,4]):

    number1 = int(input("enter the  first number: "))
    number2 = int(input("enter the second number: "))

    if(option == 1):
        result = number1 + number2
    elif(option == 2):
        result = number1 - number2
    elif(option == 3):
        result = number1 * number2
    elif(option == 4):
        result = number1 / number2

else:
    print("invalid operation..")

print("the result of the operation is {}".format(result))