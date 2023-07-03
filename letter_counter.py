Alphabetic = "abcdefghijklmnopqrstuvwxyz"

userInput = input("Enter text: ")


def letterChecker(text):
    print("The count of letters in text is:[", end="")
    first = True
    for AtoZ in Alphabetic:
        counter = 0
        for LETTERS in text:
            if AtoZ.lower() == LETTERS.lower():
                counter = counter + 1
        if counter > 0:
            if first:
                print("{}:{}".format(AtoZ, counter), end="")
                first = False
            elif not first:
                print(",{}:{}".format(AtoZ, counter), end="")

    print("]")


letters = False
for i in userInput:
    if i.isalpha():
        letters = True

if userInput.isspace():
    print("your text does not contain any letter")
elif not letters:
    print("your text does not contain any letter")
else:
    letterChecker(userInput)
