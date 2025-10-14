# Loops
# start end updation
# while
# i = 1
# while i <= 10:
#     print(i)
#     i+=1
# print("Loop End")

# For in range

# i = 1
# for i in range(1,6):
#     print(i)

# for in

# fruits = ["Apple", "Mango", "Strawberry"]
# for fruit in fruits:
#     print(fruit)

# Break & Continue
# for i in range(1,6):
#     if i == 3:
#         # break
#         continue
#     print(i)

# Task

correctPassword = "1234"
attempts = 0

while attempts < 3:
    password = input("Enter your password: ")
    if password == correctPassword:
        print("Login!")
        break
    else:
        print("Wrong Password")
        attempts += 1
if attempts == 3:
    print("Account Blocked!")