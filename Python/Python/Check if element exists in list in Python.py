# How to write a Python program that swaps the first and last elements of a list


def swap_first_and_last(val):
    if len(val)>1:
        #swap the fisrt and last elements
        val[0],val[-1]=val[-1],val[0]
    return val;

val = [3,1,4,19];
print(swap_first_and_last(val));

