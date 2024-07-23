#
import random
class Die:
    __roll_value = 0

    def roll(self):
        self.__roll_value = random.randint(1,6)

        
    def get_rolled_value(self):
        return self.__roll_value


    def __str__(self):
        return f"The Rolled Value Of Your Die Is {self.__roll_value}"



die1 = Die()
die2 = Die()
die3 = Die()

Die.roll(die1)
Die.roll(die2)
Die.roll(die3)


print (die1)