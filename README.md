# Geometric Brownian Motion

Geometric Brownian Motion is a stochastic, non-linear process to model asset price. As a rule of thumb , there is an [academic paper](https://www.researchgate.net/publication/325987061_Forecasting_Share_Prices_of_Small_Size_Companies_in_Bursa_Malaysia_Using_Geometric_Brownian_Motion) that stated that GBM works best for forecasting when limited to max 2 week lookahead.

The equations is as follows:
$$ \LARGE {dS \over S} = \mu dt + \sigma dW $$

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
4. Run `python3 simulate.py -i <initial price> -d <drift> -v <volatility> -p <paths>` (use `--help` for more information)

### Example
`python3 simulate.py -i 400 -d 0.2 -v 0.3 -p 200`
<br>
<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60279271/178163238-6947c3d0-fa75-417f-a51e-43e09411db59.png" alt="drawing" width="600"/>
</p>
