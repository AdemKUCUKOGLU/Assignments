
def converter(millisecond):
        
    hours = millisecond//(60*60*1000)
    remainder = millisecond%(60*60*1000)
    minutes = remainder//(60*1000)
    remainder = remainder%(60*1000)
    seconds = remainder//1000
    remainder = remainder%1000

    output = ""
    if hours > 0:
        output+= str(hours) + " hour/s "
    if minutes > 0:
        output+= str(minutes) + " minute/s "
    if seconds > 0:
        output+= str(seconds) + " second/s "
    if millisecond < 1000:
        output+= str(millisecond) + " millisecond/s"

    return output

while True:
    millisecond = input ("enter milliseconds: ")
    if millisecond.lower() == "exit":
        print("Exiting the program... Good Bye")
        break
    elif (not millisecond.isdecimal()) or int(millisecond) < 1:
        print("Not Valid Input !!!")
        continue
    else:
        print(converter(int(millisecond)))    