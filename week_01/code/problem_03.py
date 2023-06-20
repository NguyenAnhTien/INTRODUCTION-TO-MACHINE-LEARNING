"""
@author : Tien Nguyen
@date   : 2023-06-19
"""
import numpy as np
import matplotlib.pyplot as plt

theta = np.array([1, 2])  # Normal vector defining the hyperplane

# Generate some data points for plotting
x = np.linspace(-1, 10, 100)
y = (-theta[0] * x) / theta[1]  # Hyperplane equation: theta[0]*x + theta[1]*y = 0

# Plot the hyperplane
plt.plot(x, y, label='Hyperplane')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Set aspect ratio and limits
plt.gca().set_aspect('equal')
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Show the plot
plt.show()

