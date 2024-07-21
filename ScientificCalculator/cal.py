import math
def scientific_calculator():
    while True:
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: "))
        choice = input("""Choose the operation to be performed:
        Add
        Sub
        Mul
        Div
        Cos
        Tan
        Sin
        Floor
        Log
        Square
        Cube
        Exponent(EXP)
        """).strip().upper()
        if choice == 'ADD':
            result = value1 + value2
            print("The sum is:", result)
        elif choice == 'SUB':
            result = value1 - value2
            print("The subtraction is:", result)
        elif choice == 'MUL':
            result = value1 * value2
            print("The multiplication is:", result)
        elif choice == 'DIV':
            if value2 != 0:
                result = value1 / value2
                print("The division is:", result)
            else:
                print("Undefined")
        elif choice == 'COS':
            result = math.cos(value1)
            result1 = math.cos(value2)
            print("The cos of value 1 and value 2 is:", result, result1)
        elif choice == 'TAN':
            result = math.tan(value1)
            result1 = math.tan(value2)
            print("The tan of value 1 and value 2 is:", result, result1)
        elif choice == 'SIN':
            result = math.sin(value1)
            result1 = math.sin(value2)
            print("The sin of value 1 and value 2 is:", result, result1)
        elif choice == 'FLOOR':
            result = value1 // value2
            print("The floor is:", result)
        elif choice == 'LOG':
            result = math.log(value1)
            result1 = math.log(value2)
            print("The log of value 1 and value 2 is:", result, result1)
        elif choice == 'SQUARE':
            result = value1 * value1
            result1 = value2 * value2
            print("The square of value 1 and value 2 is:", result, result1)
        elif choice == 'CUBE':
            result = value1 * value1 * value1
            result1 = value2 * value2 * value2
            print("The cube of value 1 and value 2 is:", result, result1)
        elif choice == 'EXP':
            power = int(input("Enter power: "))
            result = math.pow(value1, power)
            result1 = math.pow(value2, power)
            print("The exponent of value 1 and value 2 is:", result, result1)
        ask = input("Do you want to use again? (Y/N): ").strip().upper()
        if ask != 'Y':
            print("Thank you for using the calculator")
            break
scientific_calculator()
