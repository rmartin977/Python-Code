# zero.py
# @Robert Martin
# 10/25/20

''' This program prompts the user for
    1. A polynomial function
    2. An interval to search
    3. A tolerance.
    
    and returns the zero for that function.
    
'''

import numpy as np
import matplotlib.pyplot as plt
import os

os.system('clear')

# prompt user for function definition, interval and tolerance.  No error checking on input.

f_str = input(
    "Please enter the function. Note for exponentiation use x**2 for x^2\n\n f(x)= ")

I = eval(input("\nplease enter the interval using the format [a,b]:  "))

tol = float(input("\nPlease enter the tolerance:   "))


def f(x):
    return eval(f_str)


def create_sub_intervals(I):
    ''' This function inputs and interval  [a,b] and partitions
        this interval into 10 equally spaced sub_intevals. The list of
        sub_intevals is returned.
    '''

    vals = np.linspace(I[0], I[1], 11)
    temp = [[vals[k], vals[k+1]] for k in range(len(vals)-1)]
    return temp


def find_sub_interval(subs):
    for val in subs:
        if(f(val[0])*f(val[1]) < 0):
            return val
    return 0


subs = create_sub_intervals(I)

result = find_sub_interval(subs)

if result == 0:
    print("\nSorry no zero found")

while (result[1]-result[0]) > tol:

    subs = create_sub_intervals(result)

    result = find_sub_interval(subs)


print(f"\n The zero is in the interval {result}\n")
