#


def get_p_distance(list1, list2):


    if len(list1) != len(list2):
        print ("Error! List Lengths Are Not Equal")
        exit()

    distance = 0
    length = len(list1)

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            distance += 1
    
    proportional_difference = distance / length

    return proportional_difference


def get_p_distance_matrix(list1):

    distance_matrix = []

    for i in range (len(list1)):
        row_list = []

        for j in range (len(list1)):
                row_list.append(get_p_distance((list1[i]), (list1[j])))
            
        print(row_list)

        distance_matrix.append(row_list)

    return distance_matrix





    