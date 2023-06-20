"""
@author : Tien Nguyen
@date   : 2023-06-19
"""
import numpy
import matplotlib.pyplot

numpy.random.seed(2023)

def is_normal(theta, x_point):
    return x_point[0] % theta[0] == 0 and x_point[1] % theta[1] == 0

if __name__ == '__main__':
   theta = [1, 2]
   x_point = [3, 3]
   print(is_normal(theta, x_point)) 
