from numpy.random import normal
from math import sqrt

# Geometric Brownian Motion Class
class GBM:
  def __init__(self, initial_price: float, drift: float, interval: float, volatility: float) -> None:
    self.asset_prices = [initial_price]
    self.current_price = initial_price
    self.mu = drift
    self.dt = interval
    self.sigma = volatility
  
  def time_step(self) -> None:
    dW = normal(0, sqrt(self.dt) )
    dS = self.current_price * (self.mu * self.dt + self.sigma * dW)
    self.current_price += dS
    self.asset_prices.append( self.current_price) 
