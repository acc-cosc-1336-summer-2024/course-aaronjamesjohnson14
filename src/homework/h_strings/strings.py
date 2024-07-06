#

def get_hamming_distance(dna1,dna2):

    if len(dna1) != len(dna2):
        print ("Error! DNA Lengths Are Not Equal")
        exit()

    distance = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    
    return distance


def get_dna_complement(dna):

    dna = dna.upper()

    reversed_dna = dna[::-1]

    reversed_compliment_dna = ""

    for char in reversed_dna:

        if char == "A":
            reversed_compliment_dna += "T"

        elif char == "T":
            reversed_compliment_dna += "A"

        elif char == "C":
            reversed_compliment_dna += "G"

        elif char == "G":
            reversed_compliment_dna += "C"
        
    return reversed_compliment_dna
