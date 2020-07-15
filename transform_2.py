'''
transform.py
Math 266
Summer 2020
Project #1


    This program will create a square 1 x 1 grid of points.
    Then four different tranformations will be applied to the
    "box". The box and its image will be displayed.
'''

# import standard libraries

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

# generate the data using a list comprehension
# see https://docs.python.org/3/tutorial/datastructures.html

data = np.array([[x, y] for x in np.arange(0, 1.01, .01) for y in np.arange(0, 1.01, .01)])

# define transformation matrices

A = np.array([[1, 0], [-2, 1]])
theta = 5*pi/4  # rotate the box 225 degrees
B = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
C = np.array([[-1, 0], [0, 1]])


def tran(v):
    temp = np.array([2, 1])
    return v + temp


# def tran(v):
#     v = np.array(v)
#     return v + [2, 1]

# apply the transformation to the data points (vectors).
# recall v.T  represents the traspose of v.


mat = [A, B, C]

for k in range(3):
    plt.subplot(2, 2, k+1)
    tran_data = mat[k] @ data.T
    tran_data = tran_data.T
    plt.plot(*zip(*data), '.', c='k', markersize=.2)
    plt.plot(*zip(*tran_data), '.', c='b', alpha=.5, markersize=.2)

    plt.axis('equal')
    plt.axis((-4, 4, -4, 4))
    plt.grid(True)
    plt.title(f'Transformation_{k+1}', fontsize=10)

plt.subplot(2, 2, 4)
tran_data = tran(data)

plt.plot(*zip(*data), '.', c='k', markersize=.2)
plt.plot(*zip(*tran_data), '.', c='b', alpha=.5, markersize=.2)

plt.axis('equal')
plt.axis((-4, 4, -4, 4))
plt.grid(True)
plt.title(f'Transformation_4', fontsize=10)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=.5)

plt.suptitle('Transformations', fontsize=20)
# # save the plot
#plt.savefig('transform.png')
