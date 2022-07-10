from numpy import double


class GBM:
  def __init__(self, initial_price: float, drift: float, interval: float, volatility: float) -> None:
    self.asset_price = [initial_price]
    self.current_price = initial_price
    self.mu = drift
    self.dt = interval
    self.sigma = volatility
    