print("Welcome to my game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print("You are old enough to play!")

    want_to_play = input("Do you want to play? ").lower()
    if want_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's Play")

        left_or_right = input("First choice...left or right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake...Do you swim across or around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river, which do you go to (river/house)?  ")
            if ans == "house":
                print("You go to the house and are greeted by the owner...he doesn't like you and you lose 5 health.")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game.")
                else:
                    print("You have survived..you win!")


            else:
                print("You fell in the river and lost..")

        else:
            print("You fell down and lost.")


    else:
        print("Quit the game.")

else:
    print("You are not old enogh to play!")     