import random

def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        # select a random value of the list as the pivot
        pivot = A.pop( random.randint( 0, len(A)-1 ) )

        # separate values smaller than pivot from those bigger or equal than the pivot
        less, greater = [], []
        for val in A:
            if val < pivot:
                less.append( val )
            else:
                greater.append( val )

        # concat sorted smaller values + pivot + sorted greater values
        return quick_sort(less) + [pivot] + quick_sort(greater)

A = [3, 4, 2, 5, 3, 8, 1]
print( quick_sort(A) )