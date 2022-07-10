from GBM import GBM
import numpy as np
import matplotlib.pyplot as plt

initial_price = 400
drift = 0.4 # up 20% for expected turn
interval = 1/365. # one day
volatility = 0.2

stochastic_processes = []

n = 1000 # of stochastic processes
for _ in range(n):
  stochastic_processes.append(GBM(initial_price,drift,interval,volatility))
  
# simulate each stochastic process
for process in stochastic_processes:
  tte = 1 # a year for time to expiry 
  while tte - process.dt > 0:
    process.time_step()
    tte -= process.dt
    
# graph
for process in stochastic_processes:
  x = np.arange(len(process.asset_prices))
  y = process.asset_prices
  plt.plot(x,y)
  
plt.show()