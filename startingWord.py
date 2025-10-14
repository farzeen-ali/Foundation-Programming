# Q4. Find Words Starting with a Specific Letter (Using List + Loop + if)

def startWith():
    words = ["apple", "mango", "strawberry"]
    letter = input("Enter a letter: ").lower()
    print("Starts with a letter: ")
    for w in words:
        if w.startswith(letter):
            print(w)

startWith()
