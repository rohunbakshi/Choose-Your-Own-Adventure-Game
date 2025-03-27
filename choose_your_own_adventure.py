answer = input("What is your name: ")
print("Welcome to this adventure", answer, "At any point, type q to quit. ")

while True:
    answer = input(
        "You come to a river with a bridge over it. Would you like to swim accross the river or walk across the bridge? ")
    if answer.lower() == "swim":
        answer = input(
            "The river is flowing very fast and you get swept downstream. You start floating towards a waterfall. You see a branch you can grab ahold of and a rock you can sit on. Would you like to try and grab the branch or try and climb the rock? ")
        if answer.lower() == "grab":
            print(
                "The branch breaks and you fall down the waterfall. You lose. Try Again!")
            continue
        elif answer.lower() == "climb":
            print(
                "You slipped while trying to climb the rock, and fell down the waterfall. You lose. Try Again!")
            continue
        elif answer.lower() == "q":
            break
        else:
            print("Not a valid option. You lose!")
            continue
    elif answer.lower() == "walk":
        answer = input(
            "You make it safely across the brige. After some time you come across a cave. You go inside, and see a diamond sitting on the floor. Do you try and grab the diamond or leave the cave? ")
        if answer.lower() == "grab":
            print(
                "You grab the diamond and the floor beneath you opens to reveal a hole. You lose. Try Again!")
            continue
        elif answer.lower() == "leave":
            print("You leave the cave and decide to go home. You win!")
            break
        elif answer.lower() == "q":
            break
        else:
            print("Not a valid option. You lose!")
            continue
    elif answer.lower() == "q":
        break
    else:
        print("Not a valid option. You lose!")
        continue

print("Thanks for playing!")
quit()
