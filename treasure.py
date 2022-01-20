print("welcome to the tresure haunt game")
direction=input("to find the treasure you have to go either left or right: ").lower()
if direction=="left":
    decission=input("now u can wait or swim: ").lower()
    if decission=="wait":
        colour=input("now u have to choose between red ,green, or yellow: ").lower()
        if colour=="yellow":
            print("waah!!! u have win the tresure")
        elif colour=="green":
            print("ohhhh there is a crocodile.game over")
        elif colour=="red":
            print("it's fire,game is over")
        else:
            print("entered colour doesnot exist")
    else:
        print("u have lost the game")
else:
    print("finished")