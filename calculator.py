while True:

    islem = input("Welcome to the calculator! Please enter an operation: ")
    liste = []

    liste = islem.split("+")
    if len(liste) == 2:
        if liste[0].isdigit() and liste[1].isdigit():
            print(int(liste[0]) + int(liste[1]))
        else:
            print("This is an invalid input")
        continue

    liste = islem.split("-")
    if len(liste) == 2:
        if liste[0].isdigit() and liste[1].isdigit():
            print(int(liste[0]) - int(liste[1]))
        else:
            print("This is an invalid input")
        continue    

    liste = islem.split("*")
    if len(liste) == 2:
        if liste[0].isdigit() and liste[1].isdigit():
            print(int(liste[0]) * int(liste[1]))
        else:
            print("This is an invalid input")
        continue            
    
    liste = islem.split("/")
    if len(liste) == 2:
        if liste[0].isdigit() and liste[1].isdigit():
            print(int(liste[0]) / int(liste[1]))
        else:
            print("This is an invalid input")
        continue

    if islem == "stop":    
        break
    else:
        print("This is an invalid input")