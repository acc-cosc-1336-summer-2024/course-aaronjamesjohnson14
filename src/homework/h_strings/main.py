#

from strings import get_hamming_distance
from strings import get_dna_complement

def display_dna_menu():
    print("Welcome To the Homework #5 Menu! - Which Option Would You Like To Choose?")
    print("Option 1 - Get Hamming Distance")
    print("Option 2 - Get DNA Compliment")
    print("Option 3 - Exit")
    
def homework_5_menu():

    display_dna_menu()

    choice = 0

    while choice <= 3:

        choice = int(input("Choice: "))
    
        if choice == 1:
             option_1_hamming()

        elif choice == 2:
             option_2_reverse_compliment()

        elif choice == 3:
             exit()

        else:
             print ("Invalid Selection... Please Select An Option 1-3")
             choice = 0

def continue_option():
     
    print("Would You Like To Continue?" )
    print("1 - Yes")
    print("2 - No")

    continue_choice = int(input(""))

    if continue_choice == 1:
        homework_5_menu()
    
    elif continue_choice == 2: 
          exit()

    else:
         print("Unknown Choice... Please Try Again")
         continue_choice()

def option_1_hamming():

    print("What Are The Two DNA Stands You Wish To Find The Hamming Distance Between?")
    print("Please Ensure Your Strands Only Valid Nucleotides")
    
    dna1 = input("DNA Strand #1: ")
    dna2 = input("DNA Strand #2: ")

    valid_nucleotides = validate_nucleotides(dna1) #validating that the DNA strands only contain ACTGactg
    if valid_nucleotides == False:
        print("Unknown Nucleotide Found... Please Reenter Your DNA Strand")
        option_1_hamming()

    valid_nucleotides = validate_nucleotides(dna2) #validating that the DNA strands only contain ACTGactg
    if valid_nucleotides == False:
        print("Unknown Nucleotide Found... Please Reenter Your DNA Strand")
        option_1_hamming()

    result = get_hamming_distance(dna1, dna2)

    print("The Hamming Distance Between Your Two DNA Strands Are", result)

    continue_option()

def option_2_reverse_compliment():
     
     print("What DNA Strand Would You Like To Find The Reverse Compliment Of?")
     dna = input("DNA Strand: ")

     valid_nucleotides = validate_nucleotides(dna) #validating that the DNA strands only contain ACTGactg
     if valid_nucleotides == False:
        print("Unknown Nucleotide Found... Please Reenter Your DNA Strand")
        option_2_reverse_compliment()
          
     result = get_dna_complement(dna)

     print("The Reverse Compliment Of Your DNA Strand Is", result)

     continue_option()

def validate_nucleotides(sequence):

    valid_nucleotides = 'ACTGactg'
    for char in sequence:
         if char not in valid_nucleotides:
              return False
    return True
     

homework_5_menu()





