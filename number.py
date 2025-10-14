# Q2. Find the Largest and Smallest Number from User Input List
def number():
    numbers = []
    n = int(input("Enter a number:"))

    for i in range(n):
        val = int(input("Enter a value: "))
        numbers.append(val)
    
    print("Largest: ", max(numbers))
    print("Smallest: ", min(numbers))

number()