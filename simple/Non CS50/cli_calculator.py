try:
    expression = input("Input: ")
    num1, operator, num2 = expression.split()
    num1, num2 = float(num1), float(num2)

    match operator:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)
        case _:
            print("Incorrect value")

except ValueError:
    print("incorrect format of input")

except ZeroDivisionError:
    print("cannot divide by zero!")


    