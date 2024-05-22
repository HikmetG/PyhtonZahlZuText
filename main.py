import functions
while(True):
    print("Geben Sie Ihr Zahl (q : Quit)")
    number = input()
    if number == "q":
        break
    print(functions.turnNumberToText(number))