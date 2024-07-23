#


from class_a import Die

def roll_again_option():
     
    print("Would You Like To Roll Again?" )
    print("1 - Yes")
    print("2 - No")

    continue_choice = int(input(""))

    if continue_choice == 1:
        roll_dice_option()
    
    elif continue_choice == 2: 
          exit()

    else:
         print("Unknown Choice... Please Try Again")
         continue_choice()


def display_die_menu():
    print("Welcome To the Homework Menu! - Which Option Would You Like To Choose?")
    print("Option 1 - Roll Die")
    print("Option 2 - Exit")


def roll_dice_option():
     
    die1 = Die()
    Die.roll(die1)

    print(die1)

    roll_again_option()

def homework_menu():

    display_die_menu()

    choice = 0

    while choice <= 2:

        choice = int(input("Choice: "))
    
        if choice == 1:
             roll_dice_option()

        elif choice == 2:
             exit()

homework_menu()

