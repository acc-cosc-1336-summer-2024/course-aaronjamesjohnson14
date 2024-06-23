#

from repetition import get_factorial
from repetition import sum_odd_numbers


# Homework #3 Menu

def display_menu():
    print("Welcome To the Homework #3 Menu! - Which Option Would You Like To Choose?")
    print("Option 1 - Get Factorial")
    print("Option 2 - Sum Odd Numbers")
    print("Option 3 - Exit")

def option_1():

    num = int(input("What Number 1 - 9 Would You Like To Get The Factorial Of: "))

    if 1 <= num < 10:
        result = get_factorial(num)
        print("The Factorial Of", num, "Is Equal To", result)
    else:
         print("Please Only Enter A Number 1- 9")
         option_1()

    continue_option()

def option_2():

    num = int(input("What Number 1 - 99 Would You Like To Get The Sum Of Odds For: "))
        
    if 1 <= num < 100:
             
        result = sum_odd_numbers(num)
        print("The Sum Of All The Odd Numbers Before", num, "Is Equal To", result)
        
    else:
        print("Please Only Enter A Number 1- 99")
        option_2()

    continue_option()
    
def option_3():
    print("Do You Really Want To Exit?")
    print("1 - Yes")
    print("2 - No")

    exit_choice = int(input(""))

    if exit_choice == 1:
        exit()

    elif exit_choice == 2:
         homework_3_menu()
    else:
         print("Unknown Choice... Please Try Again")
         option_3()
         
def continue_option():
     
    print("Would You Like To Continue?" )
    print("1 - Yes")
    print("2 - No")

    continue_choice = int(input(""))

    if continue_choice == 1:
        homework_3_menu()
    
    elif continue_choice == 2: 
          option_3()

    else:
         print("Unknown Choice... Please Try Again")
         continue_choice()

def homework_3_menu():

    display_menu()

    choice = 0

    while choice <= 3:

        choice = int(input("Choice: "))
    
        if choice == 1:
             option_1()

        elif choice == 2:
             option_2()

        elif choice == 3:
             option_3()


homework_3_menu()
