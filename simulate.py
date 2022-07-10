from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from GBM import GBM
import numpy as np
import matplotlib.pyplot as plt

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--initial_price", default=100, type=float, help="Initial price of an asset")
parser.add_argument("-d", "--drift", default=0.1, type=float, help="The drift or expected annual return")
parser.add_argument("-v", "--volatility", default=0.1, type=float, help="The volatility/spread of an asset")
parser.add_argument("-p", "--paths", default=100, type=int, help="The desired number of generated paths")
args = vars(parser.parse_args())

initial_price = args['initial_price']
drift = args['drift']
volatility = args['volatility']
n = args['paths']
interval = 1/365. # set interval to one day

stochastic_processes = []
for _ in range(n):
  stochastic_processes.append( GBM(initial_price,drift,interval,volatility) )
  
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

plt.title(f'{n} Price Paths : $\mu={drift},\ \sigma={volatility}$')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()