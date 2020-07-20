numbers = []
while True:
    playerInput = input("Enter your number or 'stop' to stop: ")
    try:
        if playerInput.lower() == "stop":
            multNum = 1
            for i in numbers:
                multNum = multNum * int(i)
            print("Your multiplied number is: " + str(multNum))
            break
        elif playerInput.isnumeric() == False:
            print("That aint no number")
        else:
            numbers.append(playerInput)
    except:
        print("ur donezo kid")
