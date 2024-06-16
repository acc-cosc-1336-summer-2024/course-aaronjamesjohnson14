#

from decisions import get_options_ratio
from decisions import get_faculty_rating

options = float(input("What are your amount of options? "))
total = float(input("What is your total amount? "))

ratio = (get_options_ratio(options, total))

faculty_rating = get_faculty_rating(ratio)

print ("Your Faculty Rating is", faculty_rating)
