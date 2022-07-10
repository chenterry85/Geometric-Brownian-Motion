from GBM import GBM

initial_price = 300
drift = 0.2 # up 20% for expected turn
interval = 1/365. # one day
volatility = 0.3

stochastic_processes = []

n = 1000 # of stochastic processes
for _ in range(n):
  stochastic_processes.append(GBM(initial_price,drift,interval,volatility))
  
# simulate each stochastic process
for processes in stochastic_processes:
  tte = 1 # a year for time to expiry 
  while tte - processes.dt > 0:
    processes.time_step()
    tte -= processes.dt
    
