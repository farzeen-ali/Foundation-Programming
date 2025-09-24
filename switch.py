# day = int(input("Enter day number (1-7): "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid Day")

a = int(input("First Number: "))
b = int(input("Second Number: "))
op = input("Enter any Op: ")

match op:
    case "+":
        print("Result a + b: ", a+b)
    case "-":
        print("Result a - b: ", a-b)
    case "*":
        print("Result a x b: ", a*b)
    case "/":
        print("Result a / b: ", a/b)
    case _:
        print("Ivalid Operation!")

