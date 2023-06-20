"""
@author : Tien Nguyen
@date   : 2023-06-19
"""
import numpy 
def is_belong(theta, x_point): 
    theta = numpy.asanyarray(theta) 
    x_point = numpy.asanyarray(x_point) 
    value = theta @ x_point
    return value == 0

if __name__ == '__main__':
    print(is_belong([1, 2], [-5, 3]))
