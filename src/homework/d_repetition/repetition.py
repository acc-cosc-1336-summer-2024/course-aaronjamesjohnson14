#

def get_factorial(num):
     
    factorial = 1 

    for i in range (1, num + 1):

        factorial = factorial * i

    return factorial
     
def sum_odd_numbers(num):

    sum = 0
    value = 1

    while value <= num:

        sum += value
        value += 2

    return sum

