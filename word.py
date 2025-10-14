# Q1. Count Vowels and Consonants in a Word
def startWord():
    word = input("Enter a word: ").lower()
    vowels = "aeiou"
    vCount = 0
    cCount = 0

    for ch in word:
        if ch.isalpha():
            if ch in vowels:
                vCount += 1
            else:
                cCount += 1
    print("Vowels: ", vCount)
    print("Consonants: ", cCount)

startWord()