#

from dictionary import get_p_distance
from dictionary import get_p_distance_matrix


def display_text_homework_6_menu():
    print("Welcome To the Homework #6 Menu! - Which Option Would You Like To Choose?")
    print("Option 1 - Get Distance Matrix")
    print("Option 2 - Exit")

def homework_6_menu():


    display_text_homework_6_menu()

    choice = 0

    while choice <= 2:

        choice = int(input("Choice: "))
    
        if choice == 1:
             option_1_get_matrix()

        elif choice == 2:
             exit()

        else:
             print ("Invalid Selection... Please Select An Option 1-2")
             choice = 0

def option_1_get_matrix():
     
        list_of_lists = []

        print("Please Enter Your List of Lists")
        list_of_lists = input()

        result = get_p_distance_matrix(list_of_lists)
        return result
    
        homework_6_menu()
        
homework_6_menu()