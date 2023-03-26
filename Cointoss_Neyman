import numpy as np
import matplotlib.pyplot as plt

n_experiments = 50
n_tosses = 50
#User inputs
if '-experiment' in sys.argv:
    p = sys.argv.index('-experiment')
    n_experiment = sys.argv[p+1]
if '-experiment' in sys.argv:
    p = sys.argv.index('-tosses')
    n_tosses = sys.argv[p+1]
# Initialize histogram
hist2d, _, _ = np.histogram2d([], [], bins=(len(np.linspace(0.1, 0.9, 50)), len(np.linspace(0.1, 0.9, 50))))

for i, true_p in enumerate(np.linspace(0.1, 0.9, 50)): # Loop through different true probabilities
    for _ in range(n_experiments): # Loop through different measured probabilities
        for j, measured_p in enumerate(np.linspace(0.1, 0.9, 50)): # Perform the experiment and count the heads, as well as calculate the measured probability of getting heads when given the true probability
            n_measured = np.sum(np.random.random((n_tosses,)) < measured_p) 
            p = np.math.comb(n_tosses, n_measured) * (true_p ** n_measured) * ((1 - true_p) ** (n_tosses - n_measured))
            hist2d[j, i] += p #Add the data into the histogram
hist2d /= np.sum(hist2d) #Normalize the histogram
x_mesh, y_mesh = np.meshgrid(np.linspace(0.1, 0.9, 50), np.linspace(0.1, 0.9, 50)) #Plot initialization
# Plot the dara
plt.pcolormesh(x_mesh, y_mesh, hist2d, cmap='gray')
plt.xlabel('True probability of heads')
plt.ylabel('Measured probability of heads')
plt.colorbar(label='Probability density')
plt.show()
