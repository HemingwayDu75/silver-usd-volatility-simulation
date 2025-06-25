# silver-usd-volatility-simulation
Stochastic simulation of silver (XAG/USD) price scenarios using Brownian motion to assess forward exposure, budget targets, and market risk thresholds.
Silver (USD) Price Simulation using Brownian Motion
This Python script simulates the possible price path of silver (XAG/USD) over a 12-month horizon using a Brownian motion model. It includes a spot price, forward rate, stop-loss and take-profit levels, and a budget threshold to visualize upside and downside risk scenarios.

🎯 Objective

To project the future behavior of silver prices under a stochastic path using drift and volatility, and assess whether strategic thresholds (budget, take-profit, stop-loss) are likely to be reached.

🧮 Model Assumptions

The simulation is based on a discrete Brownian motion model with drift:


P(t+1) = P(t) + μ·dt + σ·√dt·ε
Where:

μ = 10% annualized drift

σ = 100% annualized volatility

dt = 1/12 (monthly increments)

ε ~ N(0,1), independent standard normal shocks

📊 Parameters

These values can be modified in the script to adapt the simulation:


spot_rate = 29.06              # Initial spot price of silver (USD)
forward_rate = 30.706          # Forward price after 12 months
budget_rate = 17               # Target budget reference
take_profit_levels = [30, 35, 40]
stop_loss_levels = [27, 20, 15]
🖥️ Requirements

Python 3.8+

Libraries:

numpy

matplotlib

Install them via pip if needed:

nginx
Copier
Modifier
pip install numpy matplotlib
▶️ How to Use

Save the script as silver_simulation.py.

Run it in a Python environment:

python silver_simulation.py

The script will generate a plot displaying:

Simulated silver price path over 12 months

Spot price and forward rate

Take-profit and stop-loss levels

Budget price level

📈 Output

The chart will help visualize whether the current strategy aligns with the risk thresholds given realistic volatility assumptions.

🧠 Use Cases

Commodity hedging strategy testing

Risk budgeting for trading desks or corporate treasury

Visual explanation of potential future volatility scenarios
