# ascii design logo
print("""
 _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|    
 """)
print("Welcome to treasure island.\nYour mission id to find the treasure.")

# step 1. choosing the right direction
print("You're at a cross road. Where do you want to go?")
choice1 = input("Type \"left\" or \"right\"\n").lower()
if choice1 == "left":
    print("You\'ve come to a lake.\nThere is an island in the middle of the lake.")
    choice2 = input("Type 'wait' to wait for a boat.\nType 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        over_point = 0
        while over_point < 1:
            print("You arrive at the island unharmed.\nThere is house with 3 doors.\nOne yellow, one blue, and one red.")
            choice3 = input("Which color do you choose?\n").lower()
            if choice3 == "yellow":
                print("It's a room of ghost. Game Over.")
                over_point += 1
            elif choice3 == "red":
                print("It's a room full of fire. Game Over.")
                over_point += 1
            elif choice3 == "blue":
                print("you found the treasure. You Win!")
                over_point += 1
            else:
                print("You chose a door that doesn't exist. Please choose the door again.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")