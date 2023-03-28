import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
def funct(x): # Define the function
    return x**2+2*x+4
x = np.linspace(-10, 10, 100) # Select the x range for the function of the plot
y = funct(x) # Select the y values of the x range
result = minimize(funct, x0=0) #Find the minimum using the library provided
print("Minimum value :", result) # Print the minimum value
# Plot the function and the minimum
fig, ax = plt.subplots()
ax.plot(x, y, label='Function')
ax.plot(result.x, result.fun, 'ro', label='Minimum')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
plt.show()
