# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):

    bigNum = 0
    for e in list_of_numbers:
        if e > bigNum:
            bigNum = e
    return bigNum


print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0