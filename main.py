active = True
counter = 0
while active == True:
    userInput=input('For store hours, say "store hours".\nFor pharmacy, say "pharmacy".\nTo speak to a representative, say "representative".\n')
    if userInput == "store hours":
        print("Today's store hours are from 9am, to 5pm, thank you for calling.")
        active = False
    elif userInput == "pharmacy":
        print("Transfering you to pharmacy.")
        active = False
    elif userInput == "representative":
        print("Transfering you to a representative.")
        active = False
    else:
        if counter <3:
            print("Sorry, I didn't quite get that, please try again")
            counter = counter + 1
        if counter ==3:
            print("I'm having trouble understanding you. Let me transfer you to a representative.")
            active = False