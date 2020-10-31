import matplotlib.pyplot as plt
import numpy as np

def normal( mu, sigma2 ) :
  # Your code to generate the normal random variable goes here
  
  
# This part draws the graph  
indices, samples = 100*[0], 100*[0]
for i in range(100) : 
  indices[i] = i+1
  samples[i] = normal( 5, 9 )
  
plt.plot( indices, samples, 'ko' )
plt.xlabel("Numerical index")
plt.ylabel("Value of random variable")
plt.savefig("normal_rvs.png")
