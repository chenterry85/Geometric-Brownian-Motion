# Geometric Brownian Motion

Geometric Brownian Motion is a stochastic, non-linear process to model asset price.
The equations is as follows:
$$ \LARGE {dS \over S} = \mu dt + \sigma dW$$

- $dS$ - Change in asset price over time interval
- $S$ — Asset price of the previous interval
- $\mu$ — The drift or the expected return for the time interval
- $dt$ — The change in time (one interval)
- $\sigma$ — Volatility term (a measure of spread)
- $dW$ — Change in Brownian motion term

### Use python to generate sample paths for any given asset price
1. Install Python3.6+
2. Clone this repository
3. Provide parameters (initial price, drift, volatility, # generated of paths)
4. Run `python simulate.py -i <initial price> -d <drift> -v <volatility> -p <paths>` (use `--help` for more information)
