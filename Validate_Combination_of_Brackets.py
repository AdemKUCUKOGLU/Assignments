def brackets(letter):
    stack = []
    brack2 = { "(" : ")", "{" : "}", "[" : "]"}

    for l in letter:
        if l in ["(", "[", "{"]:
            stack.append(l)
        elif stack and  l == brack2[stack[-1]]:
            stack.pop()
        else:
            return False
    return True

while True:
    letter = input ("enter brackets : ")
    if letter.lower() == "exit":
        break
    print(brackets(letter))
    