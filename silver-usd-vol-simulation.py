import matplotlib.pyplot as plt
import numpy as np

# Constants
spot_rate = 29.06
forward_rate = 30.706
take_profit_levels = [30,35,40]
stop_loss_levels = [27,20,15]
budget_rate = 17

# Parameters for the Brownian motion
np.random.seed(5)  # for reproducibility
mu = 0.10 # drift
sigma = 1  # volatility
n = 250  # number of time points
dt = 1 / 12  # time increment (1 month)

# Simulate Brownian motion
time_points = np.linspace(1, 12, n)  # Time points now range from 1 to 12 representing months
brownian_motion = np.cumsum(np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt), size=n))
brownian_motion = brownian_motion - brownian_motion[0]  # normalize to start at 0

# Create the USD/MAD rate series (starting at the spot rate and adding the Brownian motion)
strengthening_usd_realistic = spot_rate + brownian_motion

# Plot the realistic strengthening USD scenario
plt.figure(figsize=(10, 6))
plt.plot(time_points, strengthening_usd_realistic, label='Cours de argent (USD)')
plt.scatter([1], [spot_rate], color='blue', label='Cours Spot (début)', zorder=5)
plt.axhline(budget_rate, color='black', linestyle='-', label='Cours Budget')
plt.scatter([12], [forward_rate], color='purple', label='Cours à Terme (1 an)', zorder=5)
for tp in take_profit_levels:
    plt.axhline(tp, color='green', linestyle='--', label=f'Take Profit {tp}')
for sl in stop_loss_levels:
    plt.axhline(sl, color='red', linestyle='--', label=f'Stop Loss {sl}')
plt.title("Application de la méthodologie sur un pattern de de l'Argent (USD)")
plt.xlabel('Temps (mois)')
plt.ylabel('Cours de argent (USD)')
plt.ylim(12, 40)
plt.xticks(np.arange(1, 13, step=1))  # Setting x-axis ticks from 1 to 12
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
