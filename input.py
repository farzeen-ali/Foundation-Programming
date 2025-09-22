# User input
# firstName = input("Enter your name: ")
# print("Hello,", firstName)

# Type casting
# age = input("Enter your age: ")
# print(type(age))
# age = int(age)
# print(type(age))

#Conditional Statements
# number = int(input("Enter Your number: "))
# if number > 0:
#     print("Number is +ve")
# else:
#     print("Number is -ve")

# if Else if ladder
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks < 50 and marks >= 0:
    print("F")
else:
    print("Invalid Marks")