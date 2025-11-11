"""
Financial System Reliability Simulation
---------------------------------------
Author: Sung Jung
Description:
This project models how financial market volatility affects system reliability
using real stock data (AAPL) and reliability engineering metrics.

Steps:
1. Download real financial data from Yahoo Finance.
2. Compute volatility (proxy for market stress).
3. Simulate stochastic system failures based on volatility.
4. Compute reliability metrics (uptime, failure rate, MTBF).
5. Visualize reliability decay and market volatility trends.
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 Download Financial Data
ticker = "AAPL"
data = yf.download(ticker, start="2023-01-01", end="2024-01-01", interval="1d")

# 2 Compute Volatility
data["Volatility"] = (data["High"] - data["Low"]) / data["Open"]

# 3 Simulate System Reliability
np.random.seed(42)
data["System_Load"] = data["Volatility"] / data["Volatility"].max()
data["Failure"] = np.where(data["System_Load"] > np.random.rand(len(data)), 1, 0)

# 4 Compute Reliability Metrics
num_failures = data["Failure"].sum()
failure_rate = num_failures / len(data)
uptime_ratio = 1 - data["Failure"].mean()
MTBF = len(data) / num_failures if num_failures > 0 else np.inf


# 5 Reliability Curve R(t)
time = np.arange(len(data))
R_t = np.exp(-failure_rate * time)


# 6 Visualizations
plt.figure(figsize=(12, 6))
plt.plot(time, R_t, label="Reliability R(t)", color="green")
plt.title(f"Reliability Curve for {ticker}")
plt.xlabel("Days")
plt.ylabel("R(t) - Probability of Survival")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Volatility"], label="Volatility", color="blue")
plt.scatter(
    data[data["Failure"] == 1].index,
    data[data["Failure"] == 1]["Volatility"],
    color="red",
    label="Failures",
)
plt.title(f"{ticker} Market Volatility vs Simulated System Failures")
plt.xlabel("Date")
plt.ylabel("Volatility (Normalized)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 7 Correlation & Summary
corr = data["Volatility"].corr(data["Failure"])
print(f"\n📊 Reliability Metrics for {ticker}")
print(f"Uptime Ratio: {uptime_ratio:.2f}")
print(f"Failure Rate: {failure_rate:.4f}")
print(f"Mean Time Between Failures (MTBF): {MTBF:.2f} days")
print(f"Correlation (Volatility ↔ Failures): {corr:.2f}")

print("\n📘 Summary:")
print(f"- {ticker} had {num_failures} simulated failures during the study period.")
print(f"- The system maintained {uptime_ratio*100:.1f}% uptime.")
print(f"- Reliability decayed with λ = {failure_rate:.4f} per day.")
print("→ Interpretation: Higher market volatility corresponds to increased system stress and lower reliability.")


# 8 Save Data
data.to_csv("financial_reliability_data.csv", index=True)
print("\n✅ Data saved to financial_reliability_data.csv")
